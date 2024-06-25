import { useState, useEffect } from 'react'
import axios from 'axios'
const baseURL = process.env.REACT_APP_API_BASE_URL || '';

const useBenchmarksUsecases = () => {
    const [benchmarksUsecases, setBenchmarksUsecases] = useState([])
    const [error, setError] = useState('')

    useEffect(() => {
        const fetchBenchmarksUsecases = async () => {
            try {
                const response = await axios.get(`${baseURL}/api/benchmarks-usecases`)
                setBenchmarksUsecases(response.data)

            } catch (error) {
                setError(error.response?.data?.message || 'An error occurred');
                console.log(error);
            }
        }
        fetchBenchmarksUsecases()
    }, []);


    return { benchmarksUsecases, error }
}

export default useBenchmarksUsecases
