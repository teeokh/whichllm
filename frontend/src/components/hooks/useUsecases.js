import { useState, useEffect } from 'react';
import axios from 'axios';
const baseURL = process.env.BACKEND_API_BASE_URL || '';

const useUsecases = () => {
    const [usecases, setUsecases] = useState([]);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchUsecases = async () => {
            try {
                const response = await axios.get(`${baseURL}/api/usecases`)
                setUsecases(response.data);
            } catch (error) {
                setError(error.response?.data?.message || 'An error occurred');
                console.log(`${baseURL}/api/usecases`)
                console.log(error);
            }
        };

        fetchUsecases();
    }, []);

    return { usecases, error };
};

export default useUsecases;