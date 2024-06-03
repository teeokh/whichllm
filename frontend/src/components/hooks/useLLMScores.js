import { useEffect, useState } from 'react'
import axios from 'axios'

const useLLMScores = () => {

    const [llmScores, setLlmScores] = useState([]);
    const [error, setError] = useState('')

    useEffect(() => {
        const fetchLLMScores = async () => {
            try {
                const response = await axios.get('/llm-scores');
                setLlmScores(response.data);
                console.log(llmScores)
            } catch (error) {
                setError(error.response?.data?.message || 'An error occurred');
                console.log(error);
            }
        };
        fetchLLMScores();
    }, [])
    return { llmScores, error };
}

export default useLLMScores