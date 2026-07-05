# Chapter 02: Linux Commands

## 1. Command Syntax

Most Linux commands follow this structure:

```bash
command [options] [arguments]
```

Example:

```bash
ls -l /home
```

| Part    | Meaning                      |
| ------- | ---------------------------- |
| `ls`    | Command                      |
| `-l`    | Option (long listing format) |
| `/home` | Argument (target directory)  |

---

## 2. Essential Navigation Commands

| Command | Description                           | Example        |
| ------- | ------------------------------------- | -------------- |
| `pwd`   | Print current working directory       | `pwd`          |
| `ls`    | List files and directories            | `ls`           |
| `cd`    | Change directory                      | `cd Documents` |
| `tree`  | Display directory structure as a tree | `tree`         |

---

## 3. File and Directory Management

| Command | Description              | Example              |
| ------- | ------------------------ | -------------------- |
| `touch` | Create an empty file     | `touch file.txt`     |
| `mkdir` | Create directory         | `mkdir project`      |
| `rmdir` | Remove empty directory   | `rmdir test`         |
| `rm`    | Remove files/directories | `rm file.txt`        |
| `cp`    | Copy files/directories   | `cp a.txt b.txt`     |
| `mv`    | Move or rename files     | `mv old.txt new.txt` |

---

## 4. Viewing File Contents

| Command | Description                    | Example         |
| ------- | ------------------------------ | --------------- |
| `cat`   | Display entire file            | `cat notes.txt` |
| `less`  | View file page by page         | `less log.txt`  |
| `more`  | Simple paginated viewer        | `more file.txt` |
| `head`  | Show first lines               | `head file.txt` |
| `tail`  | Show last lines                | `tail file.txt` |
| `nl`    | Display file with line numbers | `nl file.txt`   |

---

## 5. Searching Commands

| Command   | Description                     | Example                |
| --------- | ------------------------------- | ---------------------- |
| `find`    | Search files/directories        | `find . -name "*.txt"` |
| `locate`  | Quickly locate files            | `locate config.txt`    |
| `grep`    | Search text patterns            | `grep "error" app.log` |
| `which`   | Show command location           | `which python`         |
| `whereis` | Locate binary, source, man page | `whereis bash`         |

---

## 6. Text Processing Commands

| Command | Description                  | Example                   |
| ------- | ---------------------------- | ------------------------- |
| `echo`  | Print text                   | `echo "Hello"`            |
| `sort`  | Sort lines                   | `sort names.txt`          |
| `uniq`  | Remove duplicate lines       | `uniq file.txt`           |
| `wc`    | Count lines/words/characters | `wc file.txt`             |
| `cut`   | Extract columns              | `cut -d: -f1 /etc/passwd` |
| `tr`    | Translate characters         | `echo hi \| tr a-z A-Z`   |

---

## 7. Help Commands

| Command  | Description                  | Example       |
| -------- | ---------------------------- | ------------- |
| `man`    | Manual pages                 | `man ls`      |
| `info`   | Detailed documentation       | `info ls`     |
| `--help` | Quick help                   | `ls --help`   |
| `whatis` | One-line command description | `whatis grep` |

---

# Suggested Practical Lab

Open your terminal and perform these tasks:

```bash
# Check current directory
pwd

# Create practice directory
mkdir linux_lab

# Move into it
cd linux_lab

# Create files
touch file1.txt file2.txt

# List files
ls -l

# Copy a file
cp file1.txt backup.txt

# Rename file
mv file2.txt notes.txt

# View files
cat notes.txt

# Search file
find . -name "*.txt"

# Remove files
rm backup.txt
```

---
---

# Linux Commands Reference Table

