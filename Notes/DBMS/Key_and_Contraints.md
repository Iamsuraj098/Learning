## Keys and Contraints
Keys and Contraints are used to maintain the data integrity, accuracy and consistency in tables.

### 1. Keys in DBMS
A key is an attribute used to identify rows uniquely in a table or to establish relationships between the tables:
#### a. Super Key
A Super Key is a set of one or more attributes that can uniquely identify a row in a table.
Example table: Students

| Student_ID | Email                             | Name  |
| ---------- | --------------------------------- | ----- |
| 101        | [a@gmail.com](mailto:a@gmail.com) | Ram   |
| 102        | [b@gmail.com](mailto:b@gmail.com) | Shyam |

Possible Super Keys: Stuent_ID Emai (Student_ID, Email)
Notes - A super key may contain unnecessary attributes.

#### b. Candidate Key
A candidate key is a minimal super key.
This means:
- It uniquely identifies each record.
- It does not contain unnecessary attributes.
Example:
Candidate Keys: Student_ID Email

Notes: Both uniquely identify students.

#### c. Primary Key
A primary key is the candidate key selected to uniquely identify each records in a table.
Properties:
- Must be unique
- Cannot contains NULL
- Only one primary key per table
Examples:
```
Students
---------
Student_ID (Primary Key)
Name
Email
```
Here Student_ID uniquely identifies every student.

#### d. Alternate Key
Candidate keys not chosen as the primary key are called Alternate Keys.
Example:
Candidate Keys:
- Student_ID
- Email
If Student_ID is primary key, then Alternate Key is Email

#### e. Composite Key
A composite key is a primary key formed using two or more attributes.
Example table:
Table name- Student_course

| Student_ID | Course_ID |
| ---------- | --------- |
| 101        | C1        |
| 101        | C2        |
| 102        | C1        |

Primary Key = (Student_ID, Course_ID)
Because:
- Student_ID alone is not unique
- Course_ID alone is not unique
- Together they are unique

#### f. Foreign Key
A Foreign Key is an attribute in one table that refers to the primary key of another table.
It is used to maintain relationships between tables.

Example:
Table 1: Students

| Student_ID | Name  |
| ---------- | ----- |
| 101        | Ram   |
| 102        | Shyam |

Table 2: Orders

| Order_ID | Student_ID |
| -------- | ---------- |
| 1        | 101        |
| 2        | 102        |

Here:
```
Orders.Student_ID → Foreign Key
Students.Student_ID → Primary Key
```
Purpose:
- Maintain referential integrity
- Prevent invalid references.

---
## Constraints in DBMS
Constraints are rules applied to columns in a table to restrict the type of data that can be inserted.
They ensure valid and consistent data.

#### a. NOT NULL Contraint
Ensures a column cannot contain NULL values.
Example:
```
CREATE TABLE Students (
    Student_ID INT,
    Name VARCHAR(50) NOT NULL
);
```

#### b. UNIQUE Contraint
Ensures all values in a column are different.
Example:
```
CREATE TABLE Users (
    User_ID INT,
    Email VARCHAR(100) UNIQUE
);
```

#### c. PRIMARY KEY Constraint
Combines UNIQUE + NOT NULL.

Example:
```
CREATE TABLE Students (
    Student_ID INT PRIMARY KEY,
    Name VARCHAR(50)
);

```

#### d. FOREIGN KEY Constraint
Maintains referential integrity between tables.

Example:
```
CREATE TABLE Orders (
    Order_ID INT,
    Student_ID INT,
    FOREIGN KEY (Student_ID) REFERENCES Students(Student_ID)
);
```

#### e. CHECK Contraint
Ensures values satisfy a specific condition.

Example:
```
CREATE TABLE Employees (
    Age INT CHECK (Age >= 18)
);
```
#### f. DEFAULT Contraint
Assigns a default value when no value is provided.
Example:
```
CREATE TABLE Orders (
    Status VARCHAR(20) DEFAULT 'Pending'
);
```

#### g. INDEX Contraint
An index improves query performance by speeding up data retrieval.

Example:
```
CREATE INDEX idx_student
ON Students(Name);
```





























