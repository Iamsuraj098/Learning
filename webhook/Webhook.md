### Webhook

A webhook is a mechanism that allows one system to automatically notify another system when a specific event happens.
Instead of repeatdly asking a system whether something is changed, the system sends predefined url as soon as event occure. This makes communication event-driven, real-time and efficient.

Note: Webhooks are server-to-server communication.

Importent point - 
- Webhook requests are triggered by backend systems
- Webhook endpoints are always backend APIs
- Frontend is not “always ready” and is not part of webhook receiving
	- Explaining this point: The frontend does not need to be ready at the moment the event happens.
		The backend stores the update, and the frontend fetches it later or is notified indirectly.
	- Frontend applications:	
		- Frontend runs only when 
		- Run only when a user opens them. 
		- Can be closed, refreshed, or offline

Cannot guarantee availability at the exact moment an external event occurs
- Think of webhooks as backend event notifications
---
#### Core Idea of Webhook
A webhook works on a "push" model.
When an event occurs in System A, it immediately sends a message to System B. System B does not need to poll or check System A continuously. It simply waits for notifications.

In simple terms:
“Tell me when something happens, and send me the details immediately.”

---
#### Problems which are solved by the webhooks:
Webhooks solve several common problems:
- Real Time Updated
	- Instant message delivery
- Reduce Load
	- They eliminate frequent polling, saving network acrocss platform.
- Automation
	- They allow system to automatically trigger workflows across platform.
- Decoupled systems
	- Each system can operate independently while still staying in sync.

---

Webhook v/s polling
- Polling:
	- System B repeatedly asks System A, “Has anything changed?”
	- Causes unnecessary requests when nothing changes.
	- Slower and less efficient.

- Webhook:
	- System A informs System B only when something changes.
	- Fewer requests and near-instant updates.
	- More scalable.

---

#### Some Real World Scenario

##### Scenario 1: Online payment processing

- An e-commerce platform uses a payment gateway.
	- A customer completes a payment.
	- The payment gateway triggers a webhook event called “payment_success”.
	- The webhook sends payment details to the e-commerce platform.
	- The platform marks the order as paid, generates an invoice, and sends a confirmation email.
- Without webhooks, the platform would have to constantly check the payment gateway to see if the payment succeeded.

##### Scenario 2: Healthcare systems
- A hospital system integrates with a lab service.
	- A lab test result is finalized.
	- The lab system triggers a webhook event.
	- The hospital system receives the notification.
	- The doctor is alerted and the patient record is updated.
- This reduces delays in clinical decision-making.

---

#### After Processing Webhook what happens:
- What actually happens when a webhook arrives
	- When a webhook event occurs:
	- External system sends webhook request
	- Your backend receives it
	- Your backend processes the event
	- Your backend updates persistent storage (database, cache, file system)
	
At this point, the update is safely stored.

- It does not matter whether:
	- Any frontend is open
	- Any user is online
	- Any browser is active
	- How frontend eventually shows the update
		- Frontend fetches latest data when opened
		- Periodic refresh or polling
		- Real-time push from backend (WebSocket / SSE)

