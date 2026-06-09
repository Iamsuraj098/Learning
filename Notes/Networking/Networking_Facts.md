## 1. Public and Private IPs

**Public IPs** - A public IP address assigned by your internet service provider and is visible on the internet.
Characteristics:
- Unique across the entire internet.
- Used to identify your network to external websites and services.
- Assigned to your router or gateway device.
- Example - When you visit a website, the website sees your public IP address.

**Private IPs** - A private IP address is used inside the local network(home, office, school) and is not directly accessible from the internet.
Characteristics:
- Used for communication between devices within the same network.
- Can be reused in different networks.
- Assigned by your router (usually via DHCP).
- Examples - 192.168.1.10
- Private IP Ranges:
	- 10.0.0.0 – 10.255.255.255
	- 172.16.0.0 – 172.31.255.255
	- 192.168.0.0 – 192.168.255.255

##### How They Work Together
```
	     Internet
		|
	Public IP: 203.0.113.45
		|
	      Router
		|
	-----------------------
	|          |          |
	PC       Phone      TV
	192.168.1.2 192.168.1.3 192.168.1.4
	(Private IPs)
```

The router uses a technology called NAT(Network Address Translation) to allow multiple devices with private IP address to share on public IP address.

##### Quick Comparision
| Feature             | Public IP              | Private IP                  |
| ------------------- | ---------------------- | --------------------------- |
| Visible on Internet | Yes                    | No                          |
| Globally Unique     | Yes                    | No                          |
| Assigned By         | ISP                    | Router                      |
| Used For            | Internet communication | Local network communication |
| Example             | 203.0.113.45           | 192.168.1.10                |

To find your IPs:
- Public IP - What is my IP ? in a search engine
- Private IP
	- Windows: ipconfig
	- Linux/macOS: ipconfig or ip addr
	
---

#### Phase before that my request in private domain after that it will in public domain -
``` 
Your Laptop
Private IP: 192.168.1.10
	   |
	   v
	Router (NAT)
Private IP: 192.168.1.1 (LAN side)
Public IP: 49.x.x.x (WAN side)
	   |
	   v
	Internet
```
- When your laptop sends a packet:

	- Source IP = 192.168.1.10 (private)
	- Packet reaches the router.
	- Router performs NAT (Network Address Translation).
	- Router replaces the source IP with its public IP (e.g., 49.x.x.x).
	- Packet is sent to the internet.

So the IP itself does not become public. The router translates the packet from a private address to a public address.

## 2. Trace Route
Path that packets take from your computer to a destination host (website, server, IP address).
Traceroute is a network diagnostic tool that discovers the path (hops) to a destination and measures the round-trip latency to each hop along that path.

**Note -** 
- tracert does not measure the one-way travel time.
- It measures the round-trip time (RTT) for each hop (request goes to the hop and the response comes back).

Example - 
```
Hop 1   1 ms    192.168.1.1
Hop 2  10 ms    ISP Router
Hop 3  25 ms    Regional Router
Hop 4  40 ms    Destination Server
```

- Window command to trace it - `treacert {website_name}`
- Other things - 

| Command    | Purpose                                       |
| ---------- | --------------------------------------------- |
| `ping website_name`| Check connectivity and latency        |
| `tracert`  | Show the route packets take                   |
| `pathping` | Combines ping and tracert for deeper analysis |
| `ipconfig` | Display local network configuration           |
| `nslookup` | Query DNS records                             |

---

## 3. Topology 

- Star Topology – devices connected to a central node.
- Bus Topology – devices share a common cable.
- Ring Topology – devices connected in a circle.
- Mesh Topology – multiple interconnected paths (how the Internet largely works).
- Tree Topology – hierarchical branching structure.

Mesh Topology 
```
Your PC
   |
Home Router
   |
ISP Router
 /   |   \
A    B    C
     |
     D
     |
Destination
```

## 4. 
When we use the VPN we increase the hoping and mask our identity between them.