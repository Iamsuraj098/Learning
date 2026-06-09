### Simplified Web Request Flow - 

A user enters a domain name, the browser resolves it via DNS, establishes a TCP (or HTTPS) connection, downloads and renders the frontend code, and then communicates with the backend through HTTP requests over TCP to exchange data.

---
### Little in Details

User connected with internet.

User first enter the domain name of that server.

As it hit enter via TCP http request go to server.

Server send the frontend code in the form of packets via the TCP.

hese frontend codes are interpreted by browser and user see the UI.

After user see UI, it hit some request in the form of Http request which also go via the TCP.

In the response the server send the packets of data via TCP. 

As show on.

---

```
User → Browser
    ↓
DNS lookup → finds server IP
    ↓
TCP connection + (TLS handshake if HTTPS)
    ↓
HTTP GET request → to server
    ↓
Server → sends HTML/CSS/JS (frontend files)
    ↓
Browser renders UI
    ↓
User interacts → frontend sends API requests (HTTP over TCP)
    ↓
Backend processes → queries database
    ↓
Server sends response (JSON packets)
    ↓
Browser updates UI dynamically
```

---

### Step-by-step refined web request flow

1. **User connects to the internet** — device has network access via an ISP and routing infrastructure.
2. **User enters a domain name** — browser begins by resolving the domain (e.g., `example.com`).
3. **DNS lookup** — DNS returns the server’s IP address for the domain.
4. **Establish TCP connection** — browser opens a TCP connection to that IP on port 80 (HTTP) or 443 (HTTPS).
5. **TLS handshake (if HTTPS)** — if using HTTPS, the browser and server perform the TLS handshake to negotiate encryption.
6. **Send HTTP request** — browser sends an HTTP request (for example `GET /index.html`) over the established connection.
7. **Server responds with frontend files** — server returns HTTP response headers and body (HTML, CSS, JS, images), split into TCP packets.
8. **Browser receives and reassembles packets** — TCP/IP stack reassembles packets into the full HTTP response.
9. **Browser parses and renders** — browser parses HTML, downloads and executes JS, applies CSS, builds the DOM and render tree, and shows the UI.
10. **User interacts with the UI** — interactions trigger client-side code (routing, event handlers) and may initiate API calls.
11. **Frontend sends API requests** — JavaScript issues HTTP(S) requests (fetch/Axios) to backend API endpoints over TCP.
12. **Backend processes requests** — backend validates input, applies business logic, and queries the database as needed.
13. **Backend sends responses** — backend returns data (commonly JSON) over HTTP/TCP back to the browser.
14. **Browser updates UI** — client code consumes the response and updates the interface dynamically.
15. **Connection lifecycle** — connections may be reused (keep-alive), closed, or re-established; the loop repeats for further interactions.
