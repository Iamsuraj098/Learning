### Before moving to the Execution of a Python Program, let’s learn about Compiler-based and Interpreter-based languages

#### **Compiled Language**

* **What is a Compiler?**

  * **Definition**: Translates the **entire source code** into machine code (an executable) at once.
* **Execution**: The compiled executable runs directly on the CPU.
* **Speed**: Execution is **fast**, because the program is already translated before running.
* **Error Detection**: Errors are detected at **compile-time** (before execution).
* **Memory Usage**: Requires more memory for the generated executable.
* **Examples**: C (GCC), C++ (Clang), Go, Rust.

---

#### **Interpreted Language**

* **What is an Interpreter?**

  * **Definition**: Executes the source code **line by line** at runtime.
* **Execution**: The interpreter translates and runs code on the fly.
* **Speed**: Usually **slower**, since translation happens during execution.
* **Error Detection**: Errors appear **at runtime**, when the faulty line is reached.
* **Portability**: Generally more **portable**, since the interpreter handles platform differences.
* **Examples**: Python, JavaScript, Ruby, PHP.

---

#### **Note — Java combines both approaches**

* Uses a **compiler (`javac`)** → generates Bytecode.
* Then a **JVM (with Interpreter + JIT compiler)** → executes Bytecode efficiently.

---

### Execution of a Python Program

Python is an **interpreted language**, but it also involves a **compilation step** internally.

Example code:

```python
print("Hello World")
```

Suppose the above program is saved as `first.py`.
The execution involves **two main steps**:

1. **Compilation (to Bytecode)**
2. **Interpretation (by PVM)**

---

#### **1. Compilation**

* Python first compiles the `.py` file into **Bytecode**.
* Bytecode is a **low-level, platform-independent set of instructions** (not the same as machine code).
* This Bytecode is usually stored in a `.pyc` file inside the `__pycache__` folder.
* The `.pyc` file is generated **automatically by Python** when a module is **imported**.

  * If you just run a single script (without importing it elsewhere), Python may not leave behind a `.pyc` file, though it still compiles internally in memory.

 **Important Notes**

* `.pyc` = Compiled Python file (sometimes referred to as “frozen binaries”).
* The use of the word **compiler** here doesn’t mean Python is a compiled language — it’s just part of the execution pipeline.
* If you modify `hello.py` later and rerun it, Python will **recompile the entire file** and generate a **new `.pyc` file**. It does not partially reuse old bytecode.

---

#### **2. Interpretation**

* The **Python Virtual Machine (PVM)** takes the Bytecode (`.pyc`) and **executes it**.
* PVM translates Bytecode into **machine code**, which is understood by the CPU.
* This is done **line by line**, which makes Python relatively slower compared to compiled languages.

 **JIT Compiler**

* Some Python implementations (like **PyPy**) use a **Just-In-Time (JIT) compiler** inside the PVM.
* JIT compiles frequently executed parts of code into native machine code at runtime, improving performance.
* The standard **CPython** (most widely used Python) does **not include JIT** by default.

---

**Example**

* **C (compiled)**
* **Python (interpreted)**
* **Java (hybrid)**