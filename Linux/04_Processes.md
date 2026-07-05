# Chapter 04: Processes

A **process** is simply a program that is currently being executed by the operating system.

For example:

* When you open a terminal, a terminal process starts.
* When you open a browser, a browser process starts.
* When you run `python app.py`, a Python process is created.

In Linux, almost everything running on the system is represented as a process.

---

# 1. What is a Process?

A process consists of:

| Component             | Description                            |
| --------------------- | -------------------------------------- |
| Program Code          | Instructions being executed            |
| Process ID (PID)      | Unique number assigned to each process |
| Memory                | RAM allocated to the process           |
| Registers             | CPU state information                  |
| Open Files            | Files currently used by the process    |
| Environment Variables | Variables available to the process     |

Example:

```bash
echo $$
```

Output:

```bash
2456
```

`$$` displays the PID of the current shell.

---

# 2. Process States

A process can exist in several states.

| State          | Meaning                    |
| -------------- | -------------------------- |
| Running (R)    | Currently executing on CPU |
| Sleeping (S)   | Waiting for an event       |
| Disk Sleep (D) | Waiting for disk I/O       |
| Stopped (T)    | Suspended process          |
| Zombie (Z)     | Finished but still present |
| Idle (I)       | Kernel idle thread         |

You can see process states using:

```bash
ps aux
```

Example output:

```bash
USER   PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND
suraj  2501 0.0 0.1 12000 5000 pts/0 S+ 10:00 0:00 bash
```

The `STAT` column shows the process state.

---

# 3. Viewing Processes

## `ps` — Display Running Processes

| Command          | Description                    |
| ---------------- | ------------------------------ |
| `ps`             | Shows current shell processes  |
| `ps -e`          | Shows all processes            |
| `ps -ef`         | Full-format listing            |
| `ps aux`         | Detailed list of all processes |
| `ps -u username` | Processes of a specific user   |

Example:

```bash
ps aux | less
```

---

## `top` — Real-Time Process Monitor

```bash
top
```

Displays:

* CPU usage
* Memory usage
* Running processes
* Load average

Important keys inside `top`:

| Key | Action         |
| --- | -------------- |
| `q` | Quit           |
| `k` | Kill process   |
| `M` | Sort by memory |
| `P` | Sort by CPU    |
| `h` | Help           |

---

## `htop` — Interactive Process Viewer

```bash
htop
```

Features:

* Colorful interface
* Mouse support
* Easy process management

Install:

```bash
sudo apt install htop
```

---

# 4. Process Hierarchy

Linux processes are organized as a tree.

The first userspace process started by the kernel is usually:

```text
systemd (PID 1)
```

All other processes descend from it.

View the process tree:

```bash
pstree
```

Example:

```text
systemd─┬─NetworkManager
        ├─sshd───bash
        └─gnome-shell
```

Install if missing:

```bash
sudo apt install psmisc
```

---

# 5. Foreground and Background Processes

## Foreground Process

Runs directly in the terminal.

Example:

```bash
sleep 100
```

The terminal becomes occupied.

---

## Background Process

Runs without occupying the terminal.

Start directly in background:

```bash
sleep 100 &
```

Example output:

```bash
[1] 4567
```

`4567` is the PID.

---

# 6. Job Control Commands

| Command    | Description               |
| ---------- | ------------------------- |
| `jobs`     | Show background jobs      |
| `bg`       | Resume job in background  |
| `fg`       | Bring job to foreground   |
| `Ctrl + Z` | Suspend current process   |
| `Ctrl + C` | Terminate current process |

Example:

Start:

```bash
sleep 300
```

Suspend:

```text
Ctrl + Z
```

Move to background:

```bash
bg
```

Bring back:

```bash
fg
```

---

# 7. Finding Processes

## `pgrep`

Find process by name.

```bash
pgrep bash
```

Example:

```bash
2456
```

---

## `pidof`

```bash
pidof sshd
```

Example:

```bash
1234 1235
```

---

# 8. Sending Signals

Linux communicates with processes using **signals**.

Common signals:

| Signal  | Number | Description             |
| ------- | ------ | ----------------------- |
| SIGTERM | 15     | Graceful termination    |
| SIGKILL | 9      | Force kill              |
| SIGSTOP | 19     | Pause process           |
| SIGCONT | 18     | Continue paused process |
| SIGINT  | 2      | Interrupt (`Ctrl + C`)  |

View all signals:

```bash
kill -l
```

---

# 9. Killing Processes

## Kill by PID

```bash
kill PID
```

