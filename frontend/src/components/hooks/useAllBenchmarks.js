import React, { useEffect, useState } from 'react'
import axios from 'axios'

const useAllBenchmarks = () => {

  const [allBenchmarks, setAllBenchmarks] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchBenchmarks = async () => {
      try {
        const response = await axios.get('/benchmarks');
        setAllBenchmarks(response.data);
        console.log(allBenchmarks)
      } catch (error) {
        setError(error.response?.data?.message || 'An error occurred');
        console.log(error);
      }
    }

    fetchBenchmarks();
  }, [])

  return { allBenchmarks, error }
}

export default useAllBenchmarks
