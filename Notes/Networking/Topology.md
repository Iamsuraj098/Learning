**Network Topology** is the arrangement or structure of devices (computers, switches, routers, servers) and how they are connected in a network.

Think of topology as the **map of a network**.

---

## 1. Star Topology

Most common topology in modern LANs.

```text
       PC1
        |
PC2 -- Switch -- PC3
        |
       PC4
```

### How it works

* Every device connects to a central device (usually a switch).
* Devices do not communicate directly with each other.
* All communication passes through the switch.

### Advantages

* Easy to manage.
* Easy to add/remove devices.
* Failure of one cable affects only one device.

### Disadvantages

* If the central switch fails, the entire network goes down.

### Real-world example

* Home Wi-Fi router connecting laptops, phones, and TVs.
* Office LAN networks.

---

## 2. Bus Topology

Older topology, rarely used today.

```text
PC1 ---- PC2 ---- PC3 ---- PC4
```

### How it works

* All devices share a single communication cable.

### Advantages

* Cheap.
* Requires less cable.

### Disadvantages

* Difficult to troubleshoot.
* Single cable failure can affect the whole network.
* Performance degrades as devices increase.

### Real-world example

* Early Ethernet networks.

---

## 3. Ring Topology

Devices form a circular chain.

```text
PC1 ---- PC2
 |         |
 |         |
PC4 ---- PC3
```

### How it works

* Data travels around the ring.
* Each device forwards data to the next device.

### Advantages

* Predictable performance.
* No collision issues.

### Disadvantages

* Failure of one node can disrupt the network.
* Difficult to expand.

### Real-world example

* Legacy Token Ring networks.

---

## 4. Mesh Topology

Every node is connected to multiple nodes.

```text
A ------- B
|\       /|
| \     / |
|  \   /  |
|   \ /   |
|   / \   |
|  /   \  |
| /     \ |
|/       \|
C ------- D
```

### How it works

* Multiple paths exist between devices.
* If one path fails, traffic can take another route.

### Advantages

* Highly reliable.
* No single point of failure.
* Excellent fault tolerance.

### Disadvantages

* Expensive.
* Complex configuration.

### Real-world example

* Internet backbone.
* Cloud provider networks.
* Data center networks.

---

## 5. Tree Topology

Hierarchical structure.

```text
           Core Switch
             /    \
            /      \
      Switch1     Switch2
        /  \         /  \
      PC1 PC2      PC3 PC4
```

### How it works

* Combination of Star and Bus concepts.
* Devices are arranged in parent-child relationships.

### Advantages

* Easy to scale.
* Suitable for large organizations.

### Disadvantages

* Core device failure affects large portions of the network.

### Real-world example

* Enterprise networks.
* University campuses.

---

## 6. Hybrid Topology

Combination of multiple topologies.

```text
       Switch
      /  |  \
    PC1 PC2 PC3

         |
      Router
         |

     Mesh Network
```

### How it works

* Uses different topologies where appropriate.

### Advantages

* Flexible.
* Scalable.
* Common in modern environments.

### Real-world example

* Large corporations.
* Cloud infrastructure.
