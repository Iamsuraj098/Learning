### Rules of JSX (Refer - Day2.jsx)
#### JSX Rules

- **Return a Single Parent Element:**  
    JSX elements must be wrapped in a single parent element.

    **Incorrect Example:**
    ```jsx
    // This will cause an error
    return (
        <h1>Java</h1>
        <h1>JavaScript</h1>
    );
    ```

    **Correct Example:**
    ```jsx
    return (
        <h1>Java</h1>
    );
    ```

- **Closing Tags Required:**  
    All tags must be properly closed, e.g., `<h1 />` or `<h1></h1>`.  
    Incorrect: `<h1>`

- **Attribute Naming Differences:**  
    - Use `className` instead of `class`.
    - Use `htmlFor` instead of `for` in `<label>` tags.
    - These changes avoid conflicts with JavaScript keywords and ensure valid syntax.

- **Curly Braces for Expressions:**  
    Use curly braces `{}` to embed JavaScript expressions or variables inside JSX.  
    Example: `{2 + 2}`

- **List Traversal in React:**  
    When rendering lists, each element should have a unique `key` prop to avoid errors and manage state efficiently.

### Props
