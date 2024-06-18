import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Main from './components/Main.js'
import './index.css'

const App = () => {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/home" element={<Main />} />
          <Route path="/" element={<Main />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;