import React, {useState, useEffect } from 'react'
import Recommendation from '../Recommendation/Recommendation.js'
import useRecommendation from '../hooks/useRecommendation.js'
import useUsecaseName from '../hooks/useUsecaseName.js'
import UsecaseBtn from '../Usecase/UsecaseBtn.js'
import Filter from '../Filter/Filter.js'

const Main = () => {
    const [usecaseId, setUsecaseId] = useState(1);
    const [statusFilter, setStatusFilter] = useState(null);
    const [topN, setTopN] = useState(3);

    return (
        <>
            <UsecaseBtn onSelect={setUsecaseId}/>
            <Recommendation usecaseId={usecaseId} statusFilter={statusFilter} topN={topN}/>
            <Filter onSelect={setStatusFilter} />
        </>
    );
}

export default Main;