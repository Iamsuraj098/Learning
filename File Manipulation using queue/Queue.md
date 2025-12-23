## Queue in Data Structure

A **queue** is a linear data structure that follows the **FIFO** principle:

**First In, First Out**

The element added first is removed first, similar to a real-world waiting line.

---

## Basic Operations

1. **Enqueue**

   * Adds an element to the rear (end) of the queue.

2. **Dequeue**

   * Removes an element from the front of the queue.

3. **Front / Peek**

   * Returns the front element without removing it.

4. **Rear**

   * Returns the last element.

5. **isEmpty**

   * Checks whether the queue is empty.

6. **isFull**

   * Checks whether the queue is full (mainly for fixed-size queues).

---

## Queue Representation

### 1. Using Array

* Elements are stored in a fixed-size or dynamic array.
* Simple to implement.
* May cause unused space in a simple array-based queue.

### 2. Using Linked List

* Each element points to the next element.
* No size limitation.
* Enqueue at the tail, dequeue from the head.

---

## Types of Queue

1. **Simple Queue**

   * Basic FIFO queue.

2. **Circular Queue**

   * Last position connects back to the first.
   * Efficient use of memory.

3. **Priority Queue**

   * Each element has a priority.
   * Higher priority elements are dequeued first.

4. **Double-Ended Queue (Deque)**

   * Insertion and deletion allowed at both ends.

---

## Example (Conceptual)

Queue state after operations:

* Enqueue: A, B, C
* Queue: `A → B → C`
* Dequeue:
* Removed element: A
* Queue: `B → C`

---

## Time Complexity

| Operation | Time Complexity |
| --------- | --------------- |
| Enqueue   | O(1)            |
| Dequeue   | O(1)            |
| Peek      | O(1)            |

---

## Applications of Queue

* CPU task scheduling
* Print queue
* Breadth-First Search (BFS)
* Message queues (RabbitMQ, Kafka)
* File and job processing pipelines

---

## Key Characteristics

* Ordered structure
* FIFO access
* Efficient for sequential processing
* Widely used in distributed systems and background processing

---

## Real World Example

Project - Custom Agentic framework

Open source library for queue - 

### Distributed / Messaging Queue Systems

These provide scalable queues for inter-process or distributed systems:

1. **Celery (Python task queue)**

   * A distributed task queue for asynchronous processing in Python applications. ([Wikipedia][7])

2. **ZeroMQ**

   * A lightweight messaging library that supports queue-like message passing without a central broker. ([Wikipedia][8])

3. **BlazingMQ**

   * An open source high-performance message queue system with client libraries in several languages. ([GitHub][9])

4. **RabbitMQ**

   * A widely used open source message broker that implements messaging queues with support for many protocols (via AMQP). ([Design Gurus][10])

5. **Apache ActiveMQ**

   * Open source, multi-protocol message broker useful for enterprise queueing and messaging. ([Design Gurus][10])

6. **Apache Kafka**

   * Distributed streaming platform with durable publish/subscribe queues suitable for high-throughput data pipelines. ([Task Queues][11])

### How implement in project ?
Redis enqueue - 
A Redis queue is a messaging pattern built on top of Redis data structures, most commonly Lists or Streams, to pass tasks from producers to workers.

It is not a separate product. It is an architectural pattern using Redis as a fast, in-memory data store.

Is Redis Queue Scalable?
Yes, Redis queues are scalable, with some limits.
- Horizontal scaling (Workers): 
	You can run many workers in parallel.
	- 1 queue
	- N workers
	- Redis ensures one task goes to one worker
	- This scales very well for CPU-bound or IO-bound jobs.

