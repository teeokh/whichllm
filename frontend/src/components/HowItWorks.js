import React from 'react'
import Section from './Section'
import Heading from './Heading'
import { description } from '../constants/HowItWorks.js'
import useBenchmarksUsecases from './hooks/useBenchmarksUsecases'


const HowItWorks = () => {
    const { benchmarksUsecases, error } = useBenchmarksUsecases()

    return (
        <Section id='how-it-works'>
            <div className='container relative z-2'>
                <Heading
                    className='md:max-w-md lg:max-w-2xl text-center' // Sets width of Heading, affects space from edge
                    title='How WhichLLM works, using LLM benchmarks'
                />
                <div className='flex flex-wrap flex-col gap-10 text-center'>
                    <p>{description}</p>

                    <h3 className='h3'>List of Benchmarks and their associated Usecases:</h3>
                    <div className='grid grid-cols-2 md:flex md:flex-wrap md:justify-center '>
                        {Object.entries(benchmarksUsecases).map(([usecase, benchmarks], index) => (
                            <div key={index} className='mb-6 mx-3 p-3 bg-blue-100 hover:bg-blue-200 transition-colors'>
                                <h3 className='h3'>{usecase}</h3>
                                <ul>
                                    {benchmarks.map((benchmark, index) => (
                                        <li key={index}>
                                            <strong>{benchmark}</strong>
                                        </li>
                                    ))}
                                </ul>
                            </div>
                        ))}
                    </div>

                </div>
            </div>
        </Section >
    )
}

export default HowItWorks
