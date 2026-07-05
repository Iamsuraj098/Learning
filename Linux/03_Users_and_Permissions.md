# Chapter 03: Users and Permissions

## Why are Users and Permissions Important?

Linux systems are often shared by multiple users simultaneously. Permissions ensure that:

* Users can access only their own files.
* System files remain protected.
* Applications run securely.
* Accidental or malicious changes are prevented.

---

# Topics Covered in This Chapter

## 1. Linux User Types

| User Type    | Description                                                                    |
| ------------ | ------------------------------------------------------------------------------ |
| Root User    | The superuser with unrestricted access to the entire system.                   |
| Regular User | Normal user account with limited privileges.                                   |
| System User  | Accounts created for services and daemons (e.g., web server, database server). |

Example:

```bash
root
himanshu
www-data
mysql
```

---

## 2. Important Files Related to Users

| File           | Purpose                          |
| -------------- | -------------------------------- |
| `/etc/passwd`  | Stores user account information. |
| `/etc/shadow`  | Stores encrypted passwords.      |
| `/etc/group`   | Stores group information.        |
| `/etc/sudoers` | Defines sudo privileges.         |

You can view them:

```bash
cat /etc/passwd
cat /etc/group
sudo cat /etc/shadow
```

---

## 3. Understanding `/etc/passwd`

Example entry:

```text
himanshu:x:1000:1000:Himanshu:/home/himanshu:/bin/bash
```

| Field            | Meaning                          |
| ---------------- | -------------------------------- |
| `himanshu`       | Username                         |
| `x`              | Password stored in `/etc/shadow` |
| `1000`           | User ID (UID)                    |
| `1000`           | Primary Group ID (GID)           |
| `Himanshu`       | User description                 |
| `/home/himanshu` | Home directory                   |
| `/bin/bash`      | Default shell                    |

---

## 4. User IDs (UID)

| UID Range | Meaning       |
| --------- | ------------- |
| `0`       | Root user     |
| `1-999`   | System users  |
| `1000+`   | Regular users |

Check your UID:

```bash
id
```

Example:

```bash
uid=1000(himanshu) gid=1000(himanshu)
```

---

## 5. Groups in Linux

A group is a collection of users.

Examples:

```bash
developers
admins
docker
```

Commands:

| Command        | Description                  |
| -------------- | ---------------------------- |
| `groups`       | Show groups of current user. |
| `id`           | Show UID and GIDs.           |
| `getent group` | List all groups.             |

Example:

```bash
groups
```

Output:

```bash
himanshu sudo docker
```

---

## 6. Creating and Managing Users

| Command               | Description                                        |
| --------------------- | -------------------------------------------------- |
| `useradd username`    | Create a user.                                     |
| `adduser username`    | Interactive user creation (recommended on Ubuntu). |
| `passwd username`     | Set/change password.                               |
| `usermod`             | Modify user account.                               |
| `userdel username`    | Delete user.                                       |
| `userdel -r username` | Delete user with home directory.                   |

Examples:

```bash
sudo adduser john

sudo passwd john

sudo userdel -r john
```

---

## 7. Creating and Managing Groups

| Command                 | Description        |
| ----------------------- | ------------------ |
| `groupadd groupname`    | Create group.      |
| `groupdel groupname`    | Delete group.      |
| `groupmod`              | Modify group.      |
| `gpasswd -a user group` | Add user to group. |

Example:

```bash
sudo groupadd developers

sudo gpasswd -a john developers
```

---

## 8. File Ownership

Every file has:

1. Owner (User)
2. Group
3. Others

Check ownership:

```bash
ls -l
```

Example:

```bash
-rw-r--r-- 1 himanshu developers 250 Jun 21 notes.txt
```

| Part         | Meaning     |
| ------------ | ----------- |
| `himanshu`   | Owner       |
| `developers` | Group owner |

Change ownership:

| Command                 | Description             |
| ----------------------- | ----------------------- |
| `chown user file`       | Change owner.           |
| `chown user:group file` | Change owner and group. |
| `chgrp group file`      | Change group owner.     |

Examples:

```bash
sudo chown john file.txt

sudo chown john:developers file.txt

sudo chgrp developers file.txt
```

---

## 9. Linux Permissions

Example:

```bash
-rwxr-xr--
```
 
Breakdown:

```text
- rwxr -x r--
  |   |   |
Owner Group Others
```

| Symbol | Meaning       |
| ------ | ------------- |
| `r`    | Read          |
| `w`    | Write         |
| `x`    | Execute       |
| `-`    | No permission |

### Permission Values

| Permission | Value |
| ---------- | ----- |
| `r`        | 4     |
| `w`        | 2     |
| `x`        | 1     |

Examples:

| Permission | Numeric |
| ---------- | ------- |
| `rwx`      | 7       |
| `rw-`      | 6       |
| `r-x`      | 5       |
| `r--`      | 4       |

---

## 10. Changing Permissions

### Symbolic Mode

```bash
chmod u+x script.sh
chmod g-w file.txt
chmod o+r file.txt
```

| Symbol | Meaning    |
| ------ | ---------- |
| `u`    | User/Owner |
| `g`    | Group      |
| `o`    | Others     |
| `a`    | All        |

---

### Numeric Mode

```bash
chmod 755 script.sh
chmod 644 file.txt
chmod 700 private.txt
```

Common permissions:

| Permission | Meaning                             |
| ---------- | ----------------------------------- |
| `777`      | Full access for everyone            |
| `755`      | Owner full, others read and execute |
| `644`      | Owner read/write, others read only  |
| `700`      | Owner only                          |
| `600`      | Private file                        |

---

## 11. Sudo

`sudo` allows a regular user to execute commands as root.

Example:

```bash
sudo apt update
```

Check sudo privileges:

```bash
sudo -l
```

---

## 12. Switching Users

| Command         | Description                         |
| --------------- | ----------------------------------- |
| `su username`   | Switch user.                        |
| `su - username` | Switch with full login environment. |
| `sudo -i`       | Open root shell.                    |

Examples:

```bash
su john

su - john

sudo -i
```

---

# Essential Commands to Practice

```bash
whoami
id
groups
passwd
adduser
userdel
groupadd
groupdel
gpasswd
chown
chgrp
chmod
sudo
su
```

# Hands-on Lab

Create a practice environment:

```bash
sudo adduser alice
sudo adduser bob

sudo groupadd developers

sudo gpasswd -a alice developers

touch project.txt

sudo chown alice:developers project.txt

chmod 664 project.txt

ls -l project.txt
```

Expected output:

```bash
-rw-rw-r-- 1 alice developers 0 Jun 21 project.txt
```
