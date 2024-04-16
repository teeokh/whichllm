from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import LLM, Benchmark, Usecase, llm_benchmark, benchmark_usecase, LLMStatus
from config import db_path
from config import app, db

engine = create_engine(f'sqlite:///{db_path}')
Session = sessionmaker(bind=engine)
session = Session()

llm_data = [
    # {'name': 'ChatGPT', 'link': 'https://chat.openai.com/', 'status': 'free', 'provider': 'OpenAI'},
    # {'name': 'GPT-4', 'link': 'https://openai.com/gpt-4', 'status': 'paid', 'provider': 'OpenAI'},
    # {'name': 'GPT-4 with Vision', 'link': 'https://platform.openai.com/docs/guides/vision', 'status': 'paid', 'provider': 'OpenAI', 'notes': 'Through API access', 'speciality': 'Vision'},
    # {'name': 'Claude 3 Haiku', 'link': 'hhttps://claude.ai/', 'status': 'free', 'provider': 'Anthropic'},
    # {'name': 'Claude 3 Sonnet', 'link': 'https://claude.ai/', 'status': 'free', 'provider': 'Anthropic'},
    # {'name': 'Claude 3 Opus', 'link': 'https://claude.ai/', 'status': 'paid', 'provider': 'Anthropic'},
    # {'name': 'Gemini 1.0 Pro', 'link': 'https://gemini.google.com/app', 'status': 'free', 'provider': 'Google'},
    # {'name': 'Gemini Advanced', 'link': 'https://gemini.google.com/advanced', 'status': 'paid', 'provider': 'Google'},
    # {'name': 'Github CoPilot', 'link': 'https://github.com/features/copilot', 'status': 'paid', 'provider': 'Github', 'speciality': 'Coding'},
    # {'name': 'MedLM', 'link': 'https://cloud.google.com/vertex-ai/generative-ai/docs/medlm/overview', 'status': 'paid', 'provider': 'Google', 'notes': 'Only available in the US to Google Cloud users', 'speciality': 'Medicine'},
    # {'name': 'GPT4-Medprompt', 'link': 'https://openai.com/gpt-4', 'status': 'paid', 'provider': 'OpenAI', 'speciality': 'Medicine'},
    # {'name': 'InternLM2', 'link': 'https://github.com/InternLM/InternLM', 'status': 'free', 'provider': 'InternLM'},
    # {'name': 'InternLM-Math', 'link': 'https://github.com/InternLM/InternLM-Math', 'status': 'free', 'provider': 'InternLM', 'speciality': 'Maths'},
    # {'name': 'InternLM-XComposer2-4KHD', 'link': 'https://github.com/InternLM/InternLM-XComposer', 'status': 'free', 'provider': 'InternLM', 'speciality': 'Vision'},
    # {'name': 'LawGPT', 'link': 'https://github.com/LiuHC0428/LAW-GPT', 'status': 'free', 'provider': 'InternLM', 'speciality': 'Law'},
    # {'name': 'CogVLM', 'link': 'https://github.com/THUDM/CogVLM', 'status': 'free', 'provider': 'CogVLM', 'notes': 'Through API access', 'speciality': 'Vision'}
]

def populate_llm_table():
    for llm in llm_data:
        name = llm['name']
        link = llm['link']
        status_value = llm['status']
        provider = llm['provider']
        speciality = llm.get('speciality', None)
        notes = llm.get('notes', None)
        
        status = LLMStatus[status_value]
        
        new_llm = LLM(name=name, link=link, status=status, provider=provider, notes=notes, speciality=speciality)
        
        session.add(new_llm)
        
    session.commit()
    print('New LLM(s) added!')

# populate_llm_table()

def drop_llm_row(row_id):
    row = LLM.query.get(row_id)
    
    if row:
        db.session.delete(row)
        print('Row deleted')
    else:
        print('Row not deleted')
        
    db.session.commit()

# with app.app_context():
#     drop_llm_row(3)

