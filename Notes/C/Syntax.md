## Syntax
You have already seen the following code a couple of times in the first chapters. Let's break it down and understand what each part does:

Example
```
#include <stdio.h>

int main() {
  printf("Hello World!");
  return 0;
}
```

- `#include <stdio.h>` tells C to include a header file. This header lets us use input/output functions such as` printf()`.
- C ignores extra spaces and blank lines, but we use them to make the code easier to read.
- `main()` is a special function. Your program starts running here. Any code inside the curly brackets {} will be executed.

---

Comments:

Single Line Comments
```
// This is a comment
```
Multi-line Comments
```
/*
Hello this is multi-line comment
*/
```

---

Format Specifier:
- Format specifiers are used together with the printf() function to print variables.
- You can think of a format specifier as a placeholder that tells C what kind of value will be printed.
- A format specifier always starts with a percentage sign %, followed by a letter.

```
int myNum = 15;
printf("%d", myNum); // Outputs 15
```

---

The general rules for naming variables are:
- Names can contain letters, digits and underscores.
- Names must begin with a letter or an underscore.
- Names are case sensitive (myVar and MyVar both are different variable).
- Names cannot contain withspaces or special characters like !, #, %, etc.
- Reserved words cannot be used as th variable name
- All the variable must defined with unique names.
- These unique names are called identifiers.
- Identifiers can be short names (like x and y) or more descriptive names (age, sum, totalVolume).
Note: It is recommended to use descriptive names in order to create understandable and maintainable code.
---
























