import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [tests, setTests] = useState([]);
  const [isLoading, setIsLoading] = useState(true); 

  useEffect(() => {
    fetch('/test')
      .then(response => response.json())
      .then(test => {
        setTests(test);
        setIsLoading(false)
        console.log(test)
      })
      .catch(err => console.err('Error:', err));
  }, []);
  
  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="App">
      <div>
        {tests.map(test => (
          <div key={test.id}>
            <p>ID: {test.id}</p>
            <p>Name: {test.name}</p>
            {test.notes !== null && <p>Notes: {test.notes}</p>}
            <p>Subject: {test.subject}</p>
            {test.useCases && test.useCases.length === 1 && <p>Usecase: {test.useCases}</p>} 
            {test.useCases && test.useCases.length > 1 && <p>Usecases: {test.useCases.join(', ')}</p>} 
            <p>-----</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
