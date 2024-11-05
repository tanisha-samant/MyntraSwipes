import React, { useState } from 'react';
import TinderCard from 'react-tinder-card';
import axios from 'axios';
import '/workspaces/myntra-swipes/myntra-swipes-demo-frontend/src/App.css';

const outfits = [
  { id: 1, name: 'Outfit 1', image_url: 'https://link.to/outfit1.jpg' },
  { id: 2, name: 'Outfit 2', image_url: 'https://link.to/outfit2.jpg' },
  { id: 3, name: 'Outfit 3', image_url: 'https://link.to/outfit3.jpg' },
  { id: 4, name: 'Outfit 4', image_url: 'https://link.to/outfit4.jpg' },
  { id: 5, name: 'Outfit 5', image_url: 'https://link.to/outfit5.jpg' },
  { id: 6, name: 'Outfit 6', image_url: 'https://link.to/outfit6.jpg' },
];

function App() {
  const [lastDirection, setLastDirection] = useState();

  const swiped = (direction, outfit) => {
    setLastDirection(direction);
    axios.post('http://localhost:5000/api/recommendations', {
      outfit_id: outfit.id,
      direction: direction,
    })
    .then(response => {
      console.log(response.data);
    })
    .catch(error => {
      console.error('There was an error sending the swipe data!', error);
    });
  };

  return (
    <div className="app">
      <h1>MyntraSwipes Demo</h1>
      <div className="card-container">
        {outfits.map((outfit) => (
          <TinderCard
            key={outfit.id}
            onSwipe={(dir) => swiped(dir, outfit)}
            preventSwipe={['up', 'down']}
          >
            <div className="card">
              <img src={outfit.image_url} alt={outfit.name} />
              <h3>{outfit.name}</h3>
            </div>
          </TinderCard>
        ))}
      </div>
      {lastDirection ? <h2>You swiped {lastDirection}</h2> : <h2>Swipe a card!</h2>}
    </div>
  );
}

export default App;
