import React, { useState } from 'react';
import useRecommendation from '../components/hooks/useRecommendation.js';
import useUsecaseName from '../components/hooks/useUsecaseName.js';
import useUsecases from './hooks/useUsecases.js';
import Filter from '../components/Filter.js'
import useAllBenchmarks from './hooks/useAllBenchmarks.js';

const Recommendation = ({ usecaseId, statusFilter, topN }) => {
    const { recommendation, benchmarks, error: recError } = useRecommendation(usecaseId, statusFilter, topN);
    const { usecases, error } = useUsecases();
    const { usecaseName, error: nameError } = useUsecaseName(usecaseId);
    const { allBenchmarks, error: benchmarkError } = useAllBenchmarks()

    if (!recommendation.length || !usecases.length) {
        return <p className=''>There are no recommendations for this usecase. Try changing your filter</p>
    }

    const bestLLM = recommendation[0]
    const nextBestLLMs = recommendation.slice(1, 3)

    return (

        <div className='flex flex-col items-center text-center'>
            <h2 className=''> The best tool for you is...</h2>

            {/* Top recommendation */}
            <h1 className='font-bold mb-3 mt-3'>
                <a className='top-rec' href={bestLLM.llm.link} target='_blank' rel="noopener noreferrer">{bestLLM.llm.name}</a>
            </h1>

            {/* Recommendations information */}
            <div className='flex flex-col w-full items-center mb-5'>
                <p>It scored an average of {bestLLM.score} on the {usecaseName} benchmarks</p>
                {nextBestLLMs.length === (topN - 1) && (

                    // Next best recommendations
                    <p>Compared to <a href={nextBestLLMs[0].llm.link} target='_blank' rel="noopener noreferrer">
                        {nextBestLLMs[0].llm.name}
                    </a> ({nextBestLLMs[0].score})
                        and <a href={nextBestLLMs[1].llm.link} target='_blank' rel="noopener noreferrer">
                            {nextBestLLMs[1].llm.name}
                        </a> ({nextBestLLMs[1].score})
                    </p>)}

                <p>Link: <a href={bestLLM.llm.link} target="_blank" rel="noopener noreferrer">{bestLLM.llm.link}</a></p>
                <p>Provider: {bestLLM.llm.provider}</p>
            </div>
            <div>
                <p>This score takes an average of the following benchmarks:</p>
                <p>
                    {benchmarks.map((benchmark, index) => {
                        let allBenchmark = allBenchmarks.find(b => b.name === benchmark);
                        return (
                            <span key={index}>
                                <a href={allBenchmark ? allBenchmark.link : '#'} target="_blank" rel="noopener noreferrer">{benchmark}</a>
                            </span>
                        );

                        // Adds ',' after each element in the array
                    }).reduce((prev, curr, index, array) => {
                        return index !== array.length - 1 ? [prev, curr, ', '] : [prev, curr]

                        // First value is an empty array  
                    }, [])
                    }
                </p>
            </div>
        </div>
    )
}


export default Recommendation;