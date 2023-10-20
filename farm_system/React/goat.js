import React, { useState, useEffect } from 'react';

function App() {
  const [goats, setGoats] = useState([]);
  const [newGoat, setNewGoat] = useState({
    animal_id: '',
    gender: '',
    weight: 0,
    dob: '',
    status: '',
    goat_condition: '',
    location: '',
  });

  useEffect(() => {
    fetch('http://localhost/backend.php')
      .then((response) => response.json())
      .then((data) => setGoats(data));
  }, []);

  const addGoat = () => {
    fetch('http://localhost/backend.php', {
      method: 'POST',
      body: JSON.stringify(newGoat),
    })
      .then(() => {
        setGoats([...goats, newGoat]);
        setNewGoat({
          animal_id: '',
          gender: '',
          weight: 0,
          dob: '',
          status: '',
          goat_condition: '',
          location: '',
        });
      })
      .catch((error) => console.error('Error:', error));
  };

  return (
    <div>
      <h1>Goat Management</h1>
      <div>
        <h2>Add a New Goat</h2>
        <div>
          <label>Animal ID:</label>
          <input
            type="text"
            value={newGoat.animal_id}
            onChange={(e) => setNewGoat({ ...newGoat, animal_id: e.target.value })}
          />
        </div>
        <div>
          <label>Gender:</label>
          <input
            type="text"
            value={newGoat.gender}
            onChange={(e) => setNewGoat({ ...newGoat, gender: e.target.value })}
          />
        </div>
        <div>
          <label>Weight:</label>
          <input
            type="number"
            value={newGoat.weight}
            onChange={(e) => setNewGoat({ ...newGoat, weight: e.target.value })}
          />
        </div>
        <div>
          <label>Date of Birth:</label>
          <input
            type="date"
            value={newGoat.dob}
            onChange={(e) => setNewGoat({ ...newGoat, dob: e.target.value })}
          />
        </div>
        <div>
          <label>Status:</label>
          <input
            type="text"
            value={newGoat.status}
            onChange={(e) => setNewGoat({ ...newGoat, status: e.target.value })}
          />
        </div>
        <div>
          <label>Goat Condition:</label>
          <input
            type="text"
            value={newGoat.goat_condition}
            onChange={(e) => setNewGoat({ ...newGoat, goat_condition: e.target.value })}
          />
        </div>
        <div>
          <label>Location:</label>
          <input
            type="text"
            value={newGoat.location}
            onChange={(e) => setNewGoat({ ...newGoat, location: e.target.value })}
          />
        </div>
        <button onClick={addGoat}>Add Goat</button>
      </div>
      <div>
        <h2>Goat List</h2>
        <ul>
          {goats.map((goat, index) => (
            <li key={index}>
              <strong>Animal ID:</strong> {goat.animal_id}, <strong>Gender:</strong> {goat.gender},
              <strong>Weight:</strong> {goat.weight}, <strong>DOB:</strong> {goat.dob},
              <strong>Status:</strong> {goat.status}, <strong>Condition:</strong> {goat.goat_condition},
              <strong>Location:</strong> {goat.location}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
