# Azure Level 1
## Core Fundamentals
### 1. Regions
 - A region is a geographic location where Azure has one or more data centers. Each region provides Azure services, such as virtual machines, databases, and storage, within that area.
 - Purpose: It allows you to deploy resources close to your users for low latency, better performance and to meet data residency requirements.
 - Example: East US, West Europe, Central India
 - Note: Each region offers a different set of Azure services depending local Infrastructure.
### 2. Availability Zones
- Physically seperated data centers within a single region, each with its own power, coding and networking.
- Purpose: Provides high availability and fault tolerence within the same region.
- Example:
	- "Central India" region may have Zone 1, Zone 2, and Zone 3.
	- You can deploy your VMs in different zones to ensure that if one zone fails, others continue running.
- Benifits: Protects applications and data from data center-level failures.
### 3. Data centers
- A physical facility that houses servers, networking equipment, and storage systems that run Azure services.
- Purpose: Provides the hardware foundation for cloud computing in Azure regions.
- Details:
	- Each Azure region consists of one or more data centers.
	- Data centers are equipped with redundant power, cooling, and networking for reliability.
---
### Hierarchy
```
Azure Data Center   →  forms part of a Region
Region              →  may have multiple Availability Zones
Availability Zones  →  host multiple Data Centers
Resource Group      →  organizes your Azure resources logically
```
---

### 4. Management Groups
- A top level container used to orgnize multiple subscriptions.
- Purpose: Apply governance, policies and access control across many subscriptions at once.
- Key Points:
	- Used mostly in large organizations.
	- Can nest up to six levels deep.
	- Policies applied here automatically flow down to all subscriptions beneath it.
- Example:
	- Management Group: Healthcare-Organization
	- Subgroups: Production, Development
### 5. Subscriptions
- A logical container that holds Azure resources and defines billing boundaries.
- Purpose: 
	- Track usage and costs separately.
	- Control access and quotas (like number of VMs, CPUs, etc.).
- Key Points:
	- Each subscription is linked to one Azure account (billing entity).
	- You can have multiple subscriptions for different environments or departments.
- Example:
	- Prod-Subscription (for production workloads)
	- Dev-Subscription (for testing or development)
### 6. Resource Group
- A logical container that organizes related Azure resources that share a common lifecycle.
- Purpose:
	- Simplifies management, monitoring, and access control.
	- Enables group operations (e.g., delete all resources in one action).
- Key Points:
	- Resources in a resource group should have the same lifecycle.
	- Can’t nest resource groups inside each other.
- Example:	
	- Resource Group: HospitalApp-RG
	- Contains: Virtual Machine, Storage Account, and Database for one app.
### 7. Resources
- The individual services you use in Azure — such as VMs, Databases, Storage Accounts, Web Apps, etc.
- Purpose: Actual components that perform your workloads or host your applications.
- Examples:
	- Virtual Machine (VM1)
	- SQL Database (PatientDB)
	- Storage Account (hospitalstorage123)
---
### Hierarchy
| Level                | Description                                                   | Example                                 | Used For                                       |
| -------------------- | ------------------------------------------------------------- | --------------------------------------- | ---------------------------------------------- |
| **Management Group** | Highest level container for organizing multiple subscriptions | `Healthcare-Org`                        | Central governance and policy enforcement      |
| **Subscription**     | Defines billing and access boundary                           | `Prod-Subscription`, `Dev-Subscription` | Cost tracking, resource quotas                 |
| **Resource Group**   | Logical container for related resources                       | `HospitalApp-RG`                        | Resource organization and lifecycle management |
| **Resource**         | Actual Azure service instance                                 | VM, SQL DB, Storage                     | Running workloads                              |

---
---

## Azure App service
It is fully managed plateform for building, deploying and scaling web application and APIs.
It supports multiple languages and frameworks such as .NET, Java, Python, Node.js, PHP, and Ruby.
App Service handles infrastructure management (servers, networking, OS updates) so you can focus on your app code.

