import React from 'react'
import { about } from '../constants/About.js'
import Section from './Section.js'
import Heading from './Heading.js'

const About = () => {
    return (
        <Section id='about' customPaddings='py-5 lg:py-10 xl:py-15 px-2 border-b border-blue-200'>
            <div className='container relative z-2'>
                <Heading
                    className='md:max-w-md lg:max-w-2xl text-center'
                    title='About WhichLLM'
                />
                <div className='flex flex-wrap flex-col gap-10 text-center'>
                    <p>{about}</p>
                </div>
            </div>
        </Section >
    )
}

export default About
