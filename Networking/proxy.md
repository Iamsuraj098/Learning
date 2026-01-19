# Proxy

A Proxy is intermediate server or application that sits between a client and
destination server. It forward the requset and response between them.

#### Now where Proxy lies in the server to client web flow (Refer to simpleWebWorkflow.md file)
```
  User (Browser)
      ↓
  Forward Proxy
      ↓
   Internet
      ↓
[ Reverse Proxy / Gateway ]
      ↓
   Backend Server (API)
      ↓
   Database
```

---
#### Step-by-Step with Proxy in Context

**User connects to the internet**
The user’s browser is connected via their ISP and can reach public servers.

**User enters the domain**
The browser resolves the domain (e.g., app.example.com) via DNS.

**DNS returns the IP address of the proxy server**
Importantly, most domains actually point to the proxy or load balancer, not directly to your backend server.

**Browser establishes TCP/TLS connection with the proxy**
The browser connects (e.g., HTTPS port 443) to the proxy server, not directly to the backend.

**Proxy receives HTTP request**
The proxy (e.g., Nginx, Traefik, or Cloudflare) accepts the incoming HTTP request.

**Proxy decides where to route it**
Based on configuration or rules:

- / → serve frontend static files from disk (HTML, CSS, JS)
- /api → forward to backend service (FastAPI, Node.js, etc.)

**Frontend serving**
If it’s a frontend request (/index.html), the proxy serves those files directly.

**Backend routing**
If it’s an API request (/api/bookAppointment), the proxy forwards the request internally to your backend container or service.

**Backend processes and responds**
The backend handles business logic, queries the database, and sends back the response (JSON, etc.) to the proxy.

**Proxy relays the response to the client**
The proxy takes the backend’s response and sends it back to the browser over the same TCP connection.

**Browser receives and updates UI**
The browser receives the data packets, reassembles them, and updates the UI accordingly.

---
## Forward and Backward Proxy
client <-> forward proxy <-> internet <-> reverse proxy <-> server

### What is Forward Proxy ?
A forward proxy (also called a "proxy server") is a server that sits between client devices and the internet. When a client sends a request to access a website or online resource, the request is directed to the forward proxy first. The proxy then forwards the request to the destination server on behalf of the client.

#### Usage of Forward Proxy
- Enhancing client anonymity
- Accessing geo-blocked or restricted content
- Content filtering and monitoring in organizations
- Reducing bandwidth consumption through caching
- Logging and tracking user activity for compliance

### What is Reverse Proxy ?
A reverse proxy works the opposite of a forward proxy. While a forward proxy acts on behalf of the client, a reverse proxy acts on behalf of the server. **It is used to protect and manage servers by ensuring that clients do not directly communicate with the origin server**.
#### Use Cases of Reverse Proxy
- Load balancing across multiple web servers
- Caching content to improve server performance
- Protecting backend servers from direct exposure to the internet
- SSL/TLS offloading to improve server efficiency
- Mitigating DDoS attacks and enhancing security
---

| Type                             | Description                                                                                                                                                    |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Forward Proxy**                | Used by clients to access external resources. Common in organizations to control internet usage or cache data.                                                 |
| **Reverse Proxy**                | Used by servers to manage incoming requests. It sits in front of backend servers to handle load balancing, caching, or SSL termination (e.g., Nginx, HAProxy). |
| **Transparent Proxy**            | Users are unaware it exists; used for content filtering or monitoring.                                                                                         |
| **Anonymous Proxy**              | Hides the client’s IP address for privacy.                                                                                                                     |
| **High Anonymity Proxy (Elite)** | Makes it appear as if there’s no proxy at all.                                                                                                                 |
| **SOCKS Proxy**                  | Works at a lower network level and can handle any type of traffic (TCP/UDP). Common for gaming or P2P.                                                         |
| **HTTP/HTTPS Proxy**             | Works specifically with web traffic.                                                                                                                           |

---

**Note:**

Client → Proxy Server
- The request originates from the client’s IP (for example, 203.0.113.25) and reaches the proxy server.
- The proxy server sees this IP as the client IP.
	
Proxy Server → Destination Server (e.g., your backend)
- The proxy server then creates a new outgoing request to the actual destination (for example, your app server).
- This new request originates from the proxy’s own IP address, not the client’s.
- Therefore, your server only sees the proxy’s IP (for example, 10.0.0.15 or some public proxy IP).
---

#### Difference between Proxy and Firewall.
| Feature           | **Firewall**                               | **Proxy**                                     |
| ----------------- | ------------------------------------------ | --------------------------------------------- |
| **Main job**      | Blocks or allows network traffic           | Sends requests to the internet on your behalf |
| **Works on**      | Network level (IP, port)                   | Application level (web, email, etc.)          |
| **Purpose**       | Protects your network from attacks         | Controls or hides what users access online    |
| **Traffic type**  | Both incoming and outgoing                 | Usually outgoing (from users to internet)     |
| **Example use**   | Blocks hackers from reaching your computer | Blocks users from opening certain websites    |
| **Visibility**    | Sees network packets                       | Sees full web requests and responses          |
| **Caching**       | No                                         | Yes, can store and reuse web pages for speed  |
| **User identity** | Doesn’t know user details                  | Can track or authenticate users               |
