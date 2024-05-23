import React, { useState } from 'react';
import useRecommendation from '../components/hooks/useRecommendation.js';
import useUsecaseName from '../components/hooks/useUsecaseName.js';
import Filter from '../components/Filter.js'

const Recommendation = ({ usecaseId, statusFilter, topN }) => {
    const { recommendation, error: recError } = useRecommendation(usecaseId, statusFilter, topN);
    const { usecaseName, error: nameError } = useUsecaseName(usecaseId);

    if (recError || nameError) {
        return <p>{recError || nameError}</p>;
    }

    const bestLLM = recommendation[0]
    const nextBestLLMs = recommendation.slice(1, 3)

    if (!recommendation.length) {
        return <p></p>;
    }

    return (
        <div className='flex flex-col items-center text-center p-4'>
            <h2 className='font-bold'> The best tool for you is...</h2>

            {/* Top recommendation */}
            <h1 className='font-bold p-4'>
                <a className='bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-teal-400 hover:from-teal-400 hover:to-blue-500 text-3xl' href={bestLLM.llm.link} target='_blank' rel="noopener noreferrer">{bestLLM.llm.name}</a>
            </h1>
            
            {/* Recommendations information */}
            <div className='flex flex-col w-full items-center'>
                <p>It scored an average of {bestLLM.score} on the {usecaseName} benchmarks</p>
                {nextBestLLMs.length === (topN - 1) && (

                    // Next best recommendations
                    <p>Compared to <a className='hover:text-sky-500' href={nextBestLLMs[0].llm.link} target='_blank' rel="noopener noreferrer">
                        {nextBestLLMs[0].llm.name}
                    </a> ({nextBestLLMs[0].score})
                        and <a className='hover:text-sky-500' href={nextBestLLMs[1].llm.link} target='_blank' rel="noopener noreferrer">
                            {nextBestLLMs[1].llm.name}
                        </a> ({nextBestLLMs[1].score})
                    </p>)}

                <p>Link: <a className='hover:text-sky-500' href={bestLLM.llm.link} target="_blank" rel="noopener noreferrer">{bestLLM.llm.link}</a></p>
                <p>Provider: {bestLLM.llm.provider}</p>
            </div>
            <div>
                <p className=''>This score takes an average of the following benchmarks:</p>
            </div>
        </div>
    );
};

export default Recommendation;