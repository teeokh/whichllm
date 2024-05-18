from config import app, db
from models import *
from flask import request, jsonify 
from recommendations import top_llms_for_usecase

@app.route('/')
@app.route('/home')
def home():
    return 'Hello, whichLLM coming soon... This is the home page'

@app.route('/test', methods=['GET'])
def get_test():
    test = Benchmark.query.all()
    json_test = list(map(lambda x: x.to_json(), test))
    return jsonify(json_test)

# Recommendations route, displaying top LLMs with score in JSON format
@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    
    # Set query parameters for URL routing -> can dynamically change recommendation parameters
    usecase_id = request.args.get('usecase_id', type=int)
    status_filter = request.args.get('status_filter', default=None)
    top_n = request.args.get('top_n', default=3, type=int)
    
    # If usecase ID is not entered
    if usecase_id is None:
        return jsonify({'error': 'usecase_id is required'}), 400
    
    # If usecase ID is not recognised
    usecase = Usecase.query.filter_by(id=usecase_id).first()
    if not usecase:
        return jsonify({'error': f'Usecase with id {usecase_id} not found'}), 404
    
    recommendations = top_llms_for_usecase(usecase_id=usecase_id, status_filter=status_filter, top_n=top_n)
    json_recommendations = [{'llm':llm.to_json(), 'score': round(score, 1)} for llm, score in recommendations]
    
    # If no recommendations found / no benchmarks for that usecase
    if not json_recommendations:
        return jsonify({'message': 'No recommendations found for this usecase'}), 404
    
    return jsonify({'recommendations':json_recommendations})


