# Azure

### Networking Basics
Networking in Azure (and in general) allows communication between resources, either within the same environment or over the internet.
- In cloud or on-premises environments, networking refers to how systems communicate with each other using IP addresses, routing, and security rules.
- In Azure (and similar platforms), networking ensures that resources like virtual machines, databases, and web apps can connect securely and efficiently—either to the internet, to each other, or to on-prem systems.

### VNet(virtual Network)
- A virtual Network is like the private network within Azure.
- It allows your Azure resources to securly communicate with each other, with the internet.
- Each VNet is logically isolated with other VNet by defaults meaning no data crosses unless you configure it


### Subnets 
- A Subnet divides a VNet into smaller logical segments.
- Each subnets has its own IP range and typically groups related resout
- Subnets allow you to apply different network policies or security rules to different parts of your application.

### NSG(Network security group)
- A Network Security Group acts as a virtual firewall for your Azure resources.
- A network security group is a firewall-like component that controls inbound and outbound traffic 	to resources in a VNet or Subnets.
- You define security rules in NGS on the basis of IP, port and subnets.
- Structure of NSG
	- Priority
	- Name
	- Direaction
	- Protocol(TCP, UDP or Any)
	- Soucer/Destination (IP address, CIDR, tag or subnets)
	- Source/Destination port(e.g., 80 for HTTP, 443 for HTTPs)
	- Action(Allow or Deny)

### Private Endpoint
- A private endpoint a private IP address inside your VNet that securly connect with Azure services(like Blob storage, SQL database, Key Vaults).
- It keep the traffic on azure private network instead of going over the public internet.

