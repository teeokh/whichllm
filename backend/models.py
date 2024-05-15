from config import app, db, db_path
import enum
from sqlalchemy import Enum

class LLMStatus(enum.Enum):
    free = 'free'
    paid = 'paid'

class LLM(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    link = db.Column(db.String(225), unique=False, nullable=True) # In case unable to find link
    status = db.Column(db.Enum(LLMStatus), unique=False)
    provider = db.Column(db.String(120), unique=False, nullable=True)
    speciality = db.Column(db.String(120), nullable=True)
    notes = db.Column(db.String(220), nullable=True)
    benchmarks = db.relationship('Benchmark', secondary='llm_benchmark', backref='llms')
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'link': self.link,
            'status': self.status,
            'provider': self.provider,
            'speciality': self.speciality,
            'notes': self.notes,
            'benchmarks': [benchmark.id for benchmark in self.benchmarks]
        }
    
    def __repr__(self):
            return f'<LLM {self.id}: {self.name} ({self.status.value}) - {self.provider}. {self.notes}>'


class Benchmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    subject = db.Column(db.String(120), nullable=False)
    use_cases = db.relationship('Usecase', secondary='benchmark_usecase', backref='benchmarks')
    notes = db.Column(db.String(220), nullable=True)
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'subject': self.subject,
            'useCases': [usecase.id for usecase in self.use_cases],
            'notes': self.notes
        }
    
    def __repr__(self):
            return f'<Benchmark {self.id}: {self.name} ({self.subject}). {self.notes}>' # String representation when printing an ID - for debugging / visualisation


class Usecase(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }
    
    def __repr__(self):
        return f'<Usecase {self.id}: {self.name}>'

llm_benchmark = db.Table('llm_benchmark',
	db.Column('llm_id', db.Integer, db.ForeignKey('llm.id'), primary_key=True),
	db.Column('benchmark_id', db.Integer, db.ForeignKey('benchmark.id'), primary_key=True), # Primary key needed?
	db.Column('score', db.Float)
)

# Retrieving scores of LLMs in benchmarks in python interpreter:

# benchmark = session.query(Benchmark).filter_by(name='Elo (relative score)').first()
# for result in benchmark.benchmark_results:
#    llm = result.llm
#    score = result.score
#    print(f"LLM: {llm.name}, Score: {score}")

benchmark_usecase = db.Table('benchmark_usecase',
	db.Column('benchmark_id', db.Integer, db.ForeignKey('benchmark.id'), primary_key=True),
	db.Column('usecase_id', db.Integer, db.ForeignKey('usecase.id'), primary_key=True)
)