### 1. Web Apps
- Definition: A web app in Azure app service is used to host websites or web application.
- Purpose: It provides an environments to run your full-stack app with automatic scaling, load balancing, and custom domain/SSL support.
- Example: Hosting a company’s main website or a customer portal.
### 2. APIs
- API Apps are backend services hosted on App Service designed to expose RESTful endpoints.
- Purpose: They power mobile or web applications by handling data and logic behind the scenes.
- Example: An appointment booking API used by a hospital mobile app.
### 3. Deployment slot
- Deployment slots are separate live environments (like staging, testing, production) under the same App Service.
- Purpose: They allow zero-downtime deployments by testing new versions before swapping them into production
- Example:
	- Staging slot: Deploy new code here and test.
	- Production slot: Keep the live version running.
	- When ready, swap the slots to push updates live instantly.
### 4. Scaling
- Scaling determines how your app handles varying loads by adjusting compute resources.
- Types:
	- Vertical Scaling (Scale Up): Increase or Decrease the instance size (CPU, RAM).
	- Horizontal Scaling (Scale Out): Increase or Decrease the number of instances running your app.
- Modes:
	- Manual scaling: You set the instance count manually
	- Auto Scaling: Azure automatically adjusts based on metrics (CPU usage, requests, schedule, etc.).
- Example: During peak traffic hours, your app automatically scales out to handle more users.

---
| Term                | Description                                   | Example Use                     |
| ------------------- | --------------------------------------------- | ------------------------------- |
| **Web App**         | Hosts web frontends or full-stack sites       | Company website                 |
| **API App**         | Hosts backend REST APIs                       | Appointment booking API         |
| **Deployment Slot** | Staging environment for zero-downtime updates | Test before going live          |
| **Scaling**         | Adjusts resources to meet demand              | Add instances during peak hours |

---
---
## Azure Function
Azure Function is serverless compute service in Azure thats lets you run small peices of code without managing servers or Infrastructure.
You only pay for the time your code runs, and Azure automatically scales resources based on demand.
It’s ideal for event-driven applications — where code executes in response to specific events, such as a message in a queue, a file upload, or an HTTP request.
### 1. Triggers
- Definitions: A trigger defines how and when a function is executed.
- Every azure function much have exactly one triggers.
- Example:
	- HTTP Trigger: Runs when an HTTP request is received (used for APIs).
	- Timer trigger: Runs on a schedule (like a cron job).
	- Blob trigger: Runs when a file is uploaded to Azure Blob Storage.
	- Queue Trigger: Runs when a message is added to an Azure Storage Queue.
- Example: A Timer trigger that runs daily at midnight to clean up old data.
### 2. Bindings
- Definitions: Bindings simplify how your function connects to other Azure services or data sources.
- They act as input and output connectors.
- You can use multiple bindings in a single function (unlike triggers).
- Types:
	- Input Bindings: Reads data (e.g., from Cosmos DB, Blob, Queue).
	- Output Bindings: Writes data (e.g., send to a Queue, update a Database).
- Example Use: A function triggered by a new Blob file (Trigger) → reads metadata (Input Binding) → stores it in Cosmos DB (Output Binding).
### 3. Plans
Azure Functions can run on different hosting plans, which control scaling, billing, and performance.

| **Plan Type**                    | **Description**                                                            | **Scaling & Billing**                               | **Best For**                                 |
| -------------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------- |
| **Consumption Plan**             | Serverless model; Azure automatically allocates resources.                 | Pay only for execution time. Auto-scales instantly. | Irregular workloads or event-driven tasks.   |
| **Premium Plan**                 | Pre-warmed instances for no cold start; supports VNETs and longer runtime. | Pay for reserved instances + execution.             | High-performance or latency-sensitive apps.  |
| **Dedicated (App Service) Plan** | Runs on dedicated VMs (like Web Apps).                                     | Pay for VM uptime (not per execution).              | Always-on, large-scale enterprise workloads. |

