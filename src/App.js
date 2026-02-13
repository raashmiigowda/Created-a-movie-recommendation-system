import React, { useEffect, useState } from "react";

function App() {
  const [movies, setMovies] = useState([]);
  const [selected, setSelected] = useState("");
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/movies")
      .then(res => res.json())
      .then(data => setMovies(data));
  }, []);

  const getRecommendations = () => {
    fetch("http://localhost:5000/recommend", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ movie: selected })
    })
      .then(res => res.json())
      .then(data => setRecommendations(data));
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>🎬 Movie Recommender</h1>

      <select onChange={(e) => setSelected(e.target.value)}>
        <option>Select Movie</option>
        {movies.map((movie, index) => (
          <option key={index}>{movie}</option>
        ))}
      </select>

      <button onClick={getRecommendations}>Recommend</button>

      <h2>Recommended Movies</h2>
      <ul>
        {recommendations.map((movie, index) => (
          <li key={index}>{movie}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
