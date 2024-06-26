import React from 'react'
import Section from './Section'
import Heading from './Heading'
import { description } from '../constants/howItWorks.js'
import { about } from '../constants/about.js'
import { main_disclaimer, update_disclaimer, missing_data_disclaimer } from '../constants/disclaimer.js'


const HowItWorks = () => {

    return (
        <Section>
            <div id='how-it-works' className='container relative z-2 '>
                <Heading
                    className='md:max-w-md lg:max-w-2xl text-center !mb-4' // Sets width of Heading, affects space from edge
                    title='How it Works'
                />
                <div className='flex flex-wrap flex-col gap-10 text-center'>
                    <div>
                        <p className='mb-6'>{description}</p>
                        <p>{update_disclaimer}</p>
                    </div>

                    <div>
                        <h4 id='about' className='h4 mb-6'>About WhichLLM</h4>
                        <p>{about}</p>
                    </div>

                    <div>
                        <h4 className='h4 mb-4'>Disclaimer</h4>
                        <p className='mb-6'>{main_disclaimer}</p>
                        <p>{missing_data_disclaimer}</p>
                    </div>
                </div>
            </div>

        </Section >
    )
}

export default HowItWorks
