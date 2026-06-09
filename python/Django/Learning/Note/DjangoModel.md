## Django Models
Django Models are Python classes that represent the database structure of your application.

Each model:
- Maps to a database table
- Each attribute maps to a table column
- Django automatically handles database operations using ORM (Object Relational Mapper)

---

#### Why Django Models are Used
- No need to write raw sql queries
- Database Indepenedent
- Cleaner, safer, and maintainable code
- Automatic table creation & migrations
- Built-in validation

---

#### Common Model Fields

| Field Type                 | Purpose          |
| -------------------------- | ---------------- |
| `CharField`                | Small text       |
| `TextField`                | Large text       |
| `IntegerField`             | Numbers          |
| `FloatField`               | Decimal values   |
| `BooleanField`             | True/False       |
| `DateField`                | Date             |
| `DateTimeField`            | Date & Time      |
| `EmailField`               | Email validation |
| `FileField` / `ImageField` | File storage     |

---

#### What is ORM ?

ORM(Object Relation Mappings) allows you to interact with the database using python objects instead of sql queries.

Example:
```
User.objects.filter(age__gt=25)
```
Internally what happen - 
```
SELECT * FROM user WHERE age > 25;
```

---

#### Step-by-Step: How Django ORM Works Internally
1. Model Definition - Metadata creation
2. Query creation
3. Query Set - SQL Compilation
4. Database Backend & Driver
5. Query Execution
6. Result Mapping (Row - Object)

---

#### How efficient is ORM in Django
ORM is efficient for most complex queries, but for very complex, higly optimized or database specific queries, raw sql can be more efficient and readable.

ORM Limitations for Complex Queries

| Scenario                     | Reason                 |
| ---------------------------- | ---------------------- |
| Very complex nested queries  | Hard to read           |
| DB-specific features         | ORM abstraction limits |
| Heavy window functions       | Limited ORM support    |
| Performance-critical queries | Raw SQL faster         |
| Bulk operations              | ORM overhead           |