benchmark_data = [
    # {'name': 'MMLU', 'subject': 'General'},
    # {'name': 'HellaSwag', 'subject': 'General', 'notes': 'Sentence completion'},
    # {'name': 'SuperGLUE', 'subject': 'General'},
    # {'name': 'WinoGrande', 'subject': 'General'},
    # {'name': 'ARC', 'subject': 'General'},
    # {'name': 'GPQA', 'subject': 'General'},
    # {'name': 'OpenBookQA', 'subject': 'General'},
    # {'name': 'BIG Bench Hard', 'subject': 'Advanced Reasoning'},
    # {'name': 'Chatbot Arena Elo', 'subject': 'Conversation', 'notes': 'User-based / Relative'},
    # {'name': 'MT-Bench', 'subject': 'Conversation'},
    # {'name': 'MATH', 'subject': 'Maths'},
    # {'name': 'GSM8K', 'subject': 'Maths'},
    # {'name': 'MGSM', 'subject': 'Maths'},
    # {'name': 'HumanEval', 'subject': 'Coding'},
    # {'name': 'MBPP', 'subject': 'Coding'},
    # {'name': 'USMLE', 'subject': 'Medicine'},
    # {'name': 'MedQA', 'subject': 'Medicine'},
    # {'name': 'LSAT', 'subject': 'Law'},
    # {'name': 'Bar Exam', 'subject': 'Law'},
    # {'name': 'Graduate Record Exam', 'subject': 'Law'},
    # {'name': 'DocVQA', 'subject': 'Image Understanding'},
    # {'name': 'MMMU', 'subject': 'Image Understanding'},
    # {'name': 'TextVQA', 'subject': 'Image Understanding'},
    # {'name': 'VATEX', 'subject': 'Video Understanding'},
    # {'name': 'CoVoST 2', 'subject': 'Speech Translation'},
    # {'name': 'FLEURS', 'subject': 'Speech Recognition'}
    # {'name': 'MAWPS', 'subject': 'Maths'}
    # {'name': 'PubMedQA', 'subject': 'Medicine'}
]

def populate_benchmark_table():
    for benchmark in benchmark_data:
        name = benchmark['name']
        subject = benchmark['subject']
        notes = benchmark.get('notes', None)
        
        new_benchmark = Benchmark(name=name, notes=notes, subject=subject)
        
        session.add(new_benchmark)
        
    session.commit()
    print('New Benchmark(s) added!')
    
# populate_benchmark_table()
    
    
def update_benchmark(benchmark_name, new_subject):
    benchmark = Benchmark.query.filter_by(name=benchmark_name).first()
    if benchmark:
        benchmark.subject = new_subject
        db.session.commit()
        print(f"Subject for benchmark '{benchmark_name}' updated to '{new_subject}'.")
    else:
        print(f"Benchmark '{benchmark_name}' not found.")
       
# with app.app_context():
#     update_benchmark('GPQA', 'Science')

def drop_benchmark_row(row_id):
    row = Benchmark.query.get(row_id)
    
    if row:
        db.session.delete(row)
        print('Row deleted')
    else:
        print('Row not deleted')
        
    db.session.commit()

# with app.app_context():
#     drop_benchmark_row(16)



usecase_data = [
    # {'name': 'Text generation'},
    # {'name': 'Text summation'},
    # {'name': 'General Knowledge'},
    # {'name': 'Conversation'},
    # {'name': 'Translation'},
    # {'name': 'Maths'},
    # {'name': 'Coding'},
    # {'name': 'Science'},
    # {'name': 'Medical knowledge'},
    # {'name': 'Law knowledge'},
    # {'name': 'Advanced reasoning'},
    # {'name': 'Reading documents'},
    # {'name': 'Image input'},
    # {'name': 'Video input'},
    # {'name': 'Audio input'}
]

def populate_usecase_table():
    for usecase in usecase_data:
        name = usecase['name']
        
        new_usecase = Usecase(name=name)
        
        session.add(new_usecase)
    
    session.commit()
    print('New Usecase(s) added!')
    
