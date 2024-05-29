import React from 'react'
import Section from './Section'
import Heading from './Heading'
import { description } from '../constants/HowItWorks.js'

const HowItWorks = () => {
    return (
        <Section id='how-it-works'>
            <div className='container relative z-2'>
                <Heading
                    className='md:max-w-md lg:max-w-2xl' // Sets width of Heading, affects space from edge
                    title='How WhichLLM works, using LLM benchmarks'
                />
                <div className='flex flex-wrap gap-10 mb-10'>
                    <p>{description}</p>

                </div>
            </div>
        </Section>
    )
}

export default HowItWorks
