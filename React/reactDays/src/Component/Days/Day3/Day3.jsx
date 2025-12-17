import Styling from "./Styling"
const nice_day = () => {return <h1>It's a nice day</h1>}
const hot_day = () => {return <h1>It's a hot day</h1>}
const cold_day = () => {return <h1>It's a cold day</h1>}
function Day3() {
    const temp = 25;

    const weather = (temp) => {
        if (temp > 30) {
            return nice_day()
        } else if (temp > 20) {
            return hot_day()
        } else {
            return cold_day()
        }
    }

    return (
        <div>
            <h4>Today Weather</h4>
            <h5>Today Temp: {temp} and status: {weather(temp)}</h5>
            <Styling />
        </div>
    );
}

export default Day3