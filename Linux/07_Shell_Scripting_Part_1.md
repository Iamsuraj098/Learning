## Chapter 07: Shell Scripting.
Shell scripting is one of the most powerful skills in Linux because it allows we to automate repetitive tasks, manage systems, process files, and build complete automation workflows

Topics We Will Cover

| No. | Topic                           | Description                                            |
| --- | ------------------------------- | ------------------------------------------------------ |
| 1   | Introduction to Shell Scripting | What shell scripts are and why they are useful         |
| 2   | Creating wer First Script      | Writing and running a `.sh` file                       |
| 3   | Shebang (`#!`)                  | Specifying which interpreter should execute the script |
| 4   | Variables                       | Storing and using data                                 |
| 5   | User Input                      | Reading input from users                               |
| 6   | Command-Line Arguments          | Passing values while running scripts                   |
| 7   | Arithmetic Operations           | Performing calculations                                |
| 8   | Conditional Statements          | `if`, `elif`, `else`                                   |
| 9   | Comparison Operators            | Numeric and string comparisons                         |
| 10  | Loops                           | `for`, `while`, `until`                                |
| 11  | `case` Statement                | Multiple-choice decision making                        |
| 12  | Functions                       | Reusable blocks of code                                |
| 13  | Arrays                          | Storing multiple values                                |
| 14  | File Testing                    | Checking whether files/directories exist               |
| 15  | Exit Status                     | Understanding success and failure codes                |
| 16  | Redirection in Scripts          | Input/output redirection                               |
| 17  | Debugging Scripts               | Finding and fixing errors                              |
| 18  | Scheduling Scripts              | Using `cron` and `systemd timers`                      |


---

### 1. Introduction to Shell Scripting
A shell scripting is the simple text file that contains the linux commands.

Instead of typing commands one by one.
```
date
pwd
whoami
```
We can put them into a file
```
#!/bin/bash
date
pwd
whoami
```
and then all at once.
##### Why Use Shell Scripts?

| Use Case              | Example                         |
| --------------------- | ------------------------------- |
| Automation            | Backup files automatically      |
| System Administration | Create users, monitor services  |
| Repetitive Tasks      | Rename hundreds of files        |
| Monitoring            | Check disk or CPU usage         |
| Deployment            | Start applications and services |
| Scheduling            | Run jobs every day using cron   |

---

### 2. Our First Shell scripts
How linux execute scripts ?

```
#!
```
This line is called the `Shebang`(or hashbang).

`What is a Shebang?`

A shebang tells Linux which interpreter should execute the script.

General Syntax 
```
#!path_to_interpreter
```
Examples:

| Shebang               | Interpreter                   |
| --------------------- | ----------------------------- |
| `#!/bin/bash`         | Bash shell                    |
| `#!/bin/sh`           | POSIX shell                   |
| `#!/usr/bin/python3`  | Python                        |
| `#!/usr/bin/perl`     | Perl                          |
| `#!/usr/bin/env bash` | Finds Bash in the system PATH |

---
---

## 3. What is a Shebang?

A shebang tells Linux **which interpreter should execute the script**.

General syntax:

```bash
#!path_to_interpreter
```

Examples:

| Shebang               | Interpreter                   |
| --------------------- | ----------------------------- |
| `#!/bin/bash`         | Bash shell                    |
| `#!/bin/sh`           | POSIX shell                   |
| `#!/usr/bin/python3`  | Python                        |
| `#!/usr/bin/perl`     | Perl                          |
| `#!/usr/bin/env bash` | Finds Bash in the system PATH |

---

## Why is Shebang Important?

Suppose we have a script:

```bash
#!/bin/bash

echo "Hello from Bash"
```

When we run:

```bash
./script.sh
```

Linux:

1. Opens the file.

2. Reads the first line.

3. Sees:

   ```bash
   #!/bin/bash
   ```

4. Starts `/bin/bash`.

5. Passes the script file to Bash.

Effectively Linux runs:

```bash
/bin/bash script.sh
```

---

## What Happens If No Shebang Exists?

Example:

```bash
echo "Hello"
```

If we execute it like:

```bash
./script.sh
```

Behavior may vary depending on wer shell and system.

To avoid unexpected behavior, always include a shebang.

we can still explicitly specify the interpreter:

```bash
bash script.sh
```

In this case, Bash executes the script regardless of whether a shebang exists.

---

## Common Shebang Styles

### Direct path

```bash
#!/bin/bash
```

Advantages:

* Fast
* Explicit

Disadvantages:

* Bash may be installed in a different location on some systems.

---

### Using `env`

```bash
#!/usr/bin/env bash
```

