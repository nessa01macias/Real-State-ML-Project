import React, { useState, useEffect } from 'react'

function App() {

  const [data, setData] = useState([{}])

  useEffect(
    () => {
      fetch("/get_locations").then(
        res => res.json()
      ).then(
        data => {
          setData(data)
          console.log(data)
        }
      )
    }, []);

  return (
    <div>
      {(typeof data.locations == 'undefined') ? (
        <p>Loading...</p>
      ) : (
        data.locations.map((location, i) => (
          <p key={i}>{location}</p>
        ))
      )}
    </div>
  );
}

export default App;
