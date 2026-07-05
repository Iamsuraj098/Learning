# File System

**Linux philosophies** - "Everything is a File"

Linux organizes everything into a single hierarchical tree structure that starts from the root directory.
Unlike Windows, where you have separate drives like C:\, D:\, etc.,

# 01. File System (Linux)

The Linux file system is the way Linux organizes, stores, and manages files and directories on storage devices such as hard disks, SSDs, USB drives, and network storage.

Unlike Windows, where you have separate drives like `C:\`, `D:\`, etc., Linux organizes everything into a **single hierarchical tree structure** that starts from the root directory `/`.

## 1. Everything in Linux is a File

One of the most important Linux philosophies is:

> "Everything is a file."

This includes:

* Regular files (`notes.txt`, `script.sh`)
* Directories (`Documents/`)
* Hard disks (`/dev/sda`)
* USB devices
* Keyboards and mice
* Printers
* Processes (through `/proc`)

For example:

```bash
ls /dev
```

You will see device files representing hardware.

---

## 2. File System Hierarchy

The Linux file system starts from the **root directory**:

```text
/
```

Everything exists under this root.

```text
/
├── bin
├── boot
├── dev
├── etc
├── home
├── lib
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── sbin
├── tmp
├── usr
└── var
```

---

## 3. Important Directories

### `/`

The top-most directory.

Example:

```bash
cd /
```

---

### `/home`

Contains users' personal files.

Example:

```text
/home/suraj
/home/john
```

Your documents, downloads, and personal settings are usually stored here.

```bash
cd /home
ls
```

---

### `/root`

Home directory of the root (administrator) user.

```text
/root
```

Do not confuse:

* `/` → root directory
* `/root` → root user's home directory

---

### `/bin`

Contains essential user commands.

Examples:

```bash
ls
cp
mv
cat
```

Check:

```bash
ls /bin
```

---

### `/sbin`

Contains system administration commands.

Examples:

```bash
fdisk
mount
shutdown
```

Usually intended for administrators.

---

### `/etc`

Contains system configuration files.

Examples:

```text
/etc/passwd
/etc/hosts
/etc/fstab
```

Example:

```bash
cat /etc/hostname
```

---

### `/var`

Contains variable data that changes frequently.

Examples:

```text
/var/log
/var/cache
```

System logs are stored here.

```bash
ls /var/log
```

---

### `/tmp`

Temporary files.

Applications store temporary data here.

```bash
cd /tmp
```

Files may be deleted automatically after reboot.

---

### `/usr`

Contains user applications and libraries.

Examples:

```text
/usr/bin
/usr/lib
/usr/share
```

Most installed software resides here.

---

### `/boot`

Contains files required during system startup.

Examples:

```text
Kernel image
Bootloader files
```

---

### `/dev`

Contains device files.

Examples:

```text
/dev/sda   → Hard disk
/dev/null  → Discards data
/dev/tty   → Terminal
```

Example:

```bash
ls /dev
```

---

### `/proc`

A virtual file system that provides information about running processes and the kernel.

Example:

```bash
cat /proc/cpuinfo
cat /proc/meminfo
```

No actual files are stored here; information is generated dynamically by the kernel.

---

## 4. File Types in Linux

You can identify file types using:

```bash
ls -l
```

Example output:

```text
-rw-r--r--  file.txt
drwxr-xr-x  Documents
lrwxrwxrwx  shortcut
```

First character indicates the type:

| Symbol | Type             |
| ------ | ---------------- |
| `-`    | Regular file     |
| `d`    | Directory        |
| `l`    | Symbolic link    |
| `c`    | Character device |
| `b`    | Block device     |
| `p`    | Named pipe       |
| `s`    | Socket           |

---

## 5. Absolute vs Relative Path

### Absolute Path

Starts from `/`.

Example:

```bash
/home/suraj/Documents/file.txt
```

Always starts with `/`.

---

### Relative Path

Specified relative to the current directory.

Example:

```bash
Documents/file.txt
```

Special symbols:

```text
.   → Current directory
..  → Parent directory
~   → User's home directory
```

Examples:

```bash
cd ..
cd .
cd ~
```

---

## 6. Practical Commands

Try these commands on your Linux machine:

```bash
pwd                # Show current directory

ls                 # List files

ls -l              # Detailed listing

cd /               # Go to root directory

cd ~               # Go to home directory

tree /home         # Display directory tree (if installed)

file /bin/ls       # Show file type

mkdir demo         # Create directory

