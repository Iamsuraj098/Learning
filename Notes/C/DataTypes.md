In **C language**, data types define what kind of data a variable can store and how much memory it will occupy.

They are broadly classified into the following categories:

---

### 1. Basic (Primary) Data Types

These are the fundamental building blocks.

#### a) **int**

* Used to store integers (whole numbers)
* Example: `10, -5, 1000`
* Typically 4 bytes

#### b) **float**

* Used for single-precision decimal numbers
* Example: `3.14, 2.5`
* Typically 4 bytes

#### c) **double**

* Used for double-precision floating-point numbers (more accurate than float)
* Example: `3.1415926535`
* Typically 8 bytes

#### d) **char**

* Used to store a single character
* Example: `'a', 'Z', '1'`
* Typically 1 byte

---

# 2. Derived Data Types

These are formed from basic data types.

#### a) Array

* Collection of elements of the same type
* Example: `int arr[5];`

#### b) Pointer

* Stores the address of another variable
* Example: `int *ptr;`

#### c) Function

* Functions returning values of specific types
* Example: `int func();`

---

# 3. User-Defined Data Types

Created by the programmer.

#### a) **struct**

* Groups different data types under one name
* Example: student record

#### b) **union**

* Similar to struct, but shares memory among members

#### c) **enum**

* Assigns names to integer constants
* Example: `enum days {MON, TUE, WED};`

#### d) **typedef**

* Creates an alias (new name) for existing data types

---

# 4. Void Data Type

#### **void**

* Represents no value
* Used in:

  * Functions that return nothing: **void func()**
  * Generic pointers: **void *ptr**

---

# 5. Type Modifiers

Used to modify basic data types.

* **short**
* **long**
* **signed**
* **unsigned`

Example:

```c
unsigned int x;
long double y;
```

---

# Summary

* **Basic** → `int`, `float`, `double`, `char`
* **Derived** → arrays, pointers, functions
* **User-defined** → struct, union, enum, typedef
* **Void** → no value
* **Modifiers** → change size/range

---

#### Difference between signed and unsigned bits:

##### Signed
- Can store both positive and negative values
- Uses one bit for the sign (positive/negative)
##### Unsigned
- Can store only non-negative values (0 and positive)
- Uses all bits for the value
```
signed int a = -10;
unsigned int b = 10;
```

| Feature         | Signed  | Unsigned               |
| --------------- | ------- | ---------------------- |
| Negative values | Yes     | No                     |
| Zero            | Yes     | Yes                    |
| Positive values | Yes     | Yes                    |
| Range           | Smaller | Larger (only positive) |

---

### Type Conversion
There are two types of conversion in C:

Implicit Conversion (automatically)
Explicit Conversion (manually)

#### Implicit Conversion
Implicit conversion is done automatically by the compiler when you assign a value of one type to another.

#### Explicit Conversion
Explicit conversion is done manually by placing the type in parentheses () in front of the value.

---



















