Example:

```bash
kill 2456
```

Sends `SIGTERM`.

---

## Force Kill

```bash
kill -9 PID
```

Example:

```bash
kill -9 2456
```

---

## Kill by Name

```bash
pkill firefox
```

---

## Kill All Processes by Name

```bash
killall firefox
```

---

# 10. Process Priority

Linux schedules processes using priorities.

## Nice Value

Range:

```text
-20 (highest priority)
 19 (lowest priority)
```

Default:

```text
0
```

View priorities:

```bash
ps -el
```

---

## Start Process with Priority

```bash
nice -n 10 sleep 300
```

---

## Change Existing Priority

```bash
renice 5 -p 2456
```

---

# 11. Practical Commands Summary

| Command   | Purpose                     |
| --------- | --------------------------- |
| `ps`      | Show processes              |
| `top`     | Real-time monitoring        |
| `htop`    | Interactive monitoring      |
| `pstree`  | Show process hierarchy      |
| `jobs`    | Show jobs                   |
| `bg`      | Background job              |
| `fg`      | Foreground job              |
| `pgrep`   | Find process                |
| `pidof`   | Get PID                     |
| `kill`    | Terminate process           |
| `pkill`   | Kill by name                |
| `killall` | Kill all matching processes |
| `nice`    | Start with priority         |
| `renice`  | Change priority             |

# Hands-On Practice

Run these commands one by one:

```bash
echo $$
ps
ps aux
top
sleep 300 &
jobs
fg
Ctrl + Z
bg
pgrep bash
pstree
kill -l
nice -n 10 sleep 300
```

# Mini Lab

1. Start a process:

```bash
sleep 500
```

2. Suspend it:

```text
Ctrl + Z
```

3. Move it to background:

```bash
bg
```

4. Check jobs:

```bash
jobs
```

5. Find its PID:

```bash
ps aux | grep sleep
```

6. Kill it:

```bash
kill PID
```

#### Output 

```
suraj@SurajAltysys:~/practice/git_practice$ sleep 500
^Z
[2]+  Stopped                 sleep 500
suraj@SurajAltysys:~/practice/git_practice$ bg
[2]+ sleep 500 &
suraj@SurajAltysys:~/practice/git_practice$ jobs
[1]+  Stopped                 ps aux | less
[2]-  Running                 sleep 500 &
suraj@SurajAltysys:~/practice/git_practice$ ps aux | grep sleep
suraj    63537  0.0  0.0   3128  1664 pts/4    S    06:13   0:00 sleep 500
suraj    63539  0.0  0.0   4092  1920 pts/4    S+   06:13   0:00 grep --color=auto sleep
suraj@SurajAltysys:~/practice/git_practice$ kill 63537
suraj@SurajAltysys:~/practice/git_practice$
```


---

#### Process State Code 

PROCESS STATE CODES
- Here are the different values that the s, stat and state output specifiers (header "STAT" or "S")  will  display  to  describe  the  state  of  a process:

               D    uninterruptible sleep (usually IO)
               I    Idle kernel thread
               R    running or runnable (on run queue)
               S    interruptible sleep (waiting for an event to complete)
               T    stopped by job control signal
               t    stopped by debugger during the tracing
               W    paging (not valid since the 2.6.xx kernel)
               X    dead (should never be seen)
               Z    defunct ("zombie") process, terminated but not reaped by its parent

       For BSD formats and when the stat keyword is used, additional characters may be displayed:

               <    high-priority (not nice to other users)
               N    low-priority (nice to other users)
               L    has pages locked into memory (for real-time and custom IO)
               s    is a session leader
               l    is multi-threaded (using CLONE_THREAD, like NPTL pthreads do)
               +    is in the foreground process group
			   
---

### Background v/s Foreground

#### Foreground:

A foreground process is a process that is directly connected to your terminal. When it is running:

- You can interact with it using the keyboard.
- The terminal waits until the process finishes.
- You cannot run another command in the same terminal until it completes (unless you open another terminal).
- Example
```
sleep 30
```

#### Background Process

A background process runs without occupying the terminal. The shell immediately gives you the prompt back, allowing you to execute other commands.

Start a process in the background
- Add & at the end of the command:
```
sleep 30 &
```

Differnece: 

| Foreground                           | Background                                    |
| ------------------------------------ | --------------------------------------------- |
| Uses the terminal interactively      | Runs without occupying the terminal           |
| Only one foreground job per terminal | Multiple background jobs possible             |
| Terminal waits for it to finish      | Terminal remains available for other commands |
