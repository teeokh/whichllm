from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import LLM, Benchmark, Usecase, llm_benchmark, benchmark_usecase, LLMStatus
from config import db_path

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

benchmark_data = [
    # {'name': 'MMLU', 'subject': 'General'}
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