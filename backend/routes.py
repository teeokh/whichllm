from config import app, db
from models import *
from flask import request, jsonify 
from recommendations import top_llms_for_usecase

@app.route('/')
@app.route('/home')
def home():
    return jsonify({'message': 'WhichLLM coming soon...'})

@app.route('/usecases')
def get_all_usecases():
    usecases = db.session.query(Usecase).join(benchmark_usecase, Usecase.id == benchmark_usecase.c.usecase_id).distinct().all()
    json_usecases = [usecase.to_json() for usecase in usecases]
    return jsonify(json_usecases)

@app.route('/usecase/<int:usecase_id>', methods=['GET'])
def get_usecase(usecase_id):
    usecase = Usecase.query.get_or_404(usecase_id)
    json_usecase = usecase.to_json()
    return jsonify(json_usecase)

@app.route('/benchmarks-usecases')
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

# Recommendations route, displaying top LLMs with score in JSON format
@app.route('/recommendations', methods=['GET'])
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
    
@app.route('/llm-scores', methods=['GET'])
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

with app.app_context():
    get_benchmarks_usecases()