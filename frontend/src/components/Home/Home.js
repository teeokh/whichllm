import React, { useState, useEffect } from 'react'
import axios from 'axios'
import {Link} from 'react-router-dom'

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
            <h1 className='App'>{message}</h1>
            <Link to='/main' className='App'>Main page</Link>
        </div>
    );
}
 
export default Home;