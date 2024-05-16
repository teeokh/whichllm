from app import app, db
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
    return jsonify({'llms':json_test})

# Recommendations route, displaying top LLMs with score in JSON format
@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    recommendations = top_llms_for_usecase(usecase_id=6, status_filter='free', top_n=5)
    json_recommendations = [{'llm':llm.to_json(), 'score': round(score, 1)} for llm, score in recommendations]
    if json_recommendations == []:
        return "This usecase information is unavailable"
    return jsonify({'recommendations':json_recommendations})


