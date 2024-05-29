import React, { useEffect, useState } from 'react'
import axios from 'axios'

const useBenchmark = (usecaseId, statusFilter, topN) => {

  const [benchmarkName, setBenchmarkName] = useState('');
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchBenchmark = async () => {
      try {
        const response = await axios.get('/recommendations');
        setBenchmarkName(response.data.benchmarks);
      } catch (error) {
        setError(error.response?.data?.message || 'An error occurred');
        console.log(error);
      }
    }

    fetchBenchmark();
  }, [usecaseId, statusFilter, topN])

  return { benchmarkName, error }
}

export default useBenchmark
