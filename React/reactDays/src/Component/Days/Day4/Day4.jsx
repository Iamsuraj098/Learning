import { useState } from 'react'

function Day4() {
    const [count, setCount] = useState(0);
    const update = () => {
        setCount(Math.random().toFixed(2) * 100);
    }
    console.log(count, setCount)
    return (
        <div>
            <h1>Day 4</h1>
            <h2>Counter: {count}</h2>
            <button onClick={update}>Incrment</button>
        </div>
    )
}

export default Day4