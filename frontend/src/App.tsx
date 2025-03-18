import { useState } from 'react'
import axios from 'axios';
import './App.css';

function App() {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);

  // Handle input change
  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  // Handle form submission (POST request)
  const handleSubmit = (e) => {
    e.preventDefault();

    axios.post('http://localhost:5000/api/hello', { text: input })
      .then((res) => {
        setResponse(res.data);
        setInput(''); // Clear input after successful submission
      })
      .catch((err) => {
        setError(err);
      });
  };

  return (
    <>
      <h1>LLM Viewer</h1>
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          value={input} 
          onChange={handleInputChange} 
          placeholder="Enter text" 
        />
        <button type="submit">Submit</button>
        <p>{JSON.stringify(response)}</p>
      </form>
    </>
  )
}

export default App
