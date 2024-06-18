import React, { useState, useEffect } from 'react';
import useRecommendation from '../components/hooks/useRecommendation.js';
import useUsecaseName from '../components/hooks/useUsecaseName.js';
import useUsecases from './hooks/useUsecases.js';
import useAllBenchmarks from './hooks/useAllBenchmarks.js';
import Title from './Title.js'


const Recommendation = ({ usecaseId, statusFilter, topN, triggerShowRec, hideRec }) => {
    const { recommendation, benchmarks } = useRecommendation(usecaseId, statusFilter, topN);
    const { usecases } = useUsecases();
    const { usecaseName } = useUsecaseName(usecaseId);
    const { allBenchmarks, error: benchmarkError } = useAllBenchmarks()
    const [loading, setLoading] = useState(true);

    const bestLLM = recommendation[0]
    const nextBestLLMs = recommendation.slice(1, 3)

    useEffect(() => {
        const timer = setTimeout(() => {
            setLoading(false);
        }, 200);

        return () => clearTimeout(timer); // This will clear the timeout if the component unmounts before the timeout finishes
    }, []);

    // TODO filter button not working once recommendation selected

    if (loading) {
        return <p>Fetching...</p>;
    }
    else if (!recommendation.length || !usecases.length) {
        return (
            <div className='flex flex-col items-center'>
                <p>There are no recommendations for this usecase. Try changing your filter</p>
                <div className='mt-10'>
                    <button className='button-primary' onClick={hideRec}>Search Again?</button>
                </div>
            </div>

        )

    }
    else if (recommendation.length || usecases.length) {
        return (
            <div className='flex flex-col items-center text-center'>

                <Title />

                <div className='mt-10'>
                    <h2 className=''>The best tool for you is...</h2>

                    {/* Top recommendation */}
                    <h1 className='font-bold mb-3 mt-3'>
                        <a className='top-rec' href={bestLLM.llm.link} target='_blank' rel="noopener noreferrer">{bestLLM.llm.name}</a>
                    </h1>

                    {/* Recommendations information */}
                    <div className='flex flex-col w-full items-center mb-5'>
                        <p>It scored an average of {bestLLM.score} on the {usecaseName} benchmarks</p>
                        <p>Provider: {bestLLM.llm.provider}</p>
                    </div>
                    <div className='flex flex-col w-full items-center mb-8'>
                        <p>This score uses the following benchmarks:</p>
                        <p>
                            {benchmarks.map((benchmark, index) => {
                                let allBenchmark = allBenchmarks.find(b => b.name === benchmark);
                                return (
                                    <span key={index}>
                                        <a href={allBenchmark ? allBenchmark.link : '#'} target="_blank" rel="noopener noreferrer">{benchmark}</a>
                                    </span>
                                );
                            }).reduce((prev, curr, index, array) => {
                                return index !== array.length - 1 ? [prev, curr, ', '] : [prev, curr];
                            }, [])
                            }
                        </p>
                    </div>

                    <div className=''>
                        {nextBestLLMs.length >= 1 && (
                            <div>
                                <p className='text-xl'>Close Competitors:</p>
                                <span>
                                    <a className='h5' href={nextBestLLMs[0].llm.link} target='_blank' rel="noopener noreferrer">
                                        {nextBestLLMs[0].llm.name}
                                    </a> ({nextBestLLMs[0].score})
                                </span>

                                {nextBestLLMs.length >= 2 && (
                                    <span>
                                        {' '}and <a className='h5' href={nextBestLLMs[1].llm.link} target='_blank' rel="noopener noreferrer">
                                            {nextBestLLMs[1].llm.name}
                                        </a> ({nextBestLLMs[1].score})
                                    </span>
                                )}
                            </div>
                        )}
                    </div>
                </div>

                <div className='mt-10'>
                    <button className='button-primary' onClick={hideRec}>Search Again?</button>
                </div>
            </div>
        )
    }

}

export default Recommendation;