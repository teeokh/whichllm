from models import *
from config import app, db, db_path

# TODO think about adding provider logos to display in recommendation
# TODO Perplexity for all wildcard / internet search (no benchmarks, more obscure). For this to work, have to create fake benchmarks. Can make these a clickable link, which pop up a modal saying 'Personal preference / known fact'
# TODO Perplexity usecase link?

llm_data = [
    # {'name': 'ChatGPT', 'link': 'https://chat.openai.com/', 'status': 'free', 'provider': 'OpenAI'},
    # {'name': 'GPT-4', 'link': 'https://openai.com/gpt-4', 'status': 'paid', 'provider': 'OpenAI'},
    # {'name': 'GPT-4o', 'link': 'https://openai.com/index/hello-gpt-4o/', 'status': 'free', 'provider': 'OpenAI'},
    # {'name': 'GPT-4 with Vision', 'link': 'https://platform.openai.com/docs/guides/vision', 'status': 'paid', 'provider': 'OpenAI', 'notes': 'Through API access', 'speciality': 'Vision'},
    # {'name': 'Claude 3 Haiku', 'link': 'hhttps://claude.ai/', 'status': 'free', 'provider': 'Anthropic'},
    # {'name': 'Claude 3 Sonnet', 'link': 'https://claude.ai/', 'status': 'free', 'provider': 'Anthropic'},
    # {'name': 'Claude 3 Opus', 'link': 'https://claude.ai/', 'status': 'paid', 'provider': 'Anthropic'},
    # {'name': 'Gemini 1.0 Pro', 'link': 'https://gemini.google.com/app', 'status': 'free', 'provider': 'Google'},
    # {'name': 'Gemini Ultra', 'link': 'https://deepmind.google/technologies/gemini/ultra/', 'status': 'paid', 'provider': 'Google'},
    # {'name': 'Github CoPilot', 'link': 'https://github.com/features/copilot', 'status': 'paid', 'provider': 'Github', 'speciality': 'Coding'},
    # {'name': 'MedLM', 'link': 'https://cloud.google.com/vertex-ai/generative-ai/docs/medlm/overview', 'status': 'paid', 'provider': 'Google', 'notes': 'Only available in the US to Google Cloud users', 'speciality': 'Medicine'},
    # {'name': 'GPT4-Medprompt', 'link': 'https://openai.com/gpt-4', 'status': 'paid', 'provider': 'OpenAI', 'speciality': 'Medicine'},
    # {'name': 'InternLM2', 'link': 'https://github.com/InternLM/InternLM', 'status': 'free', 'provider': 'InternLM'},
    # {'name': 'InternLM-Math', 'link': 'https://github.com/InternLM/InternLM-Math', 'status': 'free', 'provider': 'InternLM', 'speciality': 'Maths'},
    # {'name': 'InternLM-XComposer2-4KHD', 'link': 'https://github.com/InternLM/InternLM-XComposer', 'status': 'free', 'provider': 'InternLM', 'speciality': 'Vision'},
    # {'name': 'LawGPT', 'link': 'https://github.com/LiuHC0428/LAW-GPT', 'status': 'free', 'provider': 'InternLM', 'speciality': 'Law'},
    # {'name': 'CogVLM', 'link': 'https://github.com/THUDM/CogVLM', 'status': 'free', 'provider': 'CogVLM', 'notes': 'Through API access', 'speciality': 'Vision'},
    # {'name': 'Gemini 1.5 Pro', 'link': 'https://gemini.google.com/app', 'status': 'free', 'provider': 'Google'},
    # {'name': 'Llama 2', 'link': 'https://llama.meta.com/', 'status': 'free', 'provider': 'Meta'},
    # {'name': 'Code Llama', 'link': 'https://llama.meta.com/', 'status': 'free', 'provider': 'Meta', 'speciality': 'Coding'},
    # {'name': 'Mistral 7B', 'link': 'https://mistral.ai/', 'status': 'free', 'provider': 'Mitral AI'},
    # {'name': 'Midnight Miqu', 'link': 'https://huggingface.co/sophosympatheia/Midnight-Miqu-70B-v1.5', 'status': 'free', 'provider': 'Sophosympatheia', 'speciality': 'Writing'}
    # {'name': 'Mixtral', 'link': 'https://mistral.ai/news/mixtral-of-experts/', 'status': 'free', 'provider': 'Mistral AI'},
    # {'name': 'Llama 3', 'link': 'https://www.meta.ai/', 'status': 'free', 'provider': 'Meta'},
    # {'name': 'Perplexity', 'link': 'https://www.perplexity.ai/', 'status': 'free', 'provider': 'Perplexity AI', 'specialty': ['Internet Search', 'Wildcard'], 'notes', 'Perplexity uses a combination of language models (such as GPT-4o and Claude Opus) to leverage the internet, summarizing live information and citing sources.'}
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
#     update_cell(25, 'notes', 'Perplexity uses a combination of language models (such as GPT-4o and Claude Opus) to leverage the internet, summarizing live information and citing sources.')

benchmark_data = [
    # {'name': 'MMLU', 'subject': 'General', 'link': 'https://crfm.stanford.edu/helm/mmlu/latest/'},
    # {'name': 'HellaSwag', 'subject': 'General', 'notes': 'Sentence completion', 'link': 'https://rowanzellers.com/hellaswag/'},
    # {'name': 'SuperGLUE', 'subject': 'General', 'link': 'https://super.gluebenchmark.com/'},
    # {'name': 'WinoGrande', 'subject': 'General', 'link': 'https://winogrande.allenai.org/'},
    # {'name': 'ARC', 'subject': 'General', 'link': 'https://leaderboard.allenai.org/arc/submissions/public'},
    # {'name': 'GPQA', 'subject': 'General', 'link': 'https://arxiv.org/abs/2311.12022'},
    # {'name': 'OpenBookQA', 'subject': 'General', 'link': 'https://allenai.org/data/open-book-qa'},
    # {'name': 'BIG Bench Hard', 'subject': 'Advanced Reasoning', 'link': 'https://github.com/suzgunmirac/BIG-Bench-Hard'},
    # {'name': 'Chatbot Arena Elo', 'subject': 'Relative Performance', 'notes': 'User-based / Relative', 'link': 'https://leaderboard.lmsys.org/'},
    # {'name': 'MT-Bench', 'subject': 'Conversation', 'link': 'https://huggingface.co/spaces/lmsys/mt-bench'},
    # {'name': 'MATH', 'subject': 'Maths', 'link': 'https://arxiv.org/pdf/2103.03874v2'},
    # {'name': 'GSM8K', 'subject': 'Maths', 'link': 'https://github.com/openai/grade-school-math'},
    # {'name': 'MGSM', 'subject': 'Maths', 'link': 'https://openreview.net/forum?id=fR3wGCk-IXp'},
    # {'name': 'HumanEval', 'subject': 'Coding', 'link': 'https://arxiv.org/abs/2107.03374'},
    # {'name': 'MBPP', 'subject': 'Coding', 'link': 'https://arxiv.org/pdf/2108.07732'},
    # {'name': 'USMLE', 'subject': 'Medicine', 'link': ''},
    # {'name': 'MedQA', 'subject': 'Medicine', 'link': 'https://paperswithcode.com/dataset/medqa-usmle'},
    # {'name': 'LSAT', 'subject': 'Law', 'link': 'https://www.lsac.org/lsat'},
    # {'name': 'Bar Exam', 'subject': 'Law', 'link': ''},
    # {'name': 'Graduate Record Exam', 'subject': 'Law', 'link': 'https://www.ets.org/gre.html'},
    # {'name': 'DocVQA', 'subject': 'Image Understanding', 'link': 'https://www.docvqa.org/'},
    # {'name': 'MMMU', 'subject': 'Image Understanding', 'link': 'https://mmmu-benchmark.github.io/'},
    # {'name': 'TextVQA', 'subject': 'Image Understanding', 'link': 'https://textvqa.org/'},
    # {'name': 'VATEX', 'subject': 'Video Understanding', 'link': 'https://eric-xw.github.io/vatex-website/about.html'},
    # {'name': 'CoVoST 2', 'subject': 'Speech Translation', 'link': 'https://arxiv.org/pdf/2007.10310'},
    # {'name': 'FLEURS', 'subject': 'Speech Recognition', 'link': 'https://arxiv.org/abs/2205.12446'},
    # {'name': 'MAWPS', 'subject': 'Maths', 'link': 'https://aclanthology.org/N16-1136.pdf'},
    # {'name': 'PubMedQA', 'subject': 'Medicine', 'link': 'https://pubmedqa.github.io/'},
    # {'name': 'ChartQA', 'subject': 'Image Understanding', 'notes': 'Chart understanding', 'link': 'https://arxiv.org/abs/2203.10244'},
    # {'name': 'AI2D', 'subject': 'Image Understanding', 'notes': 'Science diagram understanding', 'link': 'https://prior.allenai.org/projects/diagram-understanding'},
    # {'name': 'MMLU Medicine', 'subject': 'Medicine', 'notes': 'Average score', 'link': 'https://crfm.stanford.edu/helm/mmlu/latest/'},
    # {'name': 'MedMCQA', 'subject': 'Medicine', 'link': 'https://medmcqa.github.io/'},
    # {'name' : 'EQ Bench', 'subject': 'Emotional intelligence / creativity', 'link': 'https://eqbench.com/'}
    # {'name' : 'Internet', 'subject': 'Internet', 'link': ''},
    # {'name': 'Wildcard', 'subject': 'Wildcard', 'link': ''}
]

def populate_benchmark_table():
    for benchmark in benchmark_data:
        name = benchmark['name']
        subject = benchmark['subject']
        notes = benchmark.get('notes', None)
        link = benchmark['link']
        
        new_benchmark = Benchmark(name=name, notes=notes, subject=subject, link=link)
        
        db.session.add(new_benchmark)
        
    db.session.commit()
    print('Benchmark(s) added / updated!')
    
# with app.app_context():
#     populate_benchmark_table()
    
    
def update_benchmark(benchmark_name, new_link):
    benchmark = Benchmark.query.filter_by(name=benchmark_name).first()
    if benchmark:
        benchmark.link = new_link
        db.session.commit()
        print(f"Link for benchmark '{benchmark_name}' updated to '{new_link}'.")
    else:
        print(f"Benchmark '{benchmark_name}' not found.")


# with app.app_context():
#     update_benchmark('EQ Bench', 'https://eqbench.com/creative_writing.html')

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
    # {'name': 'Text Generation'},
    # {'name': 'Text Summation'},
    # {'name': 'General Knowledge'},
    # {'name': 'Conversation'},
    # {'name': 'Translation'},
    # {'name': 'Mathematics'},
    # {'name': 'Programming'},
    # {'name': 'Science'},
    # {'name': 'Medical Knowledge'},
    # {'name': 'Legal Knowledge'},
    # {'name': 'Advanced Reasoning'},
    # {'name': 'Document Analysis'},
    # {'name': 'Image Analysis'},
    # {'name': 'Video Analysis'},
    # {'name': 'Audio Processing'},
    # {'name': 'Basic Reasoning'},
    # {'name': 'Creativity'},
    # {'name': 'Relative User Preference'}
    # {'name': 'Internet Search'},
    # {'name': 'Wildcard'}

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

# with app.app_context():      
#     update_usecase('User Preferences', 'Relative User Preference')


usecase_mapping = {
    'Text Generation': 1,
    'Text Summation': 2,
    'General Knowledge': 3,
    'Conversation': 4,
    'Translation': 5,
    'Mathematics': 6,
    'Programming': 7,
    'Science': 8,
    'Medical Knowledge': 9,
    'Legal Knowledge': 10,
    'Advanced Reasoning': 11,
    'Document Analysis': 12,
    'Image Analysis': 13,
    'Video Analysis': 14,
    'Audio Processing': 15,
    'Basic Reasoning': 16,
    'Creativity': 17,
    'Relative User Preference': 18,
    'Internet Search': 19,
    'Wildcard': 20
}

def capitalise()        :
    usecases = Usecase.query.all()
    for usecase in usecases:
        usecase.name = usecase.name.title()
    db.session.commit()
    print('Usecases capitalised!')
        

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
    # {'llm_id': 1, 'benchmark_id': 28, 'score': 60.2},
    # {'llm_id': 1, 'benchmark_id': 18, 'score': 82.8},
    # {'llm_id': 1, 'benchmark_id': 19, 'score': 53.3},
    # {'llm_id': 1, 'benchmark_id': 11, 'score': 34.1},
    # {'llm_id': 1, 'benchmark_id': 20, 'score': 88.5},
    # {'llm_id': 1, 'benchmark_id': 6, 'score': 28.1},
    # {'llm_id': 1, 'benchmark_id': 9, 'score': 1119},
    # {'llm_id': 1, 'benchmark_id': 33, 'score': 49.08},
    # {'llm_id': 2, 'benchmark_id': 1, 'score': 86.4},
    # {'llm_id': 2, 'benchmark_id': 2, 'score': 95.3},
    # {'llm_id': 2, 'benchmark_id': 3, 'score': 89.5},
    # {'llm_id': 2, 'benchmark_id': 4, 'score': 87.5},
    # {'llm_id': 2, 'benchmark_id': 5, 'score': 96.3},
    # {'llm_id': 2, 'benchmark_id': 6, 'score': 46.5},
    # {'llm_id': 2, 'benchmark_id': 7, 'score': 95.9},
    # {'llm_id': 2, 'benchmark_id': 8, 'score': 83.9},
    # {'llm_id': 2, 'benchmark_id': 11, 'score': 54.0},
    # {'llm_id': 2, 'benchmark_id': 12, 'score': 96.0},
    # {'llm_id': 2, 'benchmark_id': 13, 'score': 74.5},
    # {'llm_id': 2, 'benchmark_id': 14, 'score': 76.5},
    # {'llm_id': 2, 'benchmark_id': 15, 'score': 87.5},
    # {'llm_id': 2, 'benchmark_id': 17, 'score': 81.4},
    # {'llm_id': 2, 'benchmark_id': 18, 'score': 88.9},
    # {'llm_id': 2, 'benchmark_id': 19, 'score': 74.5},
    # {'llm_id': 2, 'benchmark_id': 20, 'score': 97.6},
    # {'llm_id': 2, 'benchmark_id': 21, 'score': 88.4},
    # {'llm_id': 2, 'benchmark_id': 22, 'score': 56.8},
    # {'llm_id': 2, 'benchmark_id': 23, 'score': 78.0},
    # {'llm_id': 2, 'benchmark_id': 24, 'score': 56.0},
    # {'llm_id': 2, 'benchmark_id': 25, 'score': 29.1},
    # {'llm_id': 2, 'benchmark_id': 26, 'score': 82.4},
    # {'llm_id': 2, 'benchmark_id': 28, 'score': 74.4},
    # {'llm_id': 2, 'benchmark_id': 29, 'score': 78.5},
    # {'llm_id': 2, 'benchmark_id': 30, 'score': 78.2},
    # {'llm_id': 2, 'benchmark_id': 31, 'score': 87.4},
    # {'llm_id': 2, 'benchmark_id': 32, 'score': 72.4},
    # {'llm_id': 2, 'benchmark_id': 9, 'score': 1256},
    # {'llm_id': 2, 'benchmark_id': 33, 'score': 86.35},
    # {'llm_id': 4, 'benchmark_id': 1, 'score': 75.2},
    # {'llm_id': 4, 'benchmark_id': 2, 'score': 85.9},
    # {'llm_id': 4, 'benchmark_id': 4, 'score': 74.2},
    # {'llm_id': 4, 'benchmark_id': 5, 'score': 89.2},
    # {'llm_id': 4, 'benchmark_id': 6, 'score': 33.3},
    # {'llm_id': 4, 'benchmark_id': 8, 'score': 73.7},
    # {'llm_id': 4, 'benchmark_id': 11, 'score': 40.9},
    # {'llm_id': 4, 'benchmark_id': 12, 'score': 88.9},
    # {'llm_id': 4, 'benchmark_id': 13, 'score': 75.1},
    # {'llm_id': 4, 'benchmark_id': 14, 'score': 75.9},
    # {'llm_id': 4, 'benchmark_id': 15, 'score': 80.4},
    # {'llm_id': 4, 'benchmark_id': 28, 'score': 76.0},
    # {'llm_id': 4, 'benchmark_id': 18, 'score': 86.8},
    # {'llm_id': 4, 'benchmark_id': 19, 'score': 64.0},
    # {'llm_id': 4, 'benchmark_id': 21, 'score': 88.8},
    # {'llm_id': 4, 'benchmark_id': 22, 'score': 50.2},
    # {'llm_id': 4, 'benchmark_id': 29, 'score': 50.2},
    # {'llm_id': 4, 'benchmark_id': 30, 'score': 86.7},
    # {'llm_id': 4, 'benchmark_id': 9, 'score': 1178},
    # {'llm_id': 4, 'benchmark_id': 33, 'score': 63.65},
    # {'llm_id': 5, 'benchmark_id': 1, 'score': 79.0},
    # {'llm_id': 5, 'benchmark_id': 2, 'score': 89.0},
    # {'llm_id': 5, 'benchmark_id': 4, 'score': 75.1},
    # {'llm_id': 5, 'benchmark_id': 5, 'score': 93.2},
    # {'llm_id': 5, 'benchmark_id': 6, 'score': 40.4},
    # {'llm_id': 5, 'benchmark_id': 8, 'score': 82.9},
    # {'llm_id': 5, 'benchmark_id': 11, 'score': 40.5},
    # {'llm_id': 5, 'benchmark_id': 12, 'score': 92.3},
    # {'llm_id': 5, 'benchmark_id': 13, 'score': 83.5},
    # {'llm_id': 5, 'benchmark_id': 14, 'score': 73.0},
    # {'llm_id': 5, 'benchmark_id': 15, 'score': 79.4},
    # {'llm_id': 5, 'benchmark_id': 28, 'score': 78.3},
    # {'llm_id': 5, 'benchmark_id': 18, 'score': 87.9},
    # {'llm_id': 5, 'benchmark_id': 19, 'score': 71.0},
    # {'llm_id': 5, 'benchmark_id': 21, 'score': 89.5},
    # {'llm_id': 5, 'benchmark_id': 22, 'score': 53.1},
    # {'llm_id': 5, 'benchmark_id': 29, 'score': 81.1},
    # {'llm_id': 5, 'benchmark_id': 30, 'score': 88.7},
    # {'llm_id': 5, 'benchmark_id': 9, 'score': 1201},
    # {'llm_id': 5, 'benchmark_id': 33, 'score': 80.45},
    # {'llm_id': 6, 'benchmark_id': 1, 'score': 86.8},
    # {'llm_id': 6, 'benchmark_id': 2, 'score': 95.4},
    # {'llm_id': 6, 'benchmark_id': 4, 'score': 88.5},
    # {'llm_id': 6, 'benchmark_id': 5, 'score': 96.4},
    # {'llm_id': 6, 'benchmark_id': 6, 'score': 50.4},
    # {'llm_id': 6, 'benchmark_id': 8, 'score': 86.8},
    # {'llm_id': 6, 'benchmark_id': 11, 'score': 61.0},
    # {'llm_id': 6, 'benchmark_id': 12, 'score': 95.0},
    # {'llm_id': 6, 'benchmark_id': 13, 'score': 90.7},
    # {'llm_id': 6, 'benchmark_id': 14, 'score': 84.9},
    # {'llm_id': 6, 'benchmark_id': 15, 'score': 86.4},
    # {'llm_id': 6, 'benchmark_id': 18, 'score': 89.4},
    # {'llm_id': 6, 'benchmark_id': 19, 'score': 85.0},
    # {'llm_id': 6, 'benchmark_id': 20, 'score': 95.6},
    # {'llm_id': 6, 'benchmark_id': 21, 'score': 89.3},
    # {'llm_id': 6, 'benchmark_id': 22, 'score': 59.4},
    # {'llm_id': 6, 'benchmark_id': 23, 'score': 86.8},
    # {'llm_id': 6, 'benchmark_id': 28, 'score': 75.8},
    # {'llm_id': 6, 'benchmark_id': 29, 'score': 80.8},
    # {'llm_id': 6, 'benchmark_id': 30, 'score': 88.1},
    # {'llm_id': 6, 'benchmark_id': 9, 'score': 1248},
    # {'llm_id': 6, 'benchmark_id': 33, 'score': 82.19},
    # {'llm_id': 17, 'benchmark_id': 1, 'score': 85.9},
    # {'llm_id': 17, 'benchmark_id': 2, 'score': 93.3},
    # {'llm_id': 17, 'benchmark_id': 6, 'score': 46.2}
    # {'llm_id': 17, 'benchmark_id': 8, 'score': 89.2},
    # {'llm_id': 17, 'benchmark_id': 11, 'score': 67.7},
    # {'llm_id': 17, 'benchmark_id': 12, 'score': 90.8},
    # {'llm_id': 17, 'benchmark_id': 13, 'score': 87.5},
    # {'llm_id': 17, 'benchmark_id': 14, 'score': 84.1},
    # {'llm_id': 17, 'benchmark_id': 21, 'score': 93.1},
    # {'llm_id': 17, 'benchmark_id': 22, 'score': 62.2},
    # {'llm_id': 17, 'benchmark_id': 23, 'score': 78.7}
    # {'llm_id': 17, 'benchmark_id': 24, 'score': 64.6}
    # {'llm_id': 17, 'benchmark_id': 25, 'score': 39.4}
    # {'llm_id': 17, 'benchmark_id': 26, 'score': 93.5}
    # {'llm_id': 17, 'benchmark_id': 29, 'score': 87.7},
    # {'llm_id': 17, 'benchmark_id': 30, 'score': 94.4},
    # {'llm_id': 17, 'benchmark_id': 9, 'score': 1267},
    # {'llm_id': 8, 'benchmark_id': 1, 'score': 90.0},
    # {'llm_id': 8, 'benchmark_id': 2, 'score': 87.8},
    # {'llm_id': 8, 'benchmark_id': 8, 'score': 83.6},
    # {'llm_id': 8, 'benchmark_id': 11, 'score': 53.2},
    # {'llm_id': 8, 'benchmark_id': 12, 'score': 94.4},
    # {'llm_id': 8, 'benchmark_id': 13, 'score': 79.0},
    # {'llm_id': 8, 'benchmark_id': 14, 'score': 74.4},
    # {'llm_id': 8, 'benchmark_id': 21, 'score': 90.9},
    # {'llm_id': 8, 'benchmark_id': 22, 'score': 59.4},
    # {'llm_id': 8, 'benchmark_id': 23, 'score': 82.3},
    # {'llm_id': 8, 'benchmark_id': 24, 'score': 62.7},
    # {'llm_id': 8, 'benchmark_id': 25, 'score': 40.1},
    # {'llm_id': 8, 'benchmark_id': 26, 'score': 92.4},
    # {'llm_id': 8, 'benchmark_id': 29, 'score': 80.8},
    # {'llm_id': 8, 'benchmark_id': 30, 'score': 79.5},
    # {'llm_id': 8, 'benchmark_id': 33, 'score': 77.68},
    # {'llm_id': 10, 'benchmark_id': 17, 'score': 86.5},
    # {'llm_id': 10, 'benchmark_id': 28, 'score': 81.8},
    # {'llm_id': 10, 'benchmark_id': 31, 'score': 89.9},
    # {'llm_id': 10, 'benchmark_id': 32, 'score': 72.3},
    # {'llm_id': 16, 'benchmark_id': 21, 'score': 81.6},
    # {'llm_id': 16, 'benchmark_id': 23, 'score': 76.1},
    # {'llm_id': 16, 'benchmark_id': 29, 'score': 68.4},
    # {'llm_id': 18, 'benchmark_id': 1, 'score': 82.0},
    # {'llm_id': 18, 'benchmark_id': 4, 'score': 83.1},
    # {'llm_id': 18, 'benchmark_id': 5, 'score': 93.0},
    # {'llm_id': 18, 'benchmark_id': 6, 'score': 39.5},
    # {'llm_id': 18, 'benchmark_id': 8, 'score': 81.3},
    # {'llm_id': 18, 'benchmark_id': 12, 'score': 93.0},
    # {'llm_id': 18, 'benchmark_id': 14, 'score': 81.7},
    # {'llm_id': 18, 'benchmark_id': 11, 'score': 50.4},
    # {'llm_id': 18, 'benchmark_id': 9, 'score': 1213},
    # {'llm_id': 19, 'benchmark_id': 14, 'score': 53.0},
    # {'llm_id': 19, 'benchmark_id': 15, 'score': 62.4},
    # {'llm_id': 20, 'benchmark_id': 1, 'score': 62.5},
    # {'llm_id': 20, 'benchmark_id': 2, 'score': 81.3},
    # {'llm_id': 20, 'benchmark_id': 4, 'score': 75.3},
    # {'llm_id': 20, 'benchmark_id': 5, 'score': 78.7},
    # {'llm_id': 20, 'benchmark_id': 6, 'score': 26.3},
    # {'llm_id': 20, 'benchmark_id': 8, 'score': 56.0},
    # {'llm_id': 20, 'benchmark_id': 12, 'score': 39.9},
    # {'llm_id': 20, 'benchmark_id': 11, 'score': 13.1},
    # {'llm_id': 20, 'benchmark_id': 14, 'score': 30.5},
    # {'llm_id': 20, 'benchmark_id': 15, 'score': 47.5},
    # {'llm_id': 20, 'benchmark_id': 9, 'score': 1158},
    # {'llm_id': 20, 'benchmark_id': 33, 'score': 68.18},
    # {'llm_id': 21, 'benchmark_id': 33, 'score': 75.9}
    # {'llm_id': 22, 'benchmark_id': 1, 'score': 88.7},
    # {'llm_id': 22, 'benchmark_id': 6, 'score': 53.6},
    # {'llm_id': 22, 'benchmark_id': 11, 'score': 76.6},
    # {'llm_id': 22, 'benchmark_id': 13, 'score': 90.5}, 
    # {'llm_id': 22, 'benchmark_id': 14, 'score': 90.2},
    # {'llm_id': 22, 'benchmark_id': 22, 'score': 69.1},
    # {'llm_id': 22, 'benchmark_id': 21, 'score': 92.8},
    # {'llm_id': 22, 'benchmark_id': 29, 'score': 85.7},
    # {'llm_id': 22, 'benchmark_id': 30, 'score': 92.8},
    # {'llm_id': 22, 'benchmark_id': 9, 'score': 1287} 
    # {'llm_id': 23, 'benchmark_id': 1, 'score': 70.6},
    # {'llm_id': 23, 'benchmark_id': 2, 'score': 86.7},
    # {'llm_id': 23, 'benchmark_id': 4, 'score': 81.2},
    # {'llm_id': 23, 'benchmark_id': 5, 'score': 85.8},
    # {'llm_id': 23, 'benchmark_id': 9, 'score': 1146},
    # {'llm_id': 23, 'benchmark_id': 11, 'score': 41.8},
    # {'llm_id': 23, 'benchmark_id': 12, 'score': 58.4},
    # {'llm_id': 23, 'benchmark_id': 14, 'score': 40.2},
    # {'llm_id': 23, 'benchmark_id': 15, 'score': 60.7},
    # {'llm_id': 23, 'benchmark_id': 33, 'score': 65.32},
    # {'llm_id': 24, 'benchmark_id': 33, 'score': 74.68},
    # {'llm_id': 24, 'benchmark_id': 1, 'score': 82.0},
    # {'llm_id': 24, 'benchmark_id': 4, 'score': 83.1},
    # {'llm_id': 24, 'benchmark_id': 5, 'score': 93.0},
    # {'llm_id': 24, 'benchmark_id': 6, 'score': 39.5},
    # {'llm_id': 24, 'benchmark_id': 8, 'score': 81.3},
    # {'llm_id': 24, 'benchmark_id': 11, 'score': 50.4},
    # {'llm_id': 24, 'benchmark_id': 12, 'score': 93.0},
    # {'llm_id': 24, 'benchmark_id': 14, 'score': 81.7}
    # {'llm_id': 25, 'benchmark_id': 34, 'score': 100},
    # {'llm_id': 25, 'benchmark_id': 35, 'score': 100}
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
    

def update_llm_score(llm_id, benchmark_id, new_score):
    llm_benchmark_cell = db.session.query(llm_benchmark).filter(
        llm_benchmark.c.llm_id == llm_id,
        llm_benchmark.c.benchmark_id == benchmark_id
    ).update({llm_benchmark.c.score: new_score})
    db.session.commit()
    print(f"Score for LLM ID {llm_id} in benchmark ID {benchmark_id} updated to {new_score}.")


# with app.app_context():
#     update_llm_score(1, 33, 41.08)


def delete_llm_benchmark(llm_id):
    llm_benchmark_row = llm_benchmark.delete().where(
        llm_benchmark.c.llm_id == llm_id
    )
    
    db.session.execute(llm_benchmark_row)
    db.session.commit()
    print(f"Rows for LLM ID {llm_id} deleted.")

# delete_llm_benchmark()


benchmark_usecase_data = [
    # {'benchmark_id': 1, 'usecase_id': 3},
    # {'benchmark_id': 2, 'usecase_id': 16},
    # {'benchmark_id': 4, 'usecase_id': 16},
    # {'benchmark_id': 5, 'usecase_id': 16},
    # {'benchmark_id': 6, 'usecase_id': 8},
    # {'benchmark_id': 30, 'usecase_id': 8},
    # {'benchmark_id': 7, 'usecase_id': 16},
    # {'benchmark_id': 8, 'usecase_id': 11},
    # {'benchmark_id': 12, 'usecase_id': 6},
    # {'benchmark_id': 13, 'usecase_id': 6},
    # {'benchmark_id': 11, 'usecase_id': 6},
    # {'benchmark_id': 14, 'usecase_id': 7},
    # {'benchmark_id': 15, 'usecase_id': 7},
    # {'benchmark_id': 17, 'usecase_id': 9},
    # {'benchmark_id': 28, 'usecase_id': 9},
    # {'benchmark_id': 18, 'usecase_id': 10},
    # {'benchmark_id': 19, 'usecase_id': 10},
    # {'benchmark_id': 20, 'usecase_id': 10},
    # {'benchmark_id': 21, 'usecase_id': 12},
    # {'benchmark_id': 21, 'usecase_id': 13},
    # {'benchmark_id': 22, 'usecase_id': 13},
    # {'benchmark_id': 23, 'usecase_id': 13},
    # {'benchmark_id': 24, 'usecase_id': 14},
    # {'benchmark_id': 25, 'usecase_id': 15},
    # {'benchmark_id': 26, 'usecase_id': 15},
    # {'benchmark_id': 28, 'usecase_id': 10},
    # {'benchmark_id': 29, 'usecase_id': 12},
    # {'benchmark_id': 30, 'usecase_id': 12},
    # {'benchmark_id': 31, 'usecase_id': 9},
    # {'benchmark_id': 32, 'usecase_id': 9},
    # {'benchmark_id': 2, 'usecase_id': 1},
    # {'benchmark_id': 33, 'usecase_id': 17},
    # {'benchmark_id': 9, 'usecase_id': 18},
    # {'benchmark_id': 34, 'usecase_id': 19},
    # {'benchmark_id': 35, 'usecase_id': 20},
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
