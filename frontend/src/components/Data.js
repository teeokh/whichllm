import React, { useEffect } from 'react';
import useLLMScores from './hooks/useLLMScores.js';
import Section from './Section.js';
import Heading from './Heading.js';
import useBenchmarksUsecases from './hooks/useBenchmarksUsecases';
import useAllBenchmarks from './hooks/useAllBenchmarks.js';

const Data = () => {
    const { llmScores } = useLLMScores();

    useEffect(() => { }, [llmScores]);

    const benchmarks = [...new Set(Object.values(llmScores).flat().map(score => score.benchmark))];
    const llms = Object.keys(llmScores);
    const scores = llms.map(llm => benchmarks.map(benchmark => {
        const scoreObj = llmScores[llm].find(score => score.benchmark === benchmark);
        return scoreObj ? scoreObj.score : 'N/A';
    }));

    const { benchmarksUsecases } = useBenchmarksUsecases();
    const { allBenchmarks } = useAllBenchmarks();

    return (
        <Section customPosition='flex flex-col justify-center text-center'>
            <div id='data' className='container relative z-2 min-h-screen px-4 md:px-10'>
                <Heading
                    className='md:max-w-md lg:max-w-2xl text-center mb-8'
                    title='WhichLLM Data'
                />

                <h3 className='text-2xl font-semibold mb-6'>List of benchmarks and their associated usecases:</h3>
                <div className='grid grid-cols-2 lg:grid-cols-3 gap-4'>
                    {Object.entries(benchmarksUsecases).map(([usecase, benchmarks], index) => (
                        <div key={index} className='bg-blue-950 hover:shadow-md transition-shadow hover:shadow-blue-950 rounded-md p-4'>
                            <h4 className='text-xl font-medium mb-4 text-white'>{usecase}</h4>
                            <ul>
                                {benchmarks.map((benchmark, index) => {
                                    let allBenchmark = allBenchmarks.find(b => b.name === benchmark);
                                    return (
                                        <li key={index} className='mb-2'>
                                            <a
                                                href={allBenchmark ? allBenchmark.link : '#'}
                                                target="_blank"
                                                rel="noopener noreferrer"
                                                className='text-white text-sm hover:underline'
                                            >
                                                <strong>{benchmark}</strong>
                                            </a>
                                        </li>
                                    );
                                })}
                            </ul>
                        </div>
                    ))}
                </div>

                <h3 className='text-2xl font-semibold mt-12 mb-6'>LLM Scores for each benchmark:</h3>
                <div className='max-w-full overflow-x-auto'>
                    <table className='table-auto w-full border-collapse text-center'>
                        <thead className='bg-blue-950 text-white'>
                            <tr>
                                <th className='border p-4 max-w-[120px] lg:min-w-[150px] sticky left-0 bg-blue-950'>LLM / Benchmark</th>
                                {benchmarks.map((benchmark, index) => (
                                    <th key={index} className='border p-4 max-w-[120px] lg:min-w-[120px]'>{benchmark}</th>
                                ))}
                            </tr>
                        </thead>
                        <tbody>
                            {llms.map((llm, i) => (
                                <tr key={i} className={i % 2 === 0 ? 'bg-white' : 'bg-blue-950 text-white'}>
                                    <td className={`border p-4 sticky left-0 ${i % 2 === 0 ? 'bg-white' : 'bg-blue-950 text-white'}`}>{llm}</td>
                                    {scores[i].map((score, j) => (
                                        <td key={j} className='border p-4'>{score}</td>
                                    ))}
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </Section>
    );
};

export default Data;
