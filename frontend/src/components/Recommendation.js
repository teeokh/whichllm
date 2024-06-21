import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion'
import useRecommendation from '../components/hooks/useRecommendation.js';
import useUsecaseName from '../components/hooks/useUsecaseName.js';
import useUsecases from './hooks/useUsecases.js';
import useAllBenchmarks from './hooks/useAllBenchmarks.js';
import Title from './Title.js'
import { llmLogos } from '../constants/llmLogos.js'


const Recommendation = ({ usecaseId, statusFilter, topN, triggerShowRec, hideRec }) => {
    const { recommendation, benchmarks } = useRecommendation(usecaseId, statusFilter, topN);
    const { usecases } = useUsecases();
    const { usecaseName } = useUsecaseName(usecaseId);
    const { allBenchmarks } = useAllBenchmarks()
    const [loading, setLoading] = useState(true);

    const bestLLM = recommendation[0]
    const nextBestLLMs = recommendation.slice(1, 3)

    const Logo = bestLLM && bestLLM.llm ? llmLogos[bestLLM.llm.provider] : undefined;

    useEffect(() => {
        const timer = setTimeout(() => {
            setLoading(false);
        }, 3000);

        if (recommendation.length) {
            clearTimeout(timer)
            setLoading(false)
        }

        return () => clearTimeout(timer); // This will clear the timeout if the component unmounts before the timeout finishes
    }, [recommendation]);

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
            <AnimatePresence mode='popLayout'>
                <motion.div
                    initial={{ scale: 0.8, opacity: 0, height: 0 }}
                    animate={{ scale: 1, opacity: 1, height: 'auto' }}
                    exit={{ scale: 0.8, opacity: 0, height: 0 }}
                    transition={{ type: 'spring', bounce: 0.25 }}
                    className='flex flex-col items-center text-center'>

                    <Title />

                    <div className='mt-10'>
                        <h2 className=''>The best tool for you is...</h2>

                        {/* Top recommendation */}
                        <h1 className='flex items-center justify-center gap-4 font-bold mb-3 mt-3'>
                            <a className='top-rec' href={bestLLM.llm.link} target='_blank' rel="noopener noreferrer">{bestLLM.llm.name}</a>
                            {Logo ?
                                <a href={bestLLM.llm.link} target='_blank' rel="noopener noreferrer">
                                    <Logo
                                        width='40'
                                        height='40' />
                                </a>
                                : ''}
                        </h1>

                        {/* Recommendations information */}
                        <div className='flex flex-col w-full items-center mb-5'>
                            <p>It scored an average of {bestLLM.score} on the <a className='text-lg font-black hover:text-blue-600' href='#data'>{usecaseName}</a> benchmarks</p>
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
                        <motion.button
                            whileHover={{ scale: 1.05 }}
                            className='button-primary' onClick={hideRec}>Search Again?
                        </motion.button>
                    </div>
                </motion.div>
            </AnimatePresence>
        )
    }

}

export default Recommendation;