# populate_usecase_table()

llm_benchmark_data = [
    # {'llm_id': 1, 'benchmark_id': 1, 'score': 70.0},
    # {'llm_id': 1, 'benchmark_id': 2, 'score': 85.5},
    # {'llm_id': 1, 'benchmark_id': 3, 'score': 78.3},
    # {'llm_id': 1, 'benchmark_id': 4, 'score': 81.6},
    # {'llm_id': 1, 'benchmark_id': 5, 'score': 85.2},
    # {'llm_id': 1, 'benchmark_id': 8, 'score': 71.0},
    # {'llm_id': 1, 'benchmark_id': 12, 'score': 57.1},
    # {'llm_id': 1, 'benchmark_id': 14, 'score': 48.1},
    # {'llm_id': 1, 'benchmark_id': 15, 'score': 83.2},
    # {'llm_id': 1, 'benchmark_id': 17, 'score': 50.3},
    # {'llm_id': 1, 'benchmark_id': 27, 'score': 60.2},
    # {'llm_id': 1, 'benchmark_id': 18, 'score': 82.8},
    # {'llm_id': 1, 'benchmark_id': 19, 'score': 53.3},
    # {'llm_id': 1, 'benchmark_id': 11, 'score': 34.1},
    # {'llm_id': 1, 'benchmark_id': 20, 'score': 88.5},
    {'llm_id': 1, 'benchmark_id': 6, 'score': 28.1},
    {'llm_id': 2, 'benchmark_id': 1, 'score': 86.4},
    {'llm_id': 2, 'benchmark_id': 2, 'score': 95.3},
    {'llm_id': 2, 'benchmark_id': 3, 'score': 89.5},
    {'llm_id': 2, 'benchmark_id': 4, 'score': 87.5},
    {'llm_id': 2, 'benchmark_id': 5, 'score': 96.3},
    {'llm_id': 2, 'benchmark_id': 6, 'score': 46.5},
    {'llm_id': 2, 'benchmark_id': 7, 'score': 95.9},
    {'llm_id': 2, 'benchmark_id': 8, 'score': 83.9},
    {'llm_id': 2, 'benchmark_id': 11, 'score': 54.0},
    {'llm_id': 2, 'benchmark_id': 12, 'score': 96.0},
    {'llm_id': 2, 'benchmark_id': 13, 'score': 74.5},
    {'llm_id': 2, 'benchmark_id': 14, 'score': 67.0},
    {'llm_id': 2, 'benchmark_id': 15, 'score': 87.5},
    {'llm_id': 2, 'benchmark_id': 17, 'score': 90.2},
    {'llm_id': 2, 'benchmark_id': 18, 'score': 88.9},
    {'llm_id': 2, 'benchmark_id': 19, 'score': 74.5},
    {'llm_id': 2, 'benchmark_id': 20, 'score': 97.6},
    {'llm_id': 2, 'benchmark_id': 21, 'score': 88.4},
    {'llm_id': 2, 'benchmark_id': 22, 'score': 56.8},
    {'llm_id': 2, 'benchmark_id': 23, 'score': 78.0},
    {'llm_id': 2, 'benchmark_id': 24, 'score': 56.0},
    {'llm_id': 2, 'benchmark_id': 25, 'score': 29.1},
    {'llm_id': 2, 'benchmark_id': 26, 'score': 82.4},
    {'llm_id': 2, 'benchmark_id': 27, 'score': 74.4}
]

def populate_llm_benchmark_table():
    for row in llm_benchmark_data:
        llm_bench_row = llm_benchmark.insert().values(
        llm_id=row['llm_id'],
        benchmark_id=row['benchmark_id'],
        score=row['score']
    )
        session.execute(llm_bench_row)
    
    session.commit()
    print('New LLM-Benchmark association(s) added!')

populate_llm_benchmark_table()