touch file1.txt    # Create file
```

---

## 7. Quick Revision

* Linux organizes everything under a single root directory `/`.
* Everything in Linux is treated as a file.
* `/home` stores user files.
* `/etc` stores configuration files.
* `/var` stores changing data like logs.
* `/tmp` stores temporary files.
* `/dev` contains device files.
* `/proc` provides kernel and process information.
* Paths can be absolute or relative.

For Linux interviews, understanding the purpose of `/home`, `/etc`, `/var`, `/proc`, `/dev`, `/usr`, and `/tmp` is essential.

---
---
---


## Linux File System Commands

| Command             | Description                                                                                                          |
| ------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `pwd`               | Displays the full path of the current working directory.                                                             |
| `ls`                | Lists files and directories in the current directory.                                                                |
| `ls -l`             | Lists files and directories in long format with details such as permissions, owner, size, and modification date.     |
| `cd /`              | Changes the current directory to the root directory (`/`).                                                           |
| `cd /home`          | Changes the current directory to `/home`.                                                                            |
| `cd ..`             | Moves to the parent directory of the current directory.                                                              |
| `cd .`              | Stays in the current directory (`.` represents the current directory).                                               |
| `cd ~`              | Changes the current directory to the current user's home directory.                                                  |
| `tree /home`        | Displays the directory structure of `/home` in a tree-like format. (`tree` package may need to be installed.)        |
| `file /bin/ls`      | Shows the type of the specified file. For example, it identifies whether `/bin/ls` is an executable, text file, etc. |
| `mkdir demo`        | Creates a new directory named `demo`.                                                                                |
| `touch file1.txt`   | Creates an empty file named `file1.txt`. If the file already exists, it updates its timestamp.                       |
| `cat /etc/hostname` | Displays the contents of the `/etc/hostname` file.                                                                   |
| `cat /proc/cpuinfo` | Displays information about the CPU provided by the kernel.                                                           |
| `cat /proc/meminfo` | Displays memory usage information provided by the kernel.                                                            |
| `ls /bin`           | Lists all files and commands present in the `/bin` directory.                                                        |
| `ls /var/log`       | Lists log files stored in the `/var/log` directory.                                                                  |
| `ls /dev`           | Lists device files available under the `/dev` directory.                                                             |

## Commonly Used `ls` Options

| Command | Description                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------ |
| `ls -a` | Shows all files, including hidden files (files starting with `.`).                               |
| `ls -h` | Displays file sizes in a human-readable format (KB, MB, GB). Usually used with `-l` as `ls -lh`. |
| `ls -R` | Lists files recursively, including subdirectories.                                               |
| `ls -t` | Sorts files by modification time, newest first.                                                  |

## Special Path Symbols

| Symbol | Meaning                           |
| ------ | --------------------------------- |
| `/`    | Root directory of the filesystem. |
| `.`    | Current directory.                |
| `..`   | Parent directory.                 |
| `~`    | Current user's home directory.    |

For learning Linux interactively, try running each command yourself and observe the output. This hands-on approach will help you remember them much faster.

---
---

### Meaning of Folder

- /etc - is a directory (folder) that stores system-wide configuration files.

	- It contains configuration files that control:
		- Operating system settings
		- User and group information
		- Network configuration
		- Service configuration
		- Startup scripts
		- Application settings

	| Path               | Purpose                                 |
	| ------------------ | --------------------------------------- |
	| `/etc/passwd`      | Stores user account information         |
	| `/etc/shadow`      | Stores encrypted user passwords         |
	| `/etc/group`       | Stores group information                |
	| `/etc/hostname`    | Stores the system hostname              |
	| `/etc/hosts`       | Maps hostnames to IP addresses          |
	| `/etc/fstab`       | Defines filesystems mounted at boot     |
	| `/etc/resolv.conf` | DNS server configuration                |
	| `/etc/ssh/`        | Configuration for SSH server and client |
	| `/etc/systemd/`    | Configuration for system services       |
	| `/etc/sudoers`     | Defines sudo permissions                |

- SUDO 
	- Stands for: "SuperUser DO"
	- It is a command that allows a permitted user to execute commands with the privileges of another user, typically the root user (the administrator account).
	- Why is SUDO needed ?
		- Many system tasks require administrative privileges, such as:
		- Installing software
		- Creating or deleting users
		- Modifying system configuration files
		- Starting or stopping system services
	- Syntax
		- ```sudo <command>```
	- `whoami` give the current user Named
	- `sudo whoami` give root directory.