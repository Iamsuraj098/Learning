# Types of SQL Command
1. DDL - Data Definition Language
2. DML - Data Manipulation Language
3. DQL - Data Query Language
4. DCL - Data Control Language
5. TCL - Transaction Control Language


### DDL - Data Definition Language
DDL is used to define or modify the structure of database objects such as tables, schemas and indexes.
These commands affect the database schema.

| Command  | Purpose                         |
| -------- | ------------------------------- |
| CREATE   | Creates a database object       |
| ALTER    | Modifies structure of an object |
| DROP     | Deletes an object               |
| TRUNCATE | Removes all rows from a table   |
| RENAME   | Renames a table or object       |

Example - 
```
CREATE TABLE employee (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT
);
```
Note - Important characteristics: Changes the structure of the database. Often auto-committed in many databases

---

### DML - Data Manipulation Language
DML is used to insert, update, delete or modify the data stored in tables.
Comman DML commands:

| Command | Purpose                |
| ------- | ---------------------- |
| INSERT  | Adds new data          |
| UPDATE  | Modifies existing data |
| DELETE  | Removes data           |

Example:
```
INSERT INTO employee VALUES (1, 'Rahul', 50000);
```
**Note:**  Characteristics: Works on table data, Can be rolled back using transactions

---

### DQL - Data Query Language
DQL is used to retrive the data from the database.

Main Command: 

| Command | Purpose    |
| ------- | ---------- |
| SELECT  | Fetch data |

Example:
```
SELECT * FROM employee;
```
It can also include: WHERE, GROUP BY, ORDER BY, HAVING, JOIN

---

### DCL - Data Control Language
DCL controls user access and permissions in the database.

Common commands:

| Command | Purpose                   |
| ------- | ------------------------- |
| GRANT   | Gives privileges to users |
| REVOKE  | Removes privileges        |

Example - 
```
GRANT SELECT, INSERT ON employee TO user1;
```

---

### TCL - Transaction Control Language
TCL manages the database transactions.
A transaction is a group of SQL operations executed as a single unit.

Common Commands:

| Command   | Purpose                                   |
| --------- | ----------------------------------------- |
| COMMIT    | Saves changes permanently                 |
| ROLLBACK  | Undo changes                              |
| SAVEPOINT | Creates a checkpoint inside a transaction |

Example:

```
BEGIN;

UPDATE employee
SET salary = salary + 1000; 
ROLLBACK;
```

---

Summary - 

| Category | Purpose                    | Examples               |
| -------- | -------------------------- | ---------------------- |
| DDL      | Defines database structure | CREATE, ALTER, DROP    |
| DML      | Modifies data              | INSERT, UPDATE, DELETE |
| DQL      | Retrieves data             | SELECT                 |
| DCL      | Controls permissions       | GRANT, REVOKE          |
| TCL      | Manages transactions       | COMMIT, ROLLBACK       |

