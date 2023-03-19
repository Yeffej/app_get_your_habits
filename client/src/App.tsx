import React, { useState, useEffect } from 'react'
import { BASE_API } from './config'

import './App.css';

function App() {
  const [habits, setHabits] = useState({})

  useEffect(() => {
    window.fetch(`${BASE_API}/habits`)
    .then((res) => res.json())
    .then(console.log)
  }, [])

  return (
    <div className="App">
      <h1>Hello REACT-FLASK</h1>
    </div>
  );
}

export default App
