import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__,
            static_url_path='',
            static_folder='../frontend/build',
            template_folder='../frontend/build'
) # For initialising app 

CORS(app, resources={r'/*':{'origins':'*'}}) # Stops CORS errors - allows interaction between front and backend

project_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(project_dir, 'data', 'whichllm.db')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
