# Chapter 11 - Linux Troubleshooting

## Learning Objectives

By the end of this chapter, you will be able to troubleshoot:

* Boot problems
* Service failures
* Network issues
* Disk space problems
* High CPU and memory usage
* Permission issues
* Package installation failures
* DNS issues
* SSH connection problems
* Log analysis

---

# Troubleshooting Methodology

Instead of randomly trying commands, always follow this process.

```
Problem
   ↓
Collect information
   ↓
Identify the failing component
   ↓
Check logs
   ↓
Verify configuration
   ↓
Fix the issue
   ↓
Test
   ↓
Monitor
```

A useful mindset is:

> Observe → Diagnose → Fix → Verify

---

# Step 1: Gather Information

Before changing anything, collect system information.

| Command       | Purpose                      |
| ------------- | ---------------------------- |
| `hostnamectl` | System information           |
| `uname -a`    | Kernel version               |
| `uptime`      | System uptime and load       |
| `date`        | Current system time          |
| `who`         | Logged-in users              |
| `last`        | Login history                |
| `history`     | Previously executed commands |

Example:

```bash
hostnamectl
```

Shows:

* OS
* Kernel
* Architecture
* Hostname

---

# Step 2: Check System Health

## CPU

```bash
top
```

or

```bash
htop
```

Look for:

* CPU usage
* Load average
* Running processes

---

## Memory

```bash
free -h
```

Example:

```
Mem:
8G total
6G used
2G free
```

---

## Disk

```bash
df -h
```

Shows:

* Mounted filesystem
* Available space
* Usage %

---

## Inode Usage

Sometimes disk appears full because inodes are exhausted.

```bash
df -i
```

---

# Step 3: Check Running Processes

```bash
ps aux
```

or

```bash
ps -ef
```

Search for a process:

```bash
ps -ef | grep nginx
```

Kill if necessary:

```bash
kill PID
```

Force kill:

```bash
kill -9 PID
```

---

# Step 4: Check Services

List failed services:

```bash
systemctl --failed
```

Status of one service:

```bash
systemctl status ssh
```

Restart:

```bash
sudo systemctl restart ssh
```

Enable on boot:

```bash
sudo systemctl enable ssh
```

---

# Step 5: Check Logs

Most Linux problems can be diagnosed by reading logs.

## System logs

```bash
journalctl
```

Latest entries:

```bash
journalctl -n 50
```

Live logs:

```bash
journalctl -f
```

Logs for a service:

```bash
journalctl -u ssh
```

Boot logs:

```bash
journalctl -b
```

Previous boot:

```bash
journalctl -b -1
```

---

# Step 6: Verify Network

Check IP:

```bash
ip addr
```

Routing:

```bash
ip route
```

Ping gateway:

```bash
ping 192.168.1.1
```

Ping Google:

```bash
ping 8.8.8.8
```

Ping domain:

```bash
ping openai.com
```

If IP works but domain doesn't:

Problem is probably DNS.

---

# Step 7: Check DNS

View DNS servers:

```bash
cat /etc/resolv.conf
```

Query DNS:

```bash
dig openai.com
```

or

```bash
nslookup openai.com
```

If `nslookup` is missing:

```bash
sudo apt install dnsutils
```

(We encountered a similar issue in your Linux practice.)

---

# Step 8: Verify Connectivity

Check listening ports:

```bash
ss -tuln
```

Show process using a port:

```bash
ss -tulpn
```

Example:

```
:22
```

means SSH is listening.

---

# Step 9: Check Disk Usage

Largest directories:

```bash
du -sh /*
```

Largest files:

```bash
find / -type f -size +100M
```

---

# Step 10: Check Permissions

Current user:

```bash
whoami
```

Permissions:

```bash
ls -l
```

Ownership:

```bash
ls -ld directory
```

Change owner:

```bash
sudo chown user:user file
```

Change permissions:

```bash
chmod 644 file
```

---

# Essential Troubleshooting Commands

| Command              | Purpose                    |
| -------------------- | -------------------------- |
| `top`                | Monitor CPU and memory     |
| `htop`               | Interactive process viewer |
| `free -h`            | Memory usage               |
| `df -h`              | Disk usage                 |
| `df -i`              | Inode usage                |
| `du -sh`             | Directory size             |
| `ps aux`             | Running processes          |
| `kill`               | Stop process               |
| `systemctl status`   | Service status             |
| `systemctl --failed` | Failed services            |
| `journalctl`         | System logs                |
| `ip addr`            | Network interfaces         |
| `ip route`           | Routing table              |
| `ping`               | Connectivity test          |
| `ss -tulpn`          | Listening ports            |
| `dig`                | DNS lookup                 |
| `nslookup`           | DNS query                  |
| `hostnamectl`        | System details             |
| `uptime`             | Uptime and load            |

---

## Chapter Summary

You learned how to:

* Follow a structured troubleshooting methodology.
* Collect system information before making changes.
* Diagnose CPU, memory, disk, network, and service issues.
* Analyze logs with `journalctl`.
* Troubleshoot DNS and connectivity problems.
* Use essential commands to identify and resolve common Linux issues.
