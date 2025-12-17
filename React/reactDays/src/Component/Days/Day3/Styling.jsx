import React from 'react'

function Styling() {
  const styles = {
    color: 'blue',
    fontSize: '20px',
    backgroundColor: 'Green',
    padding: '10px',
    borderRadius: '10px',
  };
  return (
    <div>
      <div>
        <h1 style={styles}>Styling</h1>
      </div>

      <div>
        <p style={{ color: 'red', fontSize: '18px', backgroundColor: 'black', padding: '10px', borderRadius: '5px' }}>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Expedita consequatur, autem magni recusandae ut nam ab sequi. Molestiae, suscipit repellat doloremque culpa eveniet perferendis quaerat nulla, itaque reprehenderit quisquam minus.
        </p>
      </div>
    </div>
  )
}

export default Styling