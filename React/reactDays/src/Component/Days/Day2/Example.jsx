const valide = () => <h1>You can go in party</h1>
const not_valid = () => <h1>You can't go in party</h1>

const check = (age) => {
    if (age >= 18) {
        return valide()
    } else return not_valid()
}

function Example({ age }) {
    return (
        <div>
            <h1>Example of Arrow Function</h1>
            <h2>Age: {age}</h2>
            {check(age)}
        </div>
    )
}

export default Example