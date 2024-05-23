import React, { useState, useEffect } from 'react'
import Recommendation from './Recommendation.js'
import useRecommendation from './hooks/useRecommendation.js'
import useUsecaseName from './hooks/useUsecaseName.js'
import UsecaseBtn from './UsecaseBtn.js'
import useUsecases from './hooks/useUsecases.js'
import Filter from './Filter.js'
import Test from '../Test.js'


const Main = () => {
    const [usecaseId, setUsecaseId] = useState(1);
    const [statusFilter, setStatusFilter] = useState(null);
    const [topN, setTopN] = useState(3);

    const { usecases, error } = useUsecases();
    const { recommendation, error: recError } = useRecommendation(usecaseId, statusFilter, topN);

    if (!recommendation.length || !usecases.length) {
        return <p className='flex justify-center items-center min-h-screen'>Loading...</p>;
    }

    return (
        <div className='flex flex-col justify-center items-center min-h-screen'>
            <div className='mb-8'>
                <UsecaseBtn onSelect={setUsecaseId} />
            </div>
            <div className='mb-8'>
                <Recommendation usecaseId={usecaseId} statusFilter={statusFilter} topN={topN} />
            </div>
            <div>
                <Filter onSelect={setStatusFilter} />
                {/* <Test /> */}
            </div>
        </div>
    );
}

export default Main;