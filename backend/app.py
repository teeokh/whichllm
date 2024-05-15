from config import app, db, db_path
from models import *
from flask import request, jsonify 

@app.route('/')
@app.route('/home')
def home():
    return 'Hello, whichLLM coming soon... This is the home page'

@app.route('/LLMs', methods=['GET'])
def get_llms():
    llms = LLM.query.all()
    json_llms = list(map(lambda x: x.to_json(), llms))
    return jsonify({'llms':json_llms})


if __name__ == "__main__":
    with app.app_context():
        db.create_all() # Create all the models we have to find in our database - if we don't have the database created already

    app.run(debug=True)