---
---
### Azure Virtual Machine
An Infrastructure-as-a-Service (IaaS) offering that provides fully customizable virtualized computing resources — including CPU, memory, storage, and networking — in the Azure cloud. It allows you to run applications, host servers, or test environments just like a physical machine, but managed and scalable in the cloud.

### 1. Virtual Machine (VM)
- A virtualized computer running in Azure that you can configure with your own operating system (Windows or Linux), software, and settings.
- Purpose: Used for hosting applications, running databases, or providing development/testing environments.
- Example: Deploying a Windows Server VM to host an ASP.NET application or a Linux VM for Python APIs.
### 2. VM Sizing
- Sizing determines the compute capacity (CPU, RAM, storage, and network performance) of the VM.
- Azure offers different VM series optimized for specific workloads:

| **VM Series**  | **Optimized For**     | **Example Use Case**     |
| -------------- | --------------------- | ------------------------ |
| **A/B-series** | Entry-level, dev/test | Small workloads, demos   |
| **D-series**   | General-purpose       | Web servers, medium apps |
| **E-series**   | Memory-optimized      | Databases, analytics     |
| **F-series**   | Compute-optimized     | Batch processing, gaming |
| **N-series**   | GPU-enabled           | AI, ML, rendering        |
| **M-series**   | High memory           | SAP HANA, enterprise DBs |
- Example: A D4s_v5 VM means 4 vCPUs, 16 GB RAM, and standard SSD support.
### 3. Images
- An image is a template used to create a VM. It includes an operating system and optional pre-installed software.
- Types of Images:
	- Azure Marketplace Images: Pre-built by Microsoft or partners (e.g., Ubuntu, Windows Server, SQL Server).
	- Custom Images: Created by you to clone or replicate an existing VM setup.
	- Shared Image Gallery: A repository to store and share custom VM images across your organization.
### 4. Availability Sets
- Definition: A logical grouping of VMs that ensures high availability within a single data center.
- Purpose: Protects against hardware failures by distributing VMs across fault domains (physical racks) and update domains (software update groups).
- Example: If you have 2 VMs in an availability set, Azure ensures they are placed on different racks and updated at different times, reducing downtime.

---
| Term                     | Description                            | Purpose / Example               |
| ------------------------ | -------------------------------------- | ------------------------------- |
| **Virtual Machine (VM)** | Virtualized computer in the cloud      | Host applications or servers    |
| **Sizing**               | Defines CPU, RAM, and storage capacity | D4s_v5 for medium workloads     |
| **Image**                | Template with OS and software          | Ubuntu or Windows Server image  |
| **Availability Set**     | Group of VMs spread across racks       | Protect from hardware failure   |

---
---
### Storage account
- An storage accont is a container that holds all your storage data objects - such as Blobs, Files, Queues, and Tables.
- It provides a unique namespace (like a URL) in Azure for storing and accessing your data.
- Example:
A storage account might be named mystorageaccount, giving you an endpoint like
https://mystorageaccount.blob.core.windows.net.
- Purpose: It’s the foundation for Azure storage services and provides features like redundancy, encryption, access control, and scalability.
### 1. Blob storage
- Stands for Binary Large Object.
- It is used to store unstructure data such as images, videos, documents or backup.
- Blob Types:
	- Block Blob: For text or binary files (most common).
	- Append Blob: For data that is constantly added to (e.g., logs).
	- Page Blob: For virtual hard disks (used by Azure VMs).
- Example Use Case: Storing user-uploaded images or application backups.
### 2. File storage
- Azure File Storage provides fully managed shared file systems accessible via SMB (Server Message Block) or NFS protocols.
- Purpose:
	- Acts like a traditional file share that multiple VMs or users can access simultaneously.
- Example Use Case:
	- Hosting shared configuration files for multiple app servers.
### 3. Queue storage
- Azure Queue storage provides reliable message queuing between application component.
- Purpose: Enables asynchronous communication — one component can send a message, and another can process it later.
- Example Use Case: A web app uploads a message to a queue when a new image is uploaded, and a background function processes it later.
### 4. Table Storage
- Azure Table Storage is a NoSQL key-value store for structured data without requiring a relational schema.
- Purpose: Stores large volumes of semi-structured data quickly and cost-effectively.
- Example Use Case: Storing IoT device data, logs, or user metadata.
---
---
### Authentication (Who are you?)
- Authentication verifies the identity of a user, application, or service that’s trying to access Azure resources.
- Common Authentication methods in Azure:
	- Azure Active Directory (Azure AD/Entra Id):
		- The main identity provider for users, apps, and services in Azure.
		- Users sign in with their Azure AD credentials.
		- Applications use service principals or managed identities.
	- Managed Identities – Automatically handle identity for Azure resources (like VMs, Functions, or App Services) without managing secrets.
	- Service Principals – Non-human identities used by applications or automation tools to access Azure resources.
	- Shared Access Signatures (SAS) – Temporary, limited access tokens for services like Blob, File, or Queue Storage.
	- Access Keys – Legacy method to authenticate storage accounts using account keys (should be avoided if possible).
### Authorization (What can you do?)
- Authorization determines what operations an authenticated identity can perform.
- In Azure, authorization is managed primarily using:
	- Role-Based Access Control (RBAC)
		- Assigns roles (sets of permissions) to users, groups, or service principals.
		- Scopes: Management Group → Subscription → Resource Group → Resource
		- Example roles:
			- Owner: Full access, including permissions management.
			- Contributor: Can modify resources but not grant permissions.
			- Reader: View-only access.
	- Access Control (IAM)
		- Portal section where you assign or review RBAC roles.
	- Azure Policy (Optional enforcement layer)
		- Defines and enforces organizational rules (e.g., enforce resource tagging, restrict region usage).
	- Resource-specific permissions
		- Some services (like Blob Storage) have their own internal permission systems, such as SAS tokens or Access Control Lists (ACLs).
---
---
### Storage Redundancy
In Azure Storage, redundancy refers to how data is replicated (copied) across different locations to ensure durability, availability, and disaster recovery. Azure provides multiple redundancy options based on how critical your data is and how much you want to spend.
### 1. LRS(Locally Redundant Storage):
- Data is replicated three times within a single data center in one Azure region.
- Ensures durability against hardware failures inside that data center.
- Lowest cost option but does not protect against a data center outage (like fire or flood).
- Use Case:
	- Suitable for non-critical data or backup copies where regional failure tolerance is not required.
- Example:
	- If your storage account is in the East US region, all three copies stay within that one data center in East US.
### 2. ZRS(Zone-redundant storage)
- Data is replicated across three separate Availability Zones within the same region.
- Each zone is an independent physical location with its own power, cooling, and networking.
- Provides higher availability and resilience against a single zone failure.
- Use case:
	- Ideal for production workloads that require high availability within a single region.
	- Commonly used for applications needing read/write access even if one zone goes down.
- Example: If your account is in East US 2, copies are stored across three different zones within East US
### 3. GRS (Geo-Redundant Storage)
- Data is replicated to a secondary region, hundreds of kilometer away from the primary one.
- In each region (primary and secondary), Azure keeps three copies of the data (using LRS).
- Provides protection even if the entire primary region becomes unavailable.
---
| Feature            | LRS                  | ZRS                         | GRS                                 |
| ------------------ | -------------------- | --------------------------- | ----------------------------------- |
| Copies of Data     | 3                    | 3                           | 6 (3 local + 3 in secondary region) |
| Region             | Single data center   | Across 3 availability zones | Across 2 regions                    |
| Protection Against | Hardware failure     | Zone failure                | Regional failure                    |
| Availability       | ~99.9%               | ~99.99%                     | ~99.9% (read access optional)       |
| Cost               | Lowest               | Medium                      | Highest                             |
| Recommended For    | Non-critical backups | High availability apps      | Disaster recovery                   |

---