Advantages:

* Portable across different Linux distributions and Unix systems.
* Searches for `bash` in the user's `PATH`.

Linux internally does something similar to:

```bash
env bash script.sh
```

This is commonly used in open-source projects.

---

## How to Find an Interpreter

Use:

```bash
which bash
```

Output:

```bash
/usr/bin/bash
```

Or:

```bash
type -a bash
```

Example:

```bash
$ type -a bash
bash is /usr/bin/bash
bash is /bin/bash
```

---

## Making a Script Executable

A script must have execute permission:

```bash
chmod +x script.sh
```

Check permissions:

```bash
ls -l script.sh
```

Example:

```bash
-rwxr-xr-x 1 suraj suraj 45 Jun 28 12:00 script.sh
```

The `x` means executable.

---

## How Linux Executes `./script.sh`

When we run:

```bash
./script.sh
```

The shell asks the kernel to execute the file.

The kernel:

1. Checks execute permission.
2. Reads the first bytes of the file.
3. If it starts with `#!`, the kernel launches the specified interpreter.
4. The interpreter reads and executes the remaining commands.

Flow:

```text
User
  │
  ▼
./script.sh
  │
  ▼
Shell
  │
  ▼
Linux Kernel
  │
  ▼
Reads #! /bin/bash
  │
  ▼
Starts Bash
  │
  ▼
Bash executes commands
```

---

## Practice Lab

Create a file:

```bash
nano test.sh
```

Add:

```bash
#!/bin/bash

echo "Interpreter Path: $BASH"
echo "Shell Version: $BASH_VERSION"
echo "Current User: $(whoami)"
```

Make it executable:

```bash
chmod +x test.sh
```

Run it:

```bash
./test.sh
```

---

## Experiment

Create another file **without** a shebang:

```bash
nano noshebang.sh
```

Contents:

```bash
echo "Hello from script without shebang"
```

Make it executable:

```bash
chmod +x noshebang.sh
```

Run:

```bash
./noshebang.sh
```

Observe what happens on our system.

---

## Key Takeaways

| Concept               | Meaning                               |
| --------------------- | ------------------------------------- |
| `#!`                  | Shebang line                          |
| `/bin/bash`           | Bash interpreter                      |
| `chmod +x`            | Makes script executable               |
| `./script.sh`         | Executes script directly              |
| `bash script.sh`      | Executes script using Bash explicitly |
| `#!/usr/bin/env bash` | Portable Bash shebang                 |


---
---
### 4. Variable in Shell Scripting

Variables allow us to store data and reuse it throughout your scripts.
```
NAME  ───► "Joker"
AGE   ───► 20
CITY  ───► "Delhi"
```

##### Creating Variable
Syntax: `VARIABLE_NAME=value`

Important: Do not put spaces around `=`

##### Accessin Variable

Use the `$` symbol to access a variable's value.

Examples:
```
#!/bin/bash
NAME=Suraj
echo $NAME
```
or we can also write ``` echo "$NAME"```

##### Why use Curly Braces ${}?
Sometimes Bash cannot determine where the variable name ends.

Examples
```
FILE=data
echo "$FILE.txt"
```
Bash searches for a variable named FILE.txt, which does not exist.
Correct way: ```echo "${FILE}.txt"``` Output`data.txt`

##### Unset the Variable
Remove a Variable

```
NAME=Kimi
echo $NAME

unset NAME

echo $NAME
```
After `unset`, the variable becomes empty.

##### Read-Only Varaibles
To prevent modification
``` 
readonly PI=3.14

echo $PI
```
Trying to change it.
`PI=4`

##### Environment Varaibles
Linux Define many predefined variables.
``` env	```

Common environment variables:

| Variable    | Description                       |
| ----------- | --------------------------------- |
| `$HOME`     | User's home directory             |
| `$USER`     | Current username                  |
| `$PWD`      | Current working directory         |
| `$PATH`     | Directories searched for commands |
| `$SHELL`    | Current shell                     |
| `$HOSTNAME` | System hostname                   |
| `$TERM`     | Terminal type                     |

Examples:
```
echo $HOME
echo $USER
echo $PWD
echo $PATH
echo $SHELL
```

##### Variable Naming Rules

| Rule                             | Example                         |
| -------------------------------- | ------------------------------- |
| Can contain letters, digits, `_` | `USER_NAME`                     |
| Cannot start with a digit        | `1USER` ❌                       |
| No spaces allowed                | `USER NAME` ❌                   |
| Case-sensitive                   | `name` and `NAME` are different |

```
USERNAME=suraj
userName=admin
USER_NAME=linux
```

























































