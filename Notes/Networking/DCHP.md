## DCHP
Dynamic Host Configuration Protocol

- It automatically assign the IP address and other network settings to devices when they connect to a network.
- without DHCP: We have to manually configured everything - 
	- IP address
	- Subnet Mask
	- Default Gateway
	- DNS Server

#### DHCP Components
- DHCP client: The device requesting network settings. Like Laptop, Mobile, Printer etc
- DHCP Server: The device assigning network settings. Like Home Router, Windows/Linux DHCP server
- DHCP Lease: The IP address is assigned for a specific period.

#### DHCP Process (DORA): 
- D = Discover: The client doesn't have an IP address yet.
- O = Offer: The DHCP server replies
- R = Request: The client responds
- A = Acknowledge: The DHCP server confirms

#### DORA Flow
```
Client                          DHCP Server

Discover  --------------------->

          <--------------------- Offer

Request   --------------------->

          <--------------------- Acknowledge
```

DCHP Other Configuration Provided: subnet mask, default gateway, and DNS servers to devices on a network