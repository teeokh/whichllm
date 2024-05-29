import React, { useState, useEffect } from 'react'
import Recommendation from './Recommendation.js'
import useRecommendation from './hooks/useRecommendation.js'
import useUsecaseName from './hooks/useUsecaseName.js'
import UsecaseBtn from './UsecaseBtn.js'
import useUsecases from './hooks/useUsecases.js'
import Filter from './Filter.js'
import Header from './Header.js'
import ButtonGradient from "../assets/svg/ButtonGradient";
import Section from './Section.js'
import HowItWorks from './HowItWorks.js'



const Main = () => {
    const [usecaseId, setUsecaseId] = useState(1);
    const [statusFilter, setStatusFilter] = useState(null);
    const [topN, setTopN] = useState(3);

    const { usecases, error } = useUsecases();
    const { recommendation, error: recError } = useRecommendation(usecaseId, statusFilter, topN);


    return (
        <>
            <div className='min-h-screen'>
                <div className='h-[5.125rem]'>
                    <Header />
                </div>

                <ButtonGradient />
                <Section>
                    <div className='flex flex-col items-center justify-center px-2'>
                        <section className='mb-[1.5rem] mt-[2.5rem] md:mb-[2rem] lg:mb-[2.5rem] md:mt-[4rem] lg:mt-[6rem]'>
                            <UsecaseBtn onSelect={setUsecaseId} />
                        </section>
                        <section className='mb-10'>
                            <Recommendation usecaseId={usecaseId} statusFilter={statusFilter} topN={topN} />
                        </section>
                        <section className='mb-10 lg:mb-[11rem]'>
                            <Filter onSelect={setStatusFilter} />
                        </section>
                    </div>
                </Section>

            </div>

            <div className='min-h-screen'>
                <HowItWorks />
            </div>
        </>
    )
}

export default Main;