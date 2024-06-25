import { useState, useEffect } from 'react';
import axios from 'axios';

const useUsecases = () => {
    const [usecases, setUsecases] = useState([]);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchUsecases = async () => {
            try {
                const response = await axios.get(`${process.env.BACKEND_API_BASE_URL}/api/usecases`)
                setUsecases(response.data);
            } catch (error) {
                setError(error.response?.data?.message || 'An error occurred');
                console.log(`${process.env.BACKEND_API_BASE_URL}/api/usecases`)
                console.log(error);
            }
        };

        fetchUsecases();
    }, []);

    return { usecases, error };
};

export default useUsecases;