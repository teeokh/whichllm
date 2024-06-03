import React from 'react'
import Section from './Section'
import Heading from './Heading'
import { description } from '../constants/HowItWorks.js'
import { about } from '../constants/About.js'


const HowItWorks = () => {

    return (
        <Section id='how-it-works'>
            <div className='container relative z-2'>
                <Heading
                    className='md:max-w-md lg:max-w-2xl text-center' // Sets width of Heading, affects space from edge
                    title='How WhichLLM works, using LLM benchmarks'
                />
                <div className='flex flex-wrap flex-col gap-10 text-center'>
                    <p>{description}</p>

                    <h4 className='h4'>About WhichLLM</h4>
                    <p>{about}</p>
                </div>
            </div>

        </Section >
    )
}

export default HowItWorks
