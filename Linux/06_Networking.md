# Chapter 06: Networking

## Topics Covered

### 1. Network Basics

* What is a network?
* IP Address (IPv4 and IPv6)
* Subnet Mask and CIDR notation
* Default Gateway
* DNS (Domain Name System)
* MAC Address
* Ports and Protocols

---

### 2. Viewing Network Information

| Command               | Description                                      |
| --------------------- | ------------------------------------------------ |
| `ip addr`             | Show IP addresses of all interfaces              |
| `ip link`             | Display network interfaces                       |
| `ip route`            | Show routing table                               |
| `hostname -I`         | Display system IP addresses                      |
| `hostname`            | Show system hostname                             |
| `ss -tuln`            | Show listening ports                             |
| `ss -tunp`            | Show active connections with process information |
| `netstat -tuln`       | Legacy command to display listening ports        |
| `nmcli device status` | Show NetworkManager device status                |

---

### 3. Testing Connectivity

| Command      | Description                         |
| ------------ | ----------------------------------- |
| `ping`       | Test connectivity to another host   |
| `traceroute` | Show packet path to destination     |
| `tracepath`  | Trace route without root privileges |
| `mtr`        | Combination of ping and traceroute  |
| `curl`       | Transfer data from URLs             |
| `wget`       | Download files from the web         |

Example:

```bash
ping google.com
```

```bash
traceroute google.com
```

---

### 4. DNS Tools

| Command    | Description               |
| ---------- | ------------------------- |
| `nslookup` | Query DNS information     |
| `dig`      | Advanced DNS query tool   |
| `host`     | Simple DNS lookup utility |

Examples:

```bash
dig google.com
```

```bash
nslookup openai.com
```

---

### 5. Socket and Port Management

| Command    | Description                              |
| ---------- | ---------------------------------------- |
| `ss -tuln` | Show listening TCP/UDP ports             |
| `ss -ant`  | Show TCP connections                     |
| `ss -lun`  | Show UDP sockets                         |
| `lsof -i`  | Show processes using network connections |
| `fuser`    | Identify processes using files or ports  |

Examples:

```bash
ss -tuln
```

```bash
sudo lsof -i :80
```

---

### 6. Network Configuration

| Command       | Description               |
| ------------- | ------------------------- |
| `ip addr add` | Add an IP address         |
| `ip link set` | Enable/disable interfaces |
| `nmcli`       | Manage NetworkManager     |
| `hostnamectl` | Change system hostname    |

Examples:

```bash
sudo ip link set eth0 down
sudo ip link set eth0 up
```

---

### 7. Important Configuration Files

| File                  | Purpose                                      |
| --------------------- | -------------------------------------------- |
| `/etc/hosts`          | Static hostname-to-IP mappings               |
| `/etc/resolv.conf`    | DNS resolver configuration                   |
| `/etc/hostname`       | System hostname                              |
| `/etc/nsswitch.conf`  | Name service lookup order                    |
| `/etc/netplan/*.yaml` | Ubuntu network configuration (modern Ubuntu) |

---

### 8. Common Networking Troubleshooting Workflow

When the network is not working:

1. Check interface status:

```bash
ip addr
```

2. Check gateway:

```bash
ip route
```

3. Test local network:

```bash
ping <gateway-ip>
```

4. Test internet connectivity:

```bash
ping 8.8.8.8
```

5. Test DNS:

```bash
ping google.com
```

6. Check listening ports:

```bash
ss -tuln
```

---

## Practical Exercises

### Exercise 1

Find your IP address:

```bash
ip addr
hostname -I
```

---

### Exercise 2

Display all listening ports:

```bash
ss -tuln
```

---

### Exercise 3

Check the route packets take to Google:

```bash
tracepath google.com
```

---

### Exercise 4

Find the DNS servers your system uses:

```bash
cat /etc/resolv.conf
```

---

### Exercise 5

Find which process is using port 22:

```bash
sudo lsof -i :22
```

# Recommended Learning Order

1. Network Basics
2. `ip` command
3. Routing (`ip route`)
4. `ping`, `traceroute`, `mtr`
5. DNS tools (`dig`, `nslookup`)
6. `ss` and `lsof`
7. Configuration files
8. Troubleshooting scenarios
