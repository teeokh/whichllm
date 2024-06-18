import React, { useState } from 'react'
import Recommendation from './Recommendation.js'
import UsecaseSelection from './UsecaseSelection.js'
import Filter from './Filter.js'
import Header from './Header.js'
import ButtonGradient from "../assets/svg/ButtonGradient";
import Section from './Section.js'
import HowItWorks from './HowItWorks.js'
import Data from './Data.js'
import Footer from './Footer.js'
import useShowRecommendation from './hooks/useShowRecommendation.js'

const Main = () => {
    const [usecaseId, setUsecaseId] = useState(1);
    const [statusFilter, setStatusFilter] = useState(null);
    const [topN] = useState(3);
    const { showRecommendation, triggerShowRecommendation, hideRecommendation } = useShowRecommendation();

    return (
        <>
            <div className='min-h-screen flex flex-col justify-center'>
                <div className='h-[5rem]'>
                    <Header />
                </div>

                <ButtonGradient />
                <Section className='' customPosition='' customPaddings=''>
                    <div>
                        <div className='flex flex-grow flex-col items-center justify-center'>

                            {!showRecommendation && (
                                <section className=' mt-[1rem]  md:mt-[1.5rem]  lg:mt-[2rem]'>
                                    <UsecaseSelection onSelect={setUsecaseId} triggerShowRecommendation={triggerShowRecommendation} hideRecommendation={hideRecommendation} />
                                </section>
                            )}

                            {showRecommendation && (
                                <section className='mb-10'>
                                    <Recommendation usecaseId={usecaseId} statusFilter={statusFilter} topN={topN} triggerShowRec={triggerShowRecommendation} hideRec={hideRecommendation} />
                                </section>
                            )}

                            <section className='mb-10'>
                                <Filter onSelect={setStatusFilter} />
                            </section>

                        </div>
                    </div>
                </Section>

                <div className='absolute bottom-0 left-0 w-full'>
                    <Footer />
                </div>
            </div>

            <Data />
            <HowItWorks />
            <Footer />
        </>
    )
}

export default Main;