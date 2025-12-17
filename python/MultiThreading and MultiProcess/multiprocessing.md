### Multiprocessing

- It is a python library that used for parallel execution of task or parallel processing.
- Very Usefull for CPU bound task(heavy computations like image processing, data transformations, mathematical operations, etc.)

#### Why we use Multiprocessing ?

- Threads in python can't truely run parallely due to GLI(only one thread execute python bytecodes at a time).
- multiprocessing creates separate processes that run truly in parallel across multiple CPU cores.
- Provides a simple interface for parallel execution, inter-process communication (IPC), and synchronization.

#### Multiprocessing V/S Multithreading
| Feature       | Multiprocessing                     | Multithreading                         |
| ------------- | ----------------------------------- | -------------------------------------- |
| GIL impact    | Avoids GIL (runs in parallel)       | Affected by GIL (not true parallelism) |
| Memory        | Each process has separate memory    | Threads share same memory              |
| Best for      | CPU-bound tasks (math, ML, etc.)    | I/O-bound tasks (networking, disk I/O) |
| Communication | Requires IPC (Queue, Pipe, Manager) | Shared variables and locks             |

#### Limitations

- More memory overhead than threads (since each process has its own memory).
- Inter-process communication is slower than shared-memory threading.
- Debugging multiple processes is harder.