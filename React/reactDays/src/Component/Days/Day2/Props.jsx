import React from 'react'

// function Props({ name, standerd, age }) {
//   return (
//     <div>
//       <h6>Name: {name}</h6>
//       <h6>Class: {standerd}</h6>
//       <h6>Age: {age}</h6>
//     </div>
//   )
// }

function Props(props) {
  return (
    <div>
      <h5>Inside the Props</h5>
      <h6>Name: {props.name}</h6>
      <h6>Class: {props.standerd}</h6>
      <h6>Age: {props.age}</h6>
    </div>
  )
}

export default Props