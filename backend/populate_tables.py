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

populate_llm_table()

benchmark_data = {
    
}