import React, { useEffect } from 'react'
import useLLMScores from './hooks/useLLMScores.js'
import Section from './Section.js'
import Heading from './Heading.js'
import useBenchmarksUsecases from './hooks/useBenchmarksUsecases'
import useAllBenchmarks from './hooks/useAllBenchmarks.js'


//TODO Try to work out sticky column (Youtube)
const Data = () => {
    const { llmScores, error } = useLLMScores()

    useEffect(() => {
    }, [llmScores]);

    // Create an array of all unique benchmark names
    const benchmarks = [...new Set(Object.values(llmScores).flat().map(score => score.benchmark))];

    // Create an array of all LLM names
    const llms = Object.keys(llmScores);

    // Create a 2D array of scores
    const scores = llms.map(llm => benchmarks.map(benchmark => {
        const scoreObj = llmScores[llm].find(score => score.benchmark === benchmark);
        return scoreObj ? scoreObj.score : 'N/A';
    }));

    const { benchmarksUsecases, buErrors } = useBenchmarksUsecases()
    const { allBenchmarks, benchError } = useAllBenchmarks()



    return (
        <Section customPosition='flex flex-col justify-center text-center' >
            <div id='data' className='container relative z-2 min-h-screen'>
                <Heading
                    className='md:max-w-md lg:max-w-2xl text-center' // Sets width of Heading, affects space from edge
                    title='WhichLLM Data'
                />

                {/* Benchmark = benchmark name from benchmarksUsecases. allBenchmarks = all benchmarks (names, links, IDs) */}
                <h3 className='h3'>List of benchmarks and their associated usecases:</h3>
                <div className='grid grid-cols-2 md:flex md:flex-wrap md:justify-center mt-[2rem]'>
                    {Object.entries(benchmarksUsecases).map(([usecase, benchmarks], index) => (
                        <div key={index} className='mb-6 mx-3 p-3 bg-blue-100 rounded hover:bg-blue-200 transition-colors'>
                            <h3 className='h4'>{usecase}</h3>
                            <ul>
                                {benchmarks.map((benchmark, index) => {
                                    let allBenchmark = allBenchmarks.find(b => b.name === benchmark);
                                    return (
                                        <li key={index}>
                                            <a href={allBenchmark ? allBenchmark.link : '#'} target="_blank" rel="noopener noreferrer">
                                                <strong>{benchmark}</strong>
                                            </a>
                                        </li>
                                    )

                                })}
                            </ul>
                        </div>
                    ))}
                </div>

                <h3 className='h3 mt-[2rem]'>LLM Scores for each benchmark:</h3>
                <div className=" max-w-full overflow-x-auto px-5 mt-[2rem]">
                    <table className='table-fixed rounded-lg shadow-md'>
                        <thead className='bg-blue-600 text-white'>
                            <tr>
                                <th className='border p-2 min-w-[150px] sticky left-0 bg-blue-600'>LLM / Benchmark</th>
                                {benchmarks.map((benchmark, index) =>
                                    <th key={index} className='border p-2'>{benchmark}</th>
                                )}
                            </tr>
                        </thead>

                        <tbody>
                            {llms.map((llm, i) => (
                                <tr key={i} className={i % 2 === 0 ? 'bg-blue-100' : 'bg-white'}>
                                    <td className={`border p-2 mx-5 min-w-[150px] sticky left-0 ${i % 2 === 0 ? 'bg-blue-100' : 'bg-white'}`}>{llm}</td>
                                    {scores[i].map((score, j) =>
                                        <td className='border p-2 min-w-[100px] break-words' key={j}>{score}</td>
                                    )}
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </Section>




    )
}

export default Data