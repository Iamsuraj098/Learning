# ACID
It garunteed that database transactions are processed reliably and maintain data integrity.

ACID stands for 
- A: Atomicity
- C: Consistency
- I: Isolation
- D: Durability

---

### Atomicity
Atomicity means a transaction is treated as single unit.
- Either all operation executed or non of them executed.
- if any part fails them entire trnasaction is rolled back.
Example:
```
Transfer ₹100 from Account A to Account B
```
Steps:
```
Deduct ₹100 from A
Add ₹100 to B
```
If the system crashes after step 1 but before step 2, atomicity ensures the deduction is undone.
Result:
- Either both happen
- Or neither happens
--- 
### Consistency
Consistency means the database always moves from one valid state to another valid states
It garunteed that database rules, contraints and relationships are not voilated.
Example constraints:
- Primary key
- Foreign key
- Unique constraints
- Check constraints

Example:
If a table requires age ≥ 0, inserting:
```
age = -5
```
will be rejected to maintain consistency.

---
### Isolation
Isolation ensures that multiple transaction running at same time do not interfere with each other.
Each transaction behaves as if it is only transaction running in the system.
Example:
Two users updating the same bank account simultaneously.
Without isolation:
```
One update may overwrite another.
```
With isolation:
```
Transactions are controlled using locks or isolation levels.
```
Common isolation levels:
- Read Uncommitted
- Read Committed
- Repeatable Read
- Serializable
---
### Durability
Durability guarantees that once a transaction is commited, the data is permanately store, even if:
- System crashes
- Power failure occurs
- Server restarts

This is ensured using:
- Transaction logs
- Checkpoints
- Disk storage

Example:
If a transaction commits and the system crashes immediately after, the data will still exist when the database restarts.