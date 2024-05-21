import React, { useState } from 'react';
import useRecommendation from '../hooks/useRecommendation.js';
import useUsecaseName from '../hooks/useUsecaseName.js';
import Filter from '../Filter/Filter.js'
import './Recommendation.css';

const Recommendation = ({ usecaseId, statusFilter, topN }) => {
    const { recommendation, error: recError } = useRecommendation(usecaseId, statusFilter, topN);
    const { usecaseName, error: nameError } = useUsecaseName(usecaseId);

    if (recError || nameError) {
        return <p>{recError || nameError}</p>;
    }

    const bestLLM = recommendation[0]
    const nextBestLLMs = recommendation.slice(1, 3)

    if (!recommendation.length) {
        return <p>Loading...</p>;
    }

    const handleClick = () => {
        window.open(bestLLM.llm.link, "_blank");
    }

    return (
            <div>
                <h1>The best tool for you is...</h1>
                <div>
                    <h2 onClick={handleClick} style={{ cursor: 'pointer' }}>{bestLLM.llm.name}</h2>
                    <p>It scored an average of {bestLLM.score} on the {usecaseName} benchmarks
                    {nextBestLLMs.length === (topN - 1) && (
                        <p>Compared to {nextBestLLMs[0].llm.name} ({nextBestLLMs[0].score}) and {nextBestLLMs[1].llm.name} ({nextBestLLMs[1].score})</p>
                )}
                    </p>
                    <p>Link: <a href={bestLLM.llm.link} target="_blank" rel="noopener noreferrer">{bestLLM.llm.link}</a></p>
                    <p>Provider: {bestLLM.llm.provider}</p>
                </div>
                
            </div>
    );
};

export default Recommendation;
