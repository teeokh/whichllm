import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home/Home.js'
import Main from './components/Main/Main.js'
import './index.css'

const App = () => {
  return (  
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/main" element={<Main />} />
        </Routes>
      </div>
    </Router>
  );
}
 
export default App;