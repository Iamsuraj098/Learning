# Memory Mangement in Python

Python automatically creates, tracks, and frees memory using reference counting and garbage collection, so developers do not manage memory manually.

We do not manually allocate memory like we do in C/C++.

---

### Reference Counter in Python: 

- Refernce counter are the number that tells how many variables are pointing to the same object in memory.
- Python use this count to decide when to free memory.
- When the counter is zero then python frees the objects.

#### Limitation of Reference Counter:
- Reference counter can not handle the circular references. This is why python uses the *Garbage Collector*

---

### Private Memory Management

- Python manage its own memory internally dosen't depend on the operating system for every object.
- Explanation:
  - When program create the objects, Python dosen't ask the OS for memory every time.
  - Takes a large chunk of memory from the OS
  - Manages that memory by itself
  - Reuses it for Python objects
- This internal memory area is called the **Python private heap**.

#### Why does Python use private memory?
- Faster Object Creation
- Less overhead from OS call
- Better performance for small object

#### PyMalloc is used to create the Private Memory Management
- Python uses PyMalloc for small objects (usually less than 512 bytes).
``` 
Operating System
 └── Python Private Heap
       ├── Arenas
       ├── Pools
       └── Blocks
```

- Arena: Large Memory Chunk 
- Pool: Divided from arena
- Block: Given to individual object
  
#### Important point to remember
Even after deleting the object memory not return to OS, It stay in the python for reuse.

#### In single line:
Private memory management in Python means Python uses its own internal memory allocator (private heap) to efficiently allocate and reuse memory instead of requesting memory from the OS for every object.

---

### Garbage Collection in Python

Garbage collection is the process by which Python automatically frees memory that is no longer being used by the program.

#### Why garbage collection is needed
Basically python used the refernce counter but when circular reference it will get stuck.
To solve this problem garbage collection in the picture.

#### How garbage collection works
- Finds the objects involve in circular reference
- Checks if they are unreachable from the program
- Frees the memory
  
#### Using the **GC** module we can control the garbage collector

```
import gc

gc.collect()     # Run GC manually
gc.disable()     # Turn off GC
gc.enable()      # Turn on GC
```

#### Important points

- Garbage collection is automatic
- You usually do not need to control it
- Reference counting + garbage collection work together
- GC mainly handles circular references

---

## Who decides whether an object lives or is deleted?

Python runtime (CPython) decides this.
It uses two mechanisms together:
- Reference counting (primary decision maker)
- Garbage collector (backup for circular references)

---

### when the python release the private memory heap
Python almost never releases its private memory heap back to the operating system while the program is running.
The private heap is usually released only when the Python process exits.

---

### Satiuation when OS comes to manage the memory
- Large memory blocks (OS-managed allocations)
- Very large objects (e.g., large lists, NumPy arrays)
- Sometimes allocated directly via OS malloc
- These may be returned to the OS