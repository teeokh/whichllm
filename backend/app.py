from config import app, db, db_path
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

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    recommendations = top_llms_for_usecase(usecase_id=3, status_filter='free', top_n=4)
    json_recommendations = [llm.to_json() for llm, score in recommendations]
    return jsonify({'recommendations':json_recommendations})


if __name__ == "__main__":
    with app.app_context():
        db.create_all() # Create all the models we have to find in our database - if we don't have the database created already

    app.run(debug=True)