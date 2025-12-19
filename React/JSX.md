**JSX (JavaScript XML)** is a **syntax extension for JavaScript** that allows you to write **HTML-like code** inside JavaScript files.

It makes UI code easier to read and write, but it is **not actual HTML** — before running in the browser, JSX is **transpiled (converted)** by tools like **Babel** into regular JavaScript calls such as `React.createElement()`.

In short:

> JSX is a developer-friendly way to describe UI structure in React using HTML-like syntax inside JavaScript.
---
### 1. **What You See in React Code**

You often write code like this:

```jsx
function App() {
  return <h1>Hello World</h1>;
}
```

It looks like **HTML** written inside **JavaScript**.

---

### 2. **What It Actually Is**

That syntax is **not HTML**. It is **JSX** (JavaScript XML) — a **special syntax extension** for JavaScript.
JSX is only a **developer convenience** that *resembles* HTML.

---

### 3. **What Happens Internally**

When you run your React app:

1. **Babel** (the compiler) converts JSX into **pure JavaScript**.
   Example:

   ```jsx
   <h1>Hello World</h1>
   ```

   becomes:

   ```js
   React.createElement("h1", null, "Hello World");
   ```
2. `React.createElement()` returns a **Virtual DOM object**, not an actual HTML element:

   ```js
   {
     type: "h1",
     props: { children: "Hello World" }
   }
   ```
3. React then uses this **Virtual DOM** to efficiently update the **Real DOM** (browser DOM).

---

### 4. **What the Browser Actually Sees**

The browser never sees JSX or HTML from your React code.
It only receives:

* JavaScript instructions from React, which create or update actual DOM nodes through the browser APIs.

---

### 5. **Why React Uses This Approach**

* It allows **UI and logic** to stay together inside one file (components).
* JSX provides **HTML-like readability**, while React handles **DOM manipulation** automatically.
* React can efficiently update the UI using **Virtual DOM diffing**, without manual DOM access.

---

### 6. **Summary Table**

| Concept                   | Description                                      |
| ------------------------- | ------------------------------------------------ |
| **HTML**                  | Real markup parsed directly by the browser       |
| **JSX**                   | JavaScript syntax extension that looks like HTML |
| **Transpilation**         | Babel converts JSX → `React.createElement()`     |
| **React.createElement()** | Creates Virtual DOM nodes (JS objects)           |
| **Virtual DOM**           | In-memory representation of UI                   |
| **Real DOM**              | Actual browser DOM rendered on screen            |

---

### 7. **Final Explanation**

> React does **not** allow you to write direct HTML inside JavaScript.
> You write **JSX**, which *looks like HTML* but is **converted into JavaScript code** that builds a **Virtual DOM tree**.
> React then uses that tree to create or update the **Real DOM** efficiently.

---
Why does React use different attribute names like className and camelCase style properties instead of regular HTML or CSS syntax?
```
In React, certain HTML attributes like `class` use different names 
(e.g., `className`) because JSX is converted into JavaScript, where some 
keywords or syntax could cause conflicts. JSX also follows JavaScript conventions, 
such as using camelCase for style properties.
```