import { useEffect, useState } from 'react'
import axios from 'axios'
const baseURL = process.env.BACKEND_API_BASE_URL || '';

const useLLMScores = () => {

    const [llmScores, setLlmScores] = useState([]);
    const [error, setError] = useState('')

    useEffect(() => {
        const fetchLLMScores = async () => {
            try {
                const response = await axios.get(`${baseURL}/api/llm-scores`);
                setLlmScores(response.data);
            } catch (error) {
                setError(error.response?.data?.message || 'An error occurred');
            }
        };
        fetchLLMScores();
    }, [])
    return { llmScores, error };
}

export default useLLMScores
