import React from 'react'
import Section from './Section'
import Heading from './Heading'
import { description } from '../constants/howItWorks.js'
import { about } from '../constants/about.js'
import { main_disclaimer, update_disclaimer, missing_data_disclaimer } from '../constants/disclaimer.js'


const HowItWorks = () => {

    return (
        <Section>
            <div id='how-it-works' className='container relative z-2'>
                <Heading
                    className='md:max-w-md lg:max-w-2xl text-center' // Sets width of Heading, affects space from edge
                    title='How WhichLLM works, using LLM benchmarks'
                />
                <div className='flex flex-wrap flex-col gap-10 text-center'>
                    <p>{description}</p>
                    <p>{update_disclaimer}</p>

                    <h4 id='about' className='h4'>About WhichLLM</h4>
                    <p>{about}</p>

                    <h4 className='h4'>Disclaimer</h4>
                    <p>{main_disclaimer}</p>
                    <p>{missing_data_disclaimer}</p>
                </div>
            </div>

        </Section >
    )
}

export default HowItWorks
