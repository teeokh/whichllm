import React, { useState, useEffect } from 'react'
import axios from 'axios'

const Recommendation = () => {

    const [recommendation, setRecommendation] = useState()
    const [usecaseId, setUsecaseId] = useState(2); 
    const [statusFilter, setStatusFilter] = useState(null); 
    const [topN, setTopN] = useState(3); 
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchRecommendation = async() => {
            try {
                const response = await axios.get('/recommendations', {
                    params: {
                        usecase_id: usecaseId,
                        status_filter: statusFilter,
                        top_n: topN
                    }
                })
                setRecommendation(response.data.recommendations)
            } catch (error) {
                setError(error.response.data.message)
                console.log(error)
            }
        }

        if (usecaseId) {
            fetchRecommendation()
        }

    }, [usecaseId, statusFilter, topN]);

    return (
        <div>
            {error ? <p>{error}</p> : null}
            {recommendation && recommendation.length > 0 ? (
                <ul>
                    {recommendation.map(( {llm} ) => (
                        <li key={llm.id}>
                            <h3>{llm.name}</h3>
                            <p>Link: {llm.link}</p>
                            <p>Provider: {llm.provider}</p>
                        </li>
                    ))}
                </ul>
            ) : null}
        </div>
    );
}
 
export default Recommendation;