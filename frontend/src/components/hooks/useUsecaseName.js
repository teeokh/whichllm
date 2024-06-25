import { useState, useEffect } from 'react';
import axios from 'axios';
const baseURL = process.env.REACT_APP_API_BASE_URL || '';

const useUsecaseName = (usecaseId) => {
    const [usecaseName, setUsecaseName] = useState('');
    const [error, setError] = useState('');

    // Fetch name of usecase based on usecase ID
    useEffect(() => {
        const fetchUsecaseName = async () => {
            try {
                const response = await axios.get(`${baseURL}/api/usecase/${usecaseId}`);
                setUsecaseName(response.data.name);
            } catch (error) {
                setError(error.response?.data?.message || 'An error occurred');
                console.log(error);
            }
        };

        fetchUsecaseName();
    }, [usecaseId]);

    return { usecaseName, error };
};

export default useUsecaseName;
