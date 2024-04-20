from models import *
from config import db, app
from populate_tables import session

def top_llms_for_usecase(usecase_id, top_n=3):
    
    usecase = Usecase.query.filter_by(id=usecase_id).first()
    
    # Returns the benchmarks associated with the given usecase (excluding Chatbot Arena)
    benchmarks = Benchmark.query.join(benchmark_usecase).filter(benchmark_usecase.c.usecase_id == usecase_id).all() 
    
    # Iterate through each benchmark and extract their benchmark ID
    benchmark_ids = [b.id for b in benchmarks if b.id != 33]
    
    # Return a list of all LLMs with any of those benchmarks
    llms = LLM.query.join(llm_benchmark, LLM.id == llm_benchmark.c.llm_id) \
                        .filter(llm_benchmark.c.benchmark_id.in_(benchmark_ids)) \
                        .all()
                        
    # Return average scores on these benchmarks for each LLM
    llm_scores = []
    for llm in llms:
        # Fetch scores for the current LLM's benchmarks
        scores = db.session.query(llm_benchmark.c.score) \
                        .filter(llm_benchmark.c.llm_id == llm.id, 
                                llm_benchmark.c.benchmark_id.in_(benchmark_ids)) \
                        .all()
        # Extract score values from the result tuples
        scores = [score[0] for score in scores]
        
        # If score is present for LLM, get average and add to list, with LLM 
        if scores:
            avg_score = sum(scores) / len(scores)
            llm_scores.append((llm, avg_score))
    
    # Sort the LLM scores in reverse order (highest to lowest)
    llm_scores.sort(key=lambda x: x[1], reverse=True)
    
    # Return the top n LLMs
    print(llm_scores[:top_n])
    return llm_scores[:top_n]
        
        

if __name__ == "__main__":
    with app.app_context():
        top_llms_for_usecase(7, 4)
