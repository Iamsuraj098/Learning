
# Chapter 10 — Linux Security

## Learning Objectives

By the end of this chapter you'll understand:

* Linux security principles
* File permissions review
* Authentication
* Authorization
* sudo
* SSH security
* Firewalls
* SELinux/AppArmor
* Logs
* Process security
* Updates
* Security best practices

---

# 1. Security Layers

Think of Linux security like a building.

```
Internet
     │
Firewall
     │
SSH
     │
User Authentication
     │
Permissions
     │
Applications
     │
Kernel
     │
Hardware
```

Every layer protects the one below it.

---

# 2. CIA Triad

Every security concept tries to protect three things.

| Principle       | Meaning                             | Example                 |
| --------------- | ----------------------------------- | ----------------------- |
| Confidentiality | Only authorized users can view data | Password file           |
| Integrity       | Data cannot be modified improperly  | Database records        |
| Availability    | Services remain accessible          | Web server stays online |

Example:

```
Employee Salary Database

Confidentiality
Only HR can read.

Integrity
Nobody except HR can edit.

Availability
HR can always access it.
```

---

# 3. Authentication vs Authorization

These two terms are commonly confused.

## Authentication

Who are you?

Examples

```
Password

SSH Key

Fingerprint

OTP
```

Linux checks your identity.

---

## Authorization

What are you allowed to do?

Example

```
User:
suraj

Allowed:
Read files

Not Allowed:
Shutdown server
```

Authentication happens first.

Authorization happens second.

---

# 4. Principle of Least Privilege

Very important concept.

Every user should receive only the permissions they actually need.

Bad

```
Everyone is root.
```

Good

```
Developer

Can:
Restart application

Cannot:
Delete databases

Cannot:
Create users
```

---

# 5. Root User

```
UID = 0
```

Root can do almost everything.

Examples

```
Delete files

Kill any process

Install software

Create users

Change passwords

Shutdown machine
```

Avoid logging in directly as root for daily work.

Instead use:

```bash
sudo command
```

---

# 6. sudo

Instead of becoming root permanently:

```bash
sudo apt update
```

Linux temporarily grants administrative privileges.

Check your permissions:

```bash
sudo -l
```

View the current user:

```bash
whoami
```

Check the effective user after using sudo:

```bash
sudo whoami
```

Output

```
root
```

---

# 7. Password Security

A good password should be:

* Long
* Unique
* Random
* Not reused

Examples

Bad

```
password123

india123

admin
```

Good

```
Mango#River82!Sky
```

Change your password:

```bash
passwd
```

Change another user's password (requires sudo):

```bash
sudo passwd username
```

---

# 8. Password Storage

Linux does **not** store plain-text passwords.

User information:

```bash
cat /etc/passwd
```

Passwords are stored separately in:

```bash
sudo cat /etc/shadow
```

Example:

```
suraj:$y$j9T$...
```

The long string is a **password hash**, not the original password.

---

# 9. Account Locking

Lock a user account:

```bash
sudo passwd -l username
```

Unlock:

```bash
sudo passwd -u username
```

---

# 10. Important Security Files

| File                         | Purpose             |
| ---------------------------- | ------------------- |
| `/etc/passwd`                | User information    |
| `/etc/shadow`                | Password hashes     |
| `/etc/group`                 | Groups              |
| `/etc/sudoers`               | sudo rules          |
| `/etc/ssh/`                  | SSH configuration   |
| `/var/log/auth.log` (Ubuntu) | Authentication logs |

---

# Hands-on Practice

Run these commands and observe the output:

```bash
whoami
```

```bash
id
```

```bash
groups
```

```bash
sudo -l
```

```bash
cat /etc/passwd
```

```bash
sudo cat /etc/shadow
```

```bash
passwd
```

```bash
sudo passwd -l testuser
```

```bash
sudo passwd -u testuser
```

---

# Key Takeaways

* Security is built in layers.
* Authentication verifies identity.
* Authorization determines permissions.
* Follow the Principle of Least Privilege.
* Use `sudo` instead of logging in as `root`.
* Passwords are stored as hashes in `/etc/shadow`.
* Keep user and security configuration files protected.