| Command   | Full Form                       | Description                                                            | Example                       |
| --------- | ------------------------------- | ---------------------------------------------------------------------- | ----------------------------- |
| `pwd`     | Print Working Directory         | Displays the current directory path.                                   | `pwd`                         |
| `ls`      | List                            | Lists files and directories.                                           | `ls -l`                       |
| `cd`      | Change Directory                | Changes the current directory.                                         | `cd Documents`                |
| `tree`    | Tree                            | Displays directories in a tree-like structure.                         | `tree`                        |
| `touch`   | Touch                           | Creates empty files or updates file timestamps.                        | `touch file.txt`              |
| `mkdir`   | Make Directory                  | Creates new directories.                                               | `mkdir project`               |
| `rmdir`   | Remove Directory                | Removes empty directories.                                             | `rmdir test`                  |
| `rm`      | Remove                          | Deletes files and directories.                                         | `rm file.txt`                 |
| `cp`      | Copy                            | Copies files and directories.                                          | `cp file1.txt backup.txt`     |
| `mv`      | Move                            | Moves or renames files and directories.                                | `mv old.txt new.txt`          |
| `cat`     | Concatenate                     | Displays or combines file contents.                                    | `cat notes.txt`               |
| `less`    | Less                            | Views file contents page by page with backward and forward navigation. | `less log.txt`                |
| `more`    | More                            | Displays file contents one screen at a time.                           | `more file.txt`               |
| `head`    | Head                            | Displays the first few lines of a file (default: 10).                  | `head file.txt`               |
| `tail`    | Tail                            | Displays the last few lines of a file (default: 10).                   | `tail file.txt`               |
| `nl`      | Number Lines                    | Displays file contents with line numbers.                              | `nl file.txt`                 |
| `find`    | Find                            | Searches for files and directories recursively.                        | `find . -name "*.txt"`        |
| `locate`  | Locate                          | Quickly finds files using a database.                                  | `locate config.txt`           |
| `grep`    | Global Regular Expression Print | Searches text using patterns.                                          | `grep "error" app.log`        |
| `which`   | Which                           | Shows the path of an executable command.                               | `which python`                |
| `whereis` | Where Is                        | Locates binary, source, and manual files of a command.                 | `whereis bash`                |
| `echo`    | Echo                            | Prints text or variables to the terminal.                              | `echo "Hello"`                |
| `sort`    | Sort                            | Sorts lines in a file alphabetically or numerically.                   | `sort names.txt`              |
| `uniq`    | Unique                          | Removes or reports duplicate adjacent lines.                           | `uniq file.txt`               |
| `wc`      | Word Count                      | Counts lines, words, and characters in a file.                         | `wc file.txt`                 |
| `cut`     | Cut                             | Extracts specific columns or fields from text.                         | `cut -d: -f1 /etc/passwd`     |
| `tr`      | Translate                       | Translates or deletes characters.                                      | `echo hello \| tr a-z A-Z`    |
| `man`     | Manual                          | Displays the manual page for a command.                                | `man ls`                      |
| `info`    | Information                     | Shows detailed documentation for commands.                             | `info ls`                     |
| `whatis`  | What Is                         | Displays a short description of a command.                             | `whatis grep`                 |
| `clear`   | Clear                           | Clears the terminal screen.                                            | `clear`                       |
| `history` | History                         | Displays previously executed commands.                                 | `history`                     |
| `alias`   | Alias                           | Creates shortcuts for commands.                                        | `alias ll='ls -l'`            |
| `uname`   | Unix Name                       | Displays system information.                                           | `uname -a`                    |
| `whoami`  | Who Am I                        | Displays the current logged-in user.                                   | `whoami`                      |
| `date`    | Date                            | Shows or sets the system date and time.                                | `date`                        |
| `cal`     | Calendar                        | Displays a calendar.                                                   | `cal`                         |
| `df`      | Disk Free                       | Shows disk space usage of file systems.                                | `df -h`                       |
| `du`      | Disk Usage                      | Displays file and directory sizes.                                     | `du -sh folder/`              |
| `free`    | Free Memory                     | Shows memory usage information.                                        | `free -h`                     |
| `ps`      | Process Status                  | Displays running processes.                                            | `ps aux`                      |
| `top`     | Top                             | Displays real-time system and process information.                     | `top`                         |
| `kill`    | Kill                            | Terminates a process using its PID.                                    | `kill 1234`                   |
| `ping`    | Packet Internet Groper          | Tests network connectivity to a host.                                  | `ping google.com`             |
| `ip`      | IP                              | Displays and configures network interfaces.                            | `ip addr`                     |
| `ssh`     | Secure Shell                    | Connects securely to remote systems.                                   | `ssh user@server`             |
| `scp`     | Secure Copy                     | Copies files securely between systems.                                 | `scp file.txt user@host:/tmp` |

