import React from 'react'
import Props from './Props';
import Example from './Example';

// Day2 Phase 1
// function Day2() {
//     const friend = "Friend";

//     function mul(a, b) {
//         return a * b;
//     }

//     const name = [
//         "John",
//         "Doe",
//         "Jane"
//     ]

//     const address = {
//         city: "New York",
//         state: "NY",
//         country: "USA"
//     }
//     const sub = (a, b) => { return a - b };
//     // wrong position of div tag or any tag.
//     return (
//         <div>
//             <h4>Day 2</h4>
//             <h4>{friend}</h4>
//             <h4>{2 + 2}</h4>
//             <h5>2*3 = {mul(2, 3)}</h5>
//             <h5>2-3 = {sub(2, 3)}</h5>
//             <h5>Names: {name.join(", ")}</h5>
//             <h5>Address: {address.city}, {address.country}</h5>
//             {/* to avoid line 31, we can also write like this */}
//             <h5>Address: {`${address.state}, ${address.country}`}</h5>
//         </div>
//     );
// }

// Day2 Phase 2

function Day2() {
    // we traversing the lists in JSX

    const friends = ["John", "Doe", "Jane", "Smith"];
    const students = [
        { name: "John", age: 20 },
        { name: "Doe", age: 22 },
        { name: "Jane", age: 21 }
    ]
    return (
        <div>
            {friends.map((friend) => (
                <ul>
                    <li>{friend}</li>
                </ul>
            ))}

            {students.map((student) => (
                <ul key={Math.random()}>
                    <li>{student.name} - {student.age}</li>
                </ul>
            ))}
            {/* we can also do by key names */}
            {students.map((student, index) => (
                <ul key={index}>
                    <li>{student.name}</li>
                    <li>{student.age}</li>
                </ul>
            ))}

            <h6>{students.map(student => student.name).join(", ")}</h6>

            {/* Props */}
            <Props name="Rahul" standerd="10th" age="15" />
            <User name="Raja" address="Simla" Age="101" married={false} />

            {/* Example */}
            <Example age="50"/>
        </div>

    );
}

function User(props) {
    return (
        <div>
            <h5>Inside the User</h5>
            <h6>Name: {props.name}</h6>
            <h6>Address: {props.address}</h6>
            <h6>Age: {props.Age}</h6>
            <h6>Married = {props.married ? "Yes" : "No"}</h6>
        </div>
    )
}
export default Day2