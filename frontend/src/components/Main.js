import React, { useState, useEffect } from 'react'
import Recommendation from './Recommendation.js'
import useRecommendation from './hooks/useRecommendation.js'
import useUsecaseName from './hooks/useUsecaseName.js'
import UsecaseBtn from './UsecaseBtn.js'
import useUsecases from './hooks/useUsecases.js'
import Filter from './Filter.js'
import Header from './Header.js'
import ButtonGradient from "../assets/svg/ButtonGradient";



const Main = () => {
    const [usecaseId, setUsecaseId] = useState(1);
    const [statusFilter, setStatusFilter] = useState(null);
    const [topN, setTopN] = useState(3);

    const { usecases, error } = useUsecases();
    const { recommendation, error: recError } = useRecommendation(usecaseId, statusFilter, topN);


    return (
        <>
            <div className="pt-[4.75rem] lg:pt-[5.25rem] overflow-hidden">
                <Header />
            </div>

            <ButtonGradient />
            <div className='flex flex-col justify-center items-center pt-[2rem] lg:pt-[4rem] '>
                <section className='mb-8'>
                    <UsecaseBtn onSelect={setUsecaseId} />
                </section>
                <section className='mb-10'>
                    <Recommendation usecaseId={usecaseId} statusFilter={statusFilter} topN={topN} />
                </section>
                <section>
                    <Filter onSelect={setStatusFilter} />
                </section>
            </div>
        </>
    )
}

export default Main;