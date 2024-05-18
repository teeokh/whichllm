import React, { useState, useEffect } from 'react'
import axios from 'axios'

const Home = () => {
const[message, setMessage] = useState('Loading...')

useEffect(() => {
    const fetchMessage = async () => {
        try {
            const response = await axios.get('/home')
            setMessage(response.data.message)
        } catch (error) {
            setMessage('Error fetching the message.')
        }
    }

    fetchMessage()
}, []);

    return (
        <div>
            <h1>{message}</h1>
        </div>
    );
}
 
export default Home;