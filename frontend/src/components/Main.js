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
import Data from './Data.js'
import About from './About.js'



const Main = () => {
    const [usecaseId, setUsecaseId] = useState(1);
    const [statusFilter, setStatusFilter] = useState(null);
    const [topN, setTopN] = useState(3);

    const { usecases, error } = useUsecases();
    const { recommendation, error: recError } = useRecommendation(usecaseId, statusFilter, topN);


    return (
        <>
            <div className='min-h-screen'>
                <div className='h-[5rem]'>
                    <Header />
                </div>

                <ButtonGradient />
                <Section className='' customPosition='' customPaddings=''>
                    <div>
                        <div className='flex flex-col items-center justify-center '  >
                            <section className='mb-[1.5rem] mt-[2rem] md:mb-[2rem] lg:mb-[2.5rem] md:mt-[3rem] lg:mt-[4rem]'>
                                <UsecaseBtn onSelect={setUsecaseId} />
                            </section>
                            <section className='mb-10'>
                                <Recommendation usecaseId={usecaseId} statusFilter={statusFilter} topN={topN} />
                            </section>
                            <section className='mb-10'>
                                <Filter onSelect={setStatusFilter} />
                            </section>
                        </div>
                    </div>
                </Section>


            </div>

            <Data />
            <HowItWorks />
        </>
    )
}

export default Main;