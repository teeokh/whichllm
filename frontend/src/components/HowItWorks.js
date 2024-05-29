import React from 'react'
import Section from './Section'
import Heading from './Heading'
import { description, benchmarks } from '../constants/HowItWorks.js'

const groupedBenchmarks = benchmarks.reduce((groups, benchmark) => {
    const key = benchmark.subject;
    if (!groups[key]) {
        groups[key] = [];
    }
    groups[key].push(benchmark);
    return groups;
}, {});

const HowItWorks = () => (
    <Section id='how-it-works'>
        <div className='container relative z-2'>
            <Heading
                className='md:max-w-md lg:max-w-2xl' // Sets width of Heading, affects space from edge
                title='How WhichLLM works, using LLM benchmarks'
            />
            <div className='flex flex-wrap flex-col gap-10 mb-10'>
                <p>{description}</p>

                <h3 className='h3'>List of benchmarks and their associated usecases:</h3>
                <div className='grid md:grid-cols-2 lg:grid-cols-3 '>
                    {Object.entries(groupedBenchmarks).map(([subject, benchmarks], index) => (
                        <div key={index} className='mb-6 mx-3 p-3 bg-blue-100'>
                            <h4 className='h4'>{subject}</h4>
                            <ul>
                                {benchmarks.map((benchmark, index) => (
                                    <li key={index}>
                                        <strong>{benchmark.name}</strong>
                                        {benchmark.notes && <span> ({benchmark.notes})</span>}
                                    </li>
                                ))}
                            </ul>
                        </div>
                    ))}
                </div>

            </div>
        </div>
    </Section>
)

export default HowItWorks
