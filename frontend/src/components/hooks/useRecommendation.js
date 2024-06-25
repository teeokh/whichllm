import { useState, useEffect } from 'react';
import axios from 'axios';
const baseURL = process.env.BACKEND_API_BASE_URL || '';

const useRecommendation = (usecaseId, statusFilter, topN) => {
    const [recommendation, setRecommendation] = useState([]);
    const [benchmarks, setBenchmarks] = useState([]);
    const [error, setError] = useState('');

    // Fetch recommendations based on usecase, filter and number of recs
    useEffect(() => {
        const fetchRecommendation = async () => {

            try {
                const response = await axios.get(`${baseURL}/api/recommendations`, {
                    params: {
                        usecase_id: usecaseId,
                        status_filter: statusFilter,
                        top_n: topN
                    }
                });
                setRecommendation(response.data.recommendations || []);
                setBenchmarks(response.data.benchmarks || []);
                setError('');
            } catch (error) {
                setError(error.response?.data?.message || 'An error occurred');
                setRecommendation([])
                setBenchmarks([])
            }

        };

        fetchRecommendation();
    }, [usecaseId, statusFilter, topN]);

    return ({ recommendation, benchmarks, error });
};

export default useRecommendation;
