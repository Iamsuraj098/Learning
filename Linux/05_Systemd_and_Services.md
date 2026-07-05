# Chapter 05: Systemd and Services

`systemd` is the **init system and service manager** used by most modern Linux distributions such as Ubuntu, Debian, Fedora, RHEL, and CentOS.

It is responsible for:

* Booting the system
* Starting and stopping services
* Managing system states (targets/runlevels)
* Handling logs
* Managing background daemons

---

# 1. What is systemd?

When Linux boots, the kernel starts a process called:

```bash
/usr/lib/systemd/systemd
```

This process gets:

```bash
PID = 1
```

You can verify this:

```bash
ps -p 1
```

Example output:

```bash
PID TTY          TIME CMD
1 ?        00:00:02 systemd
```

`systemd` is the first userspace process and acts as the parent of most other processes.

---

# 2. What is a Service?

A **service** (also called a **daemon**) is a background process that performs a specific task.

Examples:

| Service          | Purpose                     |
| ---------------- | --------------------------- |
| `sshd`           | Allows SSH connections      |
| `cron`           | Runs scheduled jobs         |
| `apache2`        | Web server                  |
| `nginx`          | Web server                  |
| `docker`         | Container engine            |
| `NetworkManager` | Manages network connections |

Services usually run continuously in the background.

---

# 3. What is a Unit?

In `systemd`, everything is represented as a **unit**.

A unit is simply a configuration file that tells `systemd` what to manage.

Common unit types:

| Unit Type | Extension  | Purpose                 |
| --------- | ---------- | ----------------------- |
| Service   | `.service` | Background services     |
| Target    | `.target`  | Group of units          |
| Socket    | `.socket`  | Socket activation       |
| Mount     | `.mount`   | Filesystem mount points |
| Timer     | `.timer`   | Scheduled tasks         |
| Device    | `.device`  | Hardware devices        |
| Path      | `.path`    | Monitor file changes    |

Examples:

```bash
sshd.service
cron.service
multi-user.target
```

---

# 4. The `systemctl` Command

`systemctl` is the main command used to interact with `systemd`.

---

## Check Service Status

```bash
systemctl status ssh
```

Example:

```bash
systemctl status cron
```

Output:

```bash
● cron.service - Regular background program processing daemon
   Loaded: loaded
   Active: active (running)
```

---

## Start a Service

```bash
sudo systemctl start <service>
```

Example:

```bash
sudo systemctl start apache2
```

---

## Stop a Service

```bash
sudo systemctl stop apache2
```

---

## Restart a Service

```bash
sudo systemctl restart apache2
```

---

## Reload Configuration Without Restart

```bash
sudo systemctl reload apache2
```

Useful when changing configuration files.

---

## Reload + Restart If Needed

```bash
sudo systemctl reload-or-restart apache2
```

---

# 5. Enable and Disable Services

## Enable Service at Boot

```bash
sudo systemctl enable apache2
```

This creates symbolic links so the service starts automatically after reboot.

---

## Disable Service at Boot

```bash
sudo systemctl disable apache2
```

---

## Check Whether Service is Enabled

```bash
systemctl is-enabled apache2
```

Possible outputs:

```bash
enabled
disabled
static
masked
```

---

# 6. List Services

## List Running Services

```bash
systemctl list-units --type=service
```

---

## List All Services

```bash
systemctl list-units --type=service --all
```

---

## List Failed Services

```bash
systemctl --failed
```

---

## List Unit Files

```bash
systemctl list-unit-files
```

---

# 7. Service States

A service can be in different states.

| State              | Meaning           |
| ------------------ | ----------------- |
| `active (running)` | Currently running |
| `inactive`         | Stopped           |
| `failed`           | Crashed or error  |
| `activating`       | Starting          |
| `deactivating`     | Stopping          |

Check:

```bash
systemctl status <service>
```

---

# 8. Targets (Replacement for Runlevels)

Older Linux systems used **runlevels**.

`systemd` uses **targets**.

| Old Runlevel | systemd Target      | Purpose              |
| ------------ | ------------------- | -------------------- |
| 0            | `poweroff.target`   | Shutdown             |
| 1            | `rescue.target`     | Single-user mode     |
| 3            | `multi-user.target` | Multi-user text mode |
| 5            | `graphical.target`  | GUI mode             |
| 6            | `reboot.target`     | Reboot               |

---

## Check Current Target

```bash
systemctl get-default
```

Example:

```bash
graphical.target
```

---

## Change Default Target

To boot into command-line mode:

```bash
sudo systemctl set-default multi-user.target
```

To boot into GUI mode:

```bash
sudo systemctl set-default graphical.target
```

---

# 9. Journald (System Logs)

`systemd` includes a logging service called:

```bash
systemd-journald
```

View logs using:

```bash
journalctl
```

---

## Show All Logs

```bash
journalctl
```

---

## Show Latest Logs

```bash
journalctl -n 50
```

---

## Follow Logs in Real Time

```bash
journalctl -f
```

Equivalent to:

```bash
tail -f
```

---

## View Logs for a Service

```bash
journalctl -u ssh
```

Example:

```bash
journalctl -u cron
```

---

## View Logs Since Today

```bash
journalctl --since today
```

---

## View Logs Since Specific Time

```bash
journalctl --since "2026-06-25 10:00:00"
```

---

# 10. Practical Lab

Try these commands on your Linux machine:

### Step 1

Check PID 1:

```bash
ps -p 1
```

---

### Step 2

See all running services:

```bash
systemctl list-units --type=service
```

---

### Step 3

Check status of a service:

```bash
systemctl status cron
```

or

```bash
systemctl status ssh
```

---

### Step 4

Find failed services:

```bash
systemctl --failed
```

---

### Step 5

Check recent logs:

```bash
journalctl -n 20
```

---

# Important Commands Summary

| Command                        | Description               |
| ------------------------------ | ------------------------- |
| `systemctl status service`     | Show service status       |
| `systemctl start service`      | Start service             |
| `systemctl stop service`       | Stop service              |
| `systemctl restart service`    | Restart service           |
| `systemctl reload service`     | Reload configuration      |
| `systemctl enable service`     | Start at boot             |
| `systemctl disable service`    | Do not start at boot      |
| `systemctl is-enabled service` | Check boot status         |
| `systemctl list-units`         | List active units         |
| `systemctl --failed`           | Show failed units         |
| `journalctl`                   | View logs                 |
| `journalctl -u service`        | Logs for specific service |
| `journalctl -f`                | Follow logs live          |
| `systemctl get-default`        | Show default target       |

## Concepts to Remember

1. `systemd` is the init system (`PID 1`).
2. Services are background processes (daemons).
3. `systemctl` manages services and units.
4. A unit is an object managed by `systemd`.
5. Targets replace traditional runlevels.
6. `journalctl` is used to read system logs.
