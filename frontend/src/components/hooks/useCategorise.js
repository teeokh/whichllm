import { useState } from 'react'
import axios from 'axios'
const baseURL = process.env.REACT_APP_API_BASE_URL || '';

const useCategorise = (userInput) => {
    const [usecaseId, setUsecaseId] = useState('');
    const [usecaseName, setUsecaseName] = useState('');
    const [categoriseError, setCategoriseError] = useState('');
    const [loading, setLoading] = useState(false);

    const categoriseText = async (input) => {
        setLoading(true);
        try {
            const response = await axios.post(`${baseURL}/api/categorise`, { text: input })
            setUsecaseId(response.data.usecase_id);
            setUsecaseName(response.data.usecase_name)
            setCategoriseError('')
        } catch (error) {
            setCategoriseError(error.response?.data?.message || 'Error categorising text');
            setUsecaseId('')
            setUsecaseName('')
            console.log(error);
        } finally {
            setLoading(false);
        }
    }

    return { usecaseId, usecaseName, categoriseError, loading, categoriseText };
}

export default useCategorise
