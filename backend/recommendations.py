from models import *
from config import db, app

def top_llms_for_usecase(usecase_id, status_filter=None, top_n=3):
    
    usecase = Usecase.query.filter_by(id=usecase_id).first()
    
    # Returns the benchmarks associated with the given usecase
    benchmarks = Benchmark.query.join(benchmark_usecase).filter(benchmark_usecase.c.usecase_id == usecase_id).all() 
    
    # Iterate through each benchmark and extract their benchmark ID (excluding elo benchmark unless elo_only)
    if usecase_id == 18:
        benchmark_ids = [b.id for b in benchmarks if b.id == 9]
        
    else:
        benchmark_ids = [b.id for b in benchmarks if b.id != 9]

    
    # Return a list of all LLMs with any of those benchmarks. Filter for free vs paid
    if status_filter != None:
        llms = LLM.query.join(llm_benchmark, LLM.id == llm_benchmark.c.llm_id) \
                        .filter(llm_benchmark.c.benchmark_id.in_(benchmark_ids)) \
                        .filter(LLM.status == status_filter) \
                        .all()
    
    else:   
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
    
    # Return the top n LLMs for the usecase. Returns a list of tuples (which is not serializable innately)
    # print(f'These are the top {top_n} LLMs for {usecase.name}: {llm_scores[:top_n]}')
    return llm_scores[:top_n]
        

if __name__ == "__main__":
    with app.app_context():
        top_llms_for_usecase(usecase_id=3, status_filter='free', top_n=4)
        