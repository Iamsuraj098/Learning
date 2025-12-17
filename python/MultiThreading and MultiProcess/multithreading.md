#### What is a Thread in Python?

- A thread is the smallest unit of execution within a process.

- In Python, you create threads using the threading module.

- Threads allow multiple tasks to run "concurrently" within the same process.

- But due to the Global Interpreter Lock (GIL) in CPython, only one thread runs Python bytecode at a time.
    - Useful mainly for I/O-bound tasks (like network calls, file I/O), not CPU-heavy work.

---

#### Why do we use Threads?

- To perform concurrent tasks (overlapping execution).

- Best for:

    - Network requests (e.g., calling APIs in parallel)

    - Reading/writing files

    - Handling multiple client connections (servers)

    - Not good for CPU-heavy tasks in Python (because of GIL). Use multiprocessing instead for that.

---

#### What is a ThreadPool?

- A thread pool is a collection of pre-created worker threads.

- Instead of manually creating/destroying threads, you submit tasks to a pool, and it assigns them to available threads.

- In Python, implemented via concurrent.futures.ThreadPoolExecutor.

- It automatically manages threads, queues tasks, and reuses existing threads.

---
#### Difference: Thread vs ThreadPoolExecutor
| Aspect              | Thread                                                    | ThreadPoolExecutor                                       |
| ------------------- | --------------------------------------------------------- | -------------------------------------------------------- |
| **Creation**        | You manually create each thread using `threading.Thread`. | Threads are created & managed automatically.             |
| **Reuse**           | Each thread is one-time use (after `.join()`, it’s done). | Worker threads are reused for multiple tasks.            |
| **Management**      | You must start, join, and track threads yourself.         | Executor handles queuing, scheduling, and shutting down. |
| **Scalability**     | Harder to scale if you need hundreds of threads.          | Efficient for running many small tasks.                  |
| **Code simplicity** | More boilerplate.                                         | Cleaner, easier, and less error-prone.                   |

---

#### What is a Worker Thread?

- A worker thread is simply a thread that performs some task in the background.

- Instead of the main thread doing everything, you delegate work to worker threads.

- In Python, you don’t usually create “worker” threads explicitly by name — it’s just a role: a thread that picks up jobs and executes them.

---

#### In Short
- A thread = a unit of execution.

- A worker thread = a thread dedicated to executing tasks (often from a queue).

- A ThreadPoolExecutor manages multiple worker threads automatically.

---

#### How a Multithreading work ?

We know that a process have multiple thread, 
- In synchronous way, a single process create a single thread at a time and all the task are run over it one by one on same thread.
- In Asynchronous way, a single process create multiple thread at a time but still at a time single thread run and use python bytecodes at a time. But if a task take long time to execute then process create the thread and put it in waiting until its turn not comes.