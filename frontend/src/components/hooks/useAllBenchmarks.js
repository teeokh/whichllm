import { useEffect, useState } from 'react'
import axios from 'axios'
const baseURL = process.env.REACT_APP_API_BASE_URL || '';

const useAllBenchmarks = () => {

  const [allBenchmarks, setAllBenchmarks] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchBenchmarks = async () => {
      try {
        const response = await axios.get(`${baseURL}/api/benchmarks`);
        setAllBenchmarks(response.data);
      } catch (error) {
        setError(error.response?.data?.message || 'An error occurred');
      }
    }

    fetchBenchmarks();
  }, [])

  return { allBenchmarks, error }
}

export default useAllBenchmarks
