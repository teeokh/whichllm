from config import app, db
from models import *
from flask import request, jsonify 
from recommendations import top_llms_for_usecase
from llm_chatbot.gpt_chatbot import categorise_text

# TODO add '/api' to the api routes (and change this in the frontend parts that receive the routes)

@app.route('/')
@app.route('/home')
def home():
    return jsonify({'message': 'Welcome to WhichLLM'})

@app.route('/api/usecases')
def get_all_usecases():
    usecases = db.session.query(Usecase).join(benchmark_usecase, Usecase.id == benchmark_usecase.c.usecase_id).distinct().all()
    json_usecases = [usecase.to_json() for usecase in usecases]
    return jsonify(json_usecases)

@app.route('/api/usecase/<int:usecase_id>', methods=['GET'])
def get_usecase(usecase_id):
    usecase = Usecase.query.get_or_404(usecase_id)
    json_usecase = usecase.to_json()
    return jsonify(json_usecase)

@app.route('/api/benchmarks-usecases')
def get_benchmarks_usecases():
    benchmarks_usecases = db.session.query(Benchmark.name, Usecase.name).\
        join(benchmark_usecase, Benchmark.id == benchmark_usecase.c.benchmark_id).\
        join(Usecase, Usecase.id == benchmark_usecase.c.usecase_id).\
        all()
    grouped_benchmarks_usecases = {}
    for benchmark, usecase in benchmarks_usecases:
        if usecase not in grouped_benchmarks_usecases:
            grouped_benchmarks_usecases[usecase] = [benchmark]
        else:
            grouped_benchmarks_usecases[usecase].append(benchmark)
    return jsonify(grouped_benchmarks_usecases)

@app.route('/api/benchmarks')
def get_all_benchmarks():
    benchmarks = Benchmark.query.all()
    json_benchmarks = [benchmark.to_json() for benchmark in benchmarks]
    return jsonify(json_benchmarks)

# Recommendations route, displaying top LLMs with score in JSON format
@app.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    
    # Set query parameters for URL routing -> can dynamically change recommendation parameters
    usecase_id = request.args.get('usecase_id', type=int)
    status_filter = request.args.get('status_filter', default=None)
    top_n = request.args.get('top_n', default=3, type=int)
    
    # If usecase ID is not entered
    if usecase_id is None:
        return jsonify({'message': 'A usecase must be selected'}), 400
    
    # If usecase ID is not recognised
    usecase = Usecase.query.filter_by(id=usecase_id).first()
    if not usecase:
        return jsonify({'message': f'Usecase with id {usecase_id} not found'}), 404
    
    recommendations, benchmark_names = top_llms_for_usecase(usecase_id=usecase_id, status_filter=status_filter, top_n=top_n)
    json_recommendations = [{'llm':llm.to_json(), 'score': round(score, 1)} for llm, score in recommendations]
    
    # If no recommendations found / no benchmarks for that usecase
    if not json_recommendations:
        return jsonify({'message': 'No recommendations found for this usecase'}), 404

    return jsonify({
        'recommendations':json_recommendations, 
        'benchmarks':benchmark_names
            })
    
@app.route('/api/llm-scores', methods=['GET'])
def get_all_llm_scores():
    # Fetch all LLM scores
    llm_scores = db.session.query(llm_benchmark).all()

    # Group the LLM scores by LLM
    grouped_llm_scores = {}
    for llm_score in llm_scores:
        llm = db.session.query(LLM).get(llm_score.llm_id)
        benchmark = db.session.query(Benchmark).get(llm_score.benchmark_id)
        score = llm_score.score

        if llm.name not in grouped_llm_scores:
            grouped_llm_scores[llm.name] = [{ 'benchmark': benchmark.name, 'score': score }]
        else:
            grouped_llm_scores[llm.name].append({ 'benchmark': benchmark.name, 'score': score })

    # Return the grouped LLM scores in JSON format
    return jsonify(grouped_llm_scores)


@app.route('/api/categorise', methods=['POST'])
def categorise():
    data = request.json
    user_input = data.get('text')

    if not user_input:
        return jsonify({'error': 'No text provided'}), 400
    
    try: 
        category = categorise_text(user_input)
        usecase = Usecase.query.filter_by(name=category).first()
        if usecase:
            return jsonify({'usecase_id': usecase.id, 'usecase_name': category}), 200
        else:
            return jsonify({'error': 'Usecase not found'}), 404
    except RuntimeError as e:
        return jsonify({'error': str(e)}), 500
