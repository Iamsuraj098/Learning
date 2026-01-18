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
