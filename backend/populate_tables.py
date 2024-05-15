from models import *
from config import app, db, db_path


llm_data = [
    {'name': 'ChatGPT', 'link': 'https://chat.openai.com/', 'status': 'free', 'provider': 'OpenAI'},
    {'name': 'GPT-4', 'link': 'https://openai.com/gpt-4', 'status': 'paid', 'provider': 'OpenAI'},
    {'name': 'GPT-4 with Vision', 'link': 'https://platform.openai.com/docs/guides/vision', 'status': 'paid', 'provider': 'OpenAI', 'notes': 'Through API access', 'speciality': 'Vision'},
    {'name': 'Claude 3 Haiku', 'link': 'hhttps://claude.ai/', 'status': 'free', 'provider': 'Anthropic'},
    {'name': 'Claude 3 Sonnet', 'link': 'https://claude.ai/', 'status': 'free', 'provider': 'Anthropic'},
    {'name': 'Claude 3 Opus', 'link': 'https://claude.ai/', 'status': 'paid', 'provider': 'Anthropic'},
    {'name': 'Gemini 1.0 Pro', 'link': 'https://gemini.google.com/app', 'status': 'free', 'provider': 'Google'},
    {'name': 'Gemini Ultra', 'link': 'https://deepmind.google/technologies/gemini/ultra/', 'status': 'paid', 'provider': 'Google'},
    {'name': 'Github CoPilot', 'link': 'https://github.com/features/copilot', 'status': 'paid', 'provider': 'Github', 'speciality': 'Coding'},
    {'name': 'MedLM', 'link': 'https://cloud.google.com/vertex-ai/generative-ai/docs/medlm/overview', 'status': 'paid', 'provider': 'Google', 'notes': 'Only available in the US to Google Cloud users', 'speciality': 'Medicine'},
    {'name': 'GPT4-Medprompt', 'link': 'https://openai.com/gpt-4', 'status': 'paid', 'provider': 'OpenAI', 'speciality': 'Medicine'},
    {'name': 'InternLM2', 'link': 'https://github.com/InternLM/InternLM', 'status': 'free', 'provider': 'InternLM'},
    {'name': 'InternLM-Math', 'link': 'https://github.com/InternLM/InternLM-Math', 'status': 'free', 'provider': 'InternLM', 'speciality': 'Maths'},
    {'name': 'InternLM-XComposer2-4KHD', 'link': 'https://github.com/InternLM/InternLM-XComposer', 'status': 'free', 'provider': 'InternLM', 'speciality': 'Vision'},
    {'name': 'LawGPT', 'link': 'https://github.com/LiuHC0428/LAW-GPT', 'status': 'free', 'provider': 'InternLM', 'speciality': 'Law'},
    {'name': 'CogVLM', 'link': 'https://github.com/THUDM/CogVLM', 'status': 'free', 'provider': 'CogVLM', 'notes': 'Through API access', 'speciality': 'Vision'},
    {'name': 'Gemini 1.5 Pro', 'link': 'https://gemini.google.com/app', 'status': 'free', 'provider': 'Google'},
    {'name': 'Llama 2', 'link': 'https://llama.meta.com/', 'status': 'free', 'provider': 'Meta'},
    {'name': 'Code Llama', 'link': 'https://llama.meta.com/', 'status': 'free', 'provider': 'Meta', 'speciality': 'Coding'},
    {'name': 'Mistral 7B', 'link': 'https://mistral.ai/', 'status': 'free', 'provider': 'Mitral AI'},
    {'name': 'Midnight Miqu', 'link': 'https://huggingface.co/sophosympatheia/Midnight-Miqu-70B-v1.5', 'status': 'free', 'provider': 'Sophosympatheia', 'speciality': 'Writing'}
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
        
        db.session.add(new_llm)
        
    db.session.commit()
    print('New LLM(s) added!')

# with app.app_context():
#     populate_llm_table()

def drop_llm_row(row_id):
    row = LLM.query.get(row_id)
    
    if row:
        db.session.delete(row)
        print('Row deleted')
    else:
        print('Row not deleted')
        
    db.session.commit()

# with app.app_context():
#     drop_llm_row()


def update_cell(row_id, column_name, new_value):
    # Retrieve the specific row from the table
    row = LLM.query.get(row_id)

    if row:
        # Update the value of the cell in that row
        setattr(row, column_name, new_value)

        # Commit the changes to the database session
        db.session.commit()
        print(f"Cell in row {row_id} updated successfully.")
    else:
        print(f"Row with ID {row_id} not found.")

# with app.app_context():
#     update_cell(8, 'name', 'Gemini Ultra')

benchmark_data = [
    {'name': 'MMLU', 'subject': 'General'},
    {'name': 'HellaSwag', 'subject': 'General', 'notes': 'Sentence completion'},
    {'name': 'SuperGLUE', 'subject': 'General'},
    {'name': 'WinoGrande', 'subject': 'General'},
    {'name': 'ARC', 'subject': 'General'},
    {'name': 'GPQA', 'subject': 'General'},
    {'name': 'OpenBookQA', 'subject': 'General'},
    {'name': 'BIG Bench Hard', 'subject': 'Advanced Reasoning'},
    {'name': 'Chatbot Arena Elo', 'subject': 'Relative Performance', 'notes': 'User-based / Relative'},
    {'name': 'MT-Bench', 'subject': 'Conversation'},
    {'name': 'MATH', 'subject': 'Maths'},
    {'name': 'GSM8K', 'subject': 'Maths'},
    {'name': 'MGSM', 'subject': 'Maths'},
    {'name': 'HumanEval', 'subject': 'Coding'},
    {'name': 'MBPP', 'subject': 'Coding'},
    {'name': 'USMLE', 'subject': 'Medicine'},
    {'name': 'MedQA', 'subject': 'Medicine'},
    {'name': 'LSAT', 'subject': 'Law'},
    {'name': 'Bar Exam', 'subject': 'Law'},
    {'name': 'Graduate Record Exam', 'subject': 'Law'},
    {'name': 'DocVQA', 'subject': 'Image Understanding'},
    {'name': 'MMMU', 'subject': 'Image Understanding'},
    {'name': 'TextVQA', 'subject': 'Image Understanding'},
    {'name': 'VATEX', 'subject': 'Video Understanding'},
    {'name': 'CoVoST 2', 'subject': 'Speech Translation'},
    {'name': 'FLEURS', 'subject': 'Speech Recognition'},
    {'name': 'MAWPS', 'subject': 'Maths'},
    {'name': 'PubMedQA', 'subject': 'Medicine'},
    {'name': 'ChartQA', 'subject': 'Image Understanding', 'notes': 'Chart understanding'},
    {'name': 'AI2D', 'subject': 'Image Understanding', 'notes': 'Science diagram understanding'},
    {'name': 'MMLU Medicine', 'subject': 'Medicine', 'notes': 'Average score'},
    {'name': 'MedMCQA', 'subject': 'Medicine'},
    {'name' : 'EQ Bench', 'subject': 'Emotional intelligence / creativity'}
]

def populate_benchmark_table():
    for benchmark in benchmark_data:
        name = benchmark['name']
        subject = benchmark['subject']
        notes = benchmark.get('notes', None)
        
        new_benchmark = Benchmark(name=name, notes=notes, subject=subject)
        
        db.session.add(new_benchmark)
        
    db.session.commit()
    print('New Benchmark(s) added!')
    
# with app.app_context():
#     populate_benchmark_table()
    
    
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
#     drop_benchmark_row()



usecase_data = [
    {'name': 'Text generation'},
    {'name': 'Text summation'},
    {'name': 'General Knowledge'},
    {'name': 'Conversation'},
    {'name': 'Translation'},
    {'name': 'Maths'},
    {'name': 'Coding'},
    {'name': 'Science'},
    {'name': 'Medical knowledge'},
    {'name': 'Law knowledge'},
    {'name': 'Advanced reasoning'},
    {'name': 'Reading documents'},
    {'name': 'Image input'},
    {'name': 'Video input'},
    {'name': 'Audio input'},
    {'name': 'Basic reasoning'},
    {'name': 'Creative writing'},
    {'name': 'Relative User Preference'}
]

def populate_usecase_table():
    for usecase in usecase_data:
        name = usecase['name']
        
        new_usecase = Usecase(name=name)
        
        db.session.add(new_usecase)
    
    db.session.commit()
    print('New Usecase(s) added!')

# with app.app_context():
#     populate_usecase_table()


def update_usecase(usecase_name, new_name):
    usecase = Usecase.query.filter_by(name=usecase_name).first()
    if usecase:
        usecase.name = new_name
        db.session.commit()
        print(f"Usecase '{usecase_name}' updated to '{new_name}'.")
    else:
        print(f"Usecase '{usecase_name}' not found.")
        

llm_benchmark_data = [
    {'llm_id': 1, 'benchmark_id': 1, 'score': 70.0},
    {'llm_id': 1, 'benchmark_id': 2, 'score': 85.5},
    {'llm_id': 1, 'benchmark_id': 3, 'score': 78.3},
    {'llm_id': 1, 'benchmark_id': 4, 'score': 81.6},
    {'llm_id': 1, 'benchmark_id': 5, 'score': 85.2},
    {'llm_id': 1, 'benchmark_id': 8, 'score': 71.0},
    {'llm_id': 1, 'benchmark_id': 12, 'score': 57.1},
    {'llm_id': 1, 'benchmark_id': 14, 'score': 48.1},
    {'llm_id': 1, 'benchmark_id': 15, 'score': 83.2},
    {'llm_id': 1, 'benchmark_id': 17, 'score': 50.3},
    {'llm_id': 1, 'benchmark_id': 28, 'score': 60.2},
    {'llm_id': 1, 'benchmark_id': 18, 'score': 82.8},
    {'llm_id': 1, 'benchmark_id': 19, 'score': 53.3},
    {'llm_id': 1, 'benchmark_id': 11, 'score': 34.1},
    {'llm_id': 1, 'benchmark_id': 20, 'score': 88.5},
    {'llm_id': 1, 'benchmark_id': 6, 'score': 28.1},
    {'llm_id': 1, 'benchmark_id': 9, 'score': 1119},
    {'llm_id': 1, 'benchmark_id': 33, 'score': 70.67},
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
    {'llm_id': 2, 'benchmark_id': 14, 'score': 76.5},
    {'llm_id': 2, 'benchmark_id': 15, 'score': 87.5},
    {'llm_id': 2, 'benchmark_id': 17, 'score': 81.4},
    {'llm_id': 2, 'benchmark_id': 18, 'score': 88.9},
    {'llm_id': 2, 'benchmark_id': 19, 'score': 74.5},
    {'llm_id': 2, 'benchmark_id': 20, 'score': 97.6},
    {'llm_id': 2, 'benchmark_id': 21, 'score': 88.4},
    {'llm_id': 2, 'benchmark_id': 22, 'score': 56.8},
    {'llm_id': 2, 'benchmark_id': 23, 'score': 78.0},
    {'llm_id': 2, 'benchmark_id': 24, 'score': 56.0},
    {'llm_id': 2, 'benchmark_id': 25, 'score': 29.1},
    {'llm_id': 2, 'benchmark_id': 26, 'score': 82.4},
    {'llm_id': 2, 'benchmark_id': 28, 'score': 74.4},
    {'llm_id': 2, 'benchmark_id': 29, 'score': 78.5},
    {'llm_id': 2, 'benchmark_id': 30, 'score': 78.2},
    {'llm_id': 2, 'benchmark_id': 31, 'score': 87.4},
    {'llm_id': 2, 'benchmark_id': 32, 'score': 72.4},
    {'llm_id': 2, 'benchmark_id': 9, 'score': 1260},
    {'llm_id': 2, 'benchmark_id': 33, 'score': 86.35},
    {'llm_id': 4, 'benchmark_id': 1, 'score': 75.2},
    {'llm_id': 4, 'benchmark_id': 2, 'score': 85.9},
    {'llm_id': 4, 'benchmark_id': 4, 'score': 74.2},
    {'llm_id': 4, 'benchmark_id': 5, 'score': 89.2},
    {'llm_id': 4, 'benchmark_id': 6, 'score': 33.3},
    {'llm_id': 4, 'benchmark_id': 8, 'score': 73.7},
    {'llm_id': 4, 'benchmark_id': 11, 'score': 40.9},
    {'llm_id': 4, 'benchmark_id': 12, 'score': 88.9},
    {'llm_id': 4, 'benchmark_id': 13, 'score': 75.1},
    {'llm_id': 4, 'benchmark_id': 14, 'score': 75.9},
    {'llm_id': 4, 'benchmark_id': 15, 'score': 80.4},
    {'llm_id': 4, 'benchmark_id': 28, 'score': 76.0},
    {'llm_id': 4, 'benchmark_id': 18, 'score': 86.8},
    {'llm_id': 4, 'benchmark_id': 19, 'score': 64.0},
    {'llm_id': 4, 'benchmark_id': 21, 'score': 88.8},
    {'llm_id': 4, 'benchmark_id': 22, 'score': 50.2},
    {'llm_id': 4, 'benchmark_id': 29, 'score': 50.2},
    {'llm_id': 4, 'benchmark_id': 30, 'score': 86.7},
    {'llm_id': 4, 'benchmark_id': 9, 'score': 1182},
    {'llm_id': 4, 'benchmark_id': 33, 'score': 63.65},
    {'llm_id': 5, 'benchmark_id': 1, 'score': 79.0},
    {'llm_id': 5, 'benchmark_id': 2, 'score': 89.0},
    {'llm_id': 5, 'benchmark_id': 4, 'score': 75.1},
    {'llm_id': 5, 'benchmark_id': 5, 'score': 93.2},
    {'llm_id': 5, 'benchmark_id': 6, 'score': 40.4},
    {'llm_id': 5, 'benchmark_id': 8, 'score': 82.9},
    {'llm_id': 5, 'benchmark_id': 11, 'score': 40.5},
    {'llm_id': 5, 'benchmark_id': 12, 'score': 92.3},
    {'llm_id': 5, 'benchmark_id': 13, 'score': 83.5},
    {'llm_id': 5, 'benchmark_id': 14, 'score': 73.0},
    {'llm_id': 5, 'benchmark_id': 15, 'score': 79.4},
    {'llm_id': 5, 'benchmark_id': 28, 'score': 78.3},
    {'llm_id': 5, 'benchmark_id': 18, 'score': 87.9},
    {'llm_id': 5, 'benchmark_id': 19, 'score': 71.0},
    {'llm_id': 5, 'benchmark_id': 21, 'score': 89.5},
    {'llm_id': 5, 'benchmark_id': 22, 'score': 53.1},
    {'llm_id': 5, 'benchmark_id': 29, 'score': 81.1},
    {'llm_id': 5, 'benchmark_id': 30, 'score': 88.7},
    {'llm_id': 5, 'benchmark_id': 9, 'score': 1203},
    {'llm_id': 5, 'benchmark_id': 33, 'score': 80.45},
    {'llm_id': 6, 'benchmark_id': 1, 'score': 86.8},
    {'llm_id': 6, 'benchmark_id': 2, 'score': 95.4},
    {'llm_id': 6, 'benchmark_id': 4, 'score': 88.5},
    {'llm_id': 6, 'benchmark_id': 5, 'score': 96.4},
    {'llm_id': 6, 'benchmark_id': 6, 'score': 50.4},
    {'llm_id': 6, 'benchmark_id': 8, 'score': 86.8},
    {'llm_id': 6, 'benchmark_id': 11, 'score': 61.0},
    {'llm_id': 6, 'benchmark_id': 12, 'score': 95.0},
    {'llm_id': 6, 'benchmark_id': 13, 'score': 90.7},
    {'llm_id': 6, 'benchmark_id': 14, 'score': 84.9},
    {'llm_id': 6, 'benchmark_id': 15, 'score': 86.4},
    {'llm_id': 6, 'benchmark_id': 18, 'score': 89.4},
    {'llm_id': 6, 'benchmark_id': 19, 'score': 85.0},
    {'llm_id': 6, 'benchmark_id': 20, 'score': 95.6},
    {'llm_id': 6, 'benchmark_id': 21, 'score': 89.3},
    {'llm_id': 6, 'benchmark_id': 22, 'score': 59.4},
    {'llm_id': 6, 'benchmark_id': 23, 'score': 86.8},
    {'llm_id': 6, 'benchmark_id': 28, 'score': 75.8},
    {'llm_id': 6, 'benchmark_id': 29, 'score': 80.8},
    {'llm_id': 6, 'benchmark_id': 30, 'score': 88.1},
    {'llm_id': 6, 'benchmark_id': 9, 'score': 1255},
    {'llm_id': 6, 'benchmark_id': 33, 'score': 82.19},
    {'llm_id': 17, 'benchmark_id': 1, 'score': 81.9},
    {'llm_id': 17, 'benchmark_id': 2, 'score': 92.5},
    {'llm_id': 17, 'benchmark_id': 8, 'score': 84.0},
    {'llm_id': 17, 'benchmark_id': 11, 'score': 58.5},
    {'llm_id': 17, 'benchmark_id': 12, 'score': 91.7},
    {'llm_id': 17, 'benchmark_id': 13, 'score': 88.7},
    {'llm_id': 17, 'benchmark_id': 14, 'score': 71.9},
    {'llm_id': 17, 'benchmark_id': 21, 'score': 86.5},
    {'llm_id': 17, 'benchmark_id': 22, 'score': 58.5},
    {'llm_id': 17, 'benchmark_id': 29, 'score': 81.3},
    {'llm_id': 17, 'benchmark_id': 30, 'score': 80.3},
    {'llm_id': 17, 'benchmark_id': 9, 'score': 1209},
    {'llm_id': 8, 'benchmark_id': 1, 'score': 90.0},
    {'llm_id': 8, 'benchmark_id': 2, 'score': 87.8},
    {'llm_id': 8, 'benchmark_id': 8, 'score': 83.6},
    {'llm_id': 8, 'benchmark_id': 11, 'score': 53.2},
    {'llm_id': 8, 'benchmark_id': 12, 'score': 94.4},
    {'llm_id': 8, 'benchmark_id': 13, 'score': 79.0},
    {'llm_id': 8, 'benchmark_id': 14, 'score': 74.4},
    {'llm_id': 8, 'benchmark_id': 21, 'score': 90.9},
    {'llm_id': 8, 'benchmark_id': 22, 'score': 59.4},
    {'llm_id': 8, 'benchmark_id': 23, 'score': 82.3},
    {'llm_id': 8, 'benchmark_id': 24, 'score': 62.7},
    {'llm_id': 8, 'benchmark_id': 25, 'score': 40.1},
    {'llm_id': 8, 'benchmark_id': 26, 'score': 92.4},
    {'llm_id': 8, 'benchmark_id': 29, 'score': 80.8},
    {'llm_id': 8, 'benchmark_id': 30, 'score': 79.5},
    {'llm_id': 8, 'benchmark_id': 33, 'score': 77.68},
    {'llm_id': 10, 'benchmark_id': 17, 'score': 86.5},
    {'llm_id': 10, 'benchmark_id': 28, 'score': 81.8},
    {'llm_id': 10, 'benchmark_id': 31, 'score': 89.9},
    {'llm_id': 10, 'benchmark_id': 32, 'score': 72.3},
    {'llm_id': 16, 'benchmark_id': 21, 'score': 81.6},
    {'llm_id': 16, 'benchmark_id': 23, 'score': 76.1},
    {'llm_id': 16, 'benchmark_id': 29, 'score': 68.4},
    {'llm_id': 18, 'benchmark_id': 1, 'score': 82.0},
    {'llm_id': 18, 'benchmark_id': 4, 'score': 83.1},
    {'llm_id': 18, 'benchmark_id': 5, 'score': 93.0},
    {'llm_id': 18, 'benchmark_id': 6, 'score': 39.5},
    {'llm_id': 18, 'benchmark_id': 8, 'score': 81.3},
    {'llm_id': 18, 'benchmark_id': 12, 'score': 93.0},
    {'llm_id': 18, 'benchmark_id': 14, 'score': 81.7},
    {'llm_id': 18, 'benchmark_id': 11, 'score': 50.4},
    {'llm_id': 18, 'benchmark_id': 9, 'score': 1213},
    {'llm_id': 19, 'benchmark_id': 14, 'score': 53.0},
    {'llm_id': 19, 'benchmark_id': 15, 'score': 62.4},
    {'llm_id': 20, 'benchmark_id': 1, 'score': 62.5},
    {'llm_id': 20, 'benchmark_id': 2, 'score': 81.3},
    {'llm_id': 20, 'benchmark_id': 4, 'score': 75.3},
    {'llm_id': 20, 'benchmark_id': 5, 'score': 78.7},
    {'llm_id': 20, 'benchmark_id': 6, 'score': 26.3},
    {'llm_id': 20, 'benchmark_id': 8, 'score': 56.0},
    {'llm_id': 20, 'benchmark_id': 12, 'score': 39.9},
    {'llm_id': 20, 'benchmark_id': 11, 'score': 13.1},
    {'llm_id': 20, 'benchmark_id': 14, 'score': 30.5},
    {'llm_id': 20, 'benchmark_id': 15, 'score': 47.5},
    {'llm_id': 20, 'benchmark_id': 9, 'score': 1158},
    {'llm_id': 20, 'benchmark_id': 33, 'score': 68.18},
    {'llm_id': 21, 'benchmark_id': 33, 'score': 75.9}
]

def populate_llm_benchmark_table():
    for row in llm_benchmark_data:
        llm_bench_row = llm_benchmark.insert().values(
        llm_id=row['llm_id'],
        benchmark_id=row['benchmark_id'],
        score=row['score']
    )
        db.session.execute(llm_bench_row)
    
    db.session.commit()
    print('New LLM-Benchmark association(s) added!')

# with app.app_context():
#     populate_llm_benchmark_table()



def delete_llm_benchmark(llm_id):
    llm_benchmark_row = llm_benchmark.delete().where(
        llm_benchmark.c.llm_id == llm_id
    )
    
    db.session.execute(llm_benchmark_row)
    db.session.commit()
    print(f"Rows for LLM ID {llm_id} deleted.")

# delete_llm_benchmark()


benchmark_usecase_data = [
    {'benchmark_id': 1, 'usecase_id': 3},
    {'benchmark_id': 2, 'usecase_id': 16},
    {'benchmark_id': 4, 'usecase_id': 16},
    {'benchmark_id': 5, 'usecase_id': 16},
    {'benchmark_id': 6, 'usecase_id': 8},
    {'benchmark_id': 30, 'usecase_id': 8},
    {'benchmark_id': 7, 'usecase_id': 16},
    {'benchmark_id': 8, 'usecase_id': 11},
    {'benchmark_id': 12, 'usecase_id': 6},
    {'benchmark_id': 13, 'usecase_id': 6},
    {'benchmark_id': 11, 'usecase_id': 6},
    {'benchmark_id': 14, 'usecase_id': 7},
    {'benchmark_id': 15, 'usecase_id': 7},
    {'benchmark_id': 17, 'usecase_id': 9},
    {'benchmark_id': 28, 'usecase_id': 9},
    {'benchmark_id': 18, 'usecase_id': 10},
    {'benchmark_id': 19, 'usecase_id': 10},
    {'benchmark_id': 20, 'usecase_id': 10},
    {'benchmark_id': 21, 'usecase_id': 12},
    {'benchmark_id': 21, 'usecase_id': 13},
    {'benchmark_id': 22, 'usecase_id': 13},
    {'benchmark_id': 23, 'usecase_id': 13},
    {'benchmark_id': 24, 'usecase_id': 14},
    {'benchmark_id': 25, 'usecase_id': 15},
    {'benchmark_id': 26, 'usecase_id': 15},
    {'benchmark_id': 28, 'usecase_id': 10},
    {'benchmark_id': 29, 'usecase_id': 12},
    {'benchmark_id': 30, 'usecase_id': 12},
    {'benchmark_id': 31, 'usecase_id': 9},
    {'benchmark_id': 32, 'usecase_id': 9},
    {'benchmark_id': 2, 'usecase_id': 1},
    {'benchmark_id': 33, 'usecase_id': 17},
    {'benchmark_id': 9, 'usecase_id': 18}
]


def populate_benchmark_usecase_table():
    for row in benchmark_usecase_data:
        benchmark_usecase_row = benchmark_usecase.insert().values(
        benchmark_id=row['benchmark_id'],
        usecase_id=row['usecase_id']
    )
        db.session.execute(benchmark_usecase_row)
    
    db.session.commit()
    print('New Benchmark-Usecase association(s) added!')
    
# with app.app_context():
#     populate_benchmark_usecase_table()
