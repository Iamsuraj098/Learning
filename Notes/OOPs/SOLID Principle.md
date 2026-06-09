## SOLID Principle
SOLID is a set of 5 object-oriented design principles introduced by Robert C. Martin to make software easier to maintain, extend, test, and understand.

S - Single Responsibility Principle (SRP)

O - Open/Closed Principle (OCP)

L - Liskov Substitution Principle (LSP)
 
I - Interface Segregation Principle (ISP)

D - Dependency Inversion Principle (DIP)


---

### S - Single Responsibility Principle (SRP)

**A class should have only one reason to change.**

A class should have one responsibility and do one job well.

### Bad Example

```python
class Employee:

    def calculate_salary(self):
        pass

    def save_to_database(self):
        pass

    def generate_report(self):
        pass
```

Problems:

* Salary calculation
* Database operations
* Report generation

Three separate responsibilities in one class.

---

### Good Example

```python
class SalaryCalculator:
    def calculate_salary(self):
        pass


class EmployeeRepository:
    def save(self):
        pass


class ReportGenerator:
    def generate(self):
        pass
```

Now each class has a single responsibility.

### Benefit

If database logic changes:

```text
EmployeeRepository changes
```

Other classes remain untouched.

---

### O - Open/Closed Principle (OCP)

**Software entities should be open for extension but closed for modification.**

You should be able to add new functionality without changing existing code.

### Bad Example

```python
class Payment:

    def pay(self, payment_type):

        if payment_type == "card":
            print("Card Payment")

        elif payment_type == "upi":
            print("UPI Payment")
```

Suppose tomorrow:

```text
Net Banking
Wallet
Crypto
```

Every time you modify this class.

---

### Good Example

```python
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class CardPayment(Payment):

    def pay(self):
        print("Card Payment")


class UPIPayment(Payment):

    def pay(self):
        print("UPI Payment")
```

Usage:

```python
payment = UPIPayment()
payment.pay()
```

Adding a new payment type:

```python
class WalletPayment(Payment):
    def pay(self):
        print("Wallet Payment")
```

No existing code changes.

### Benefit

New features can be added safely.

---

### L - Liskov Substitution Principle (LSP)

**A child class should be able to replace its parent class without breaking the program.**

### Bad Example

```python
class Bird:

    def fly(self):
        pass


class Penguin(Bird):

    def fly(self):
        raise Exception("Penguins cannot fly")
```

Usage:

```python
bird = Penguin()
bird.fly()
```

Crash.

The child violates expectations of the parent.

---

### Good Example

```python
class Bird:
    pass


class FlyingBird(Bird):

    def fly(self):
        pass


class Sparrow(FlyingBird):
    pass


class Penguin(Bird):
    pass
```

Now the hierarchy matches reality.

### Benefit

Inheritance remains safe and predictable.

---

### I - Interface Segregation Principle (ISP)

**Clients should not be forced to depend on methods they do not use.**

Create small, focused interfaces instead of large ones.

### Bad Example

```python
from abc import ABC, abstractmethod

class Worker(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass
```

Robot implementation:

```python
class Robot(Worker):

    def work(self):
        print("Working")

    def eat(self):
        raise Exception("Robot doesn't eat")
```

Problem:
Robot is forced to implement `eat()`.

---

### Good Example

```python
class Workable(ABC):

    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):

    @abstractmethod
    def eat(self):
        pass
```

Human:

```python
class Human(Workable, Eatable):

    def work(self):
        pass

    def eat(self):
        pass
```

Robot:

```python
class Robot(Workable):

    def work(self):
        pass
```

### Benefit

Classes implement only what they need.

---

### D - Dependency Inversion Principle (DIP)

**High-level modules should not depend on low-level modules. Both should depend on abstractions.**

---

### Bad Example

```python
class MySQLDatabase:

    def save(self):
        print("Saved in MySQL")


class UserService:

    def __init__(self):
        self.db = MySQLDatabase()
```

Problem:

```text
UserService directly depends on MySQL.
```

If you switch to MongoDB:

```text
Modify UserService.
```

---

### Good Example

```python
from abc import ABC, abstractmethod

class Database(ABC):

    @abstractmethod
    def save(self):
        pass
```

Implementations:

```python
class MySQLDatabase(Database):

    def save(self):
        print("MySQL")


class MongoDatabase(Database):

    def save(self):
        print("MongoDB")
```

Service:

```python
class UserService:

    def __init__(self, db):
        self.db = db

    def save_user(self):
        self.db.save()
```

Usage:

```python
service = UserService(MySQLDatabase())
service.save_user()

service = UserService(MongoDatabase())
service.save_user()
```

### Benefit

Easy testing and swapping implementations.

---

### Real-World FastAPI Example

Given your FastAPI/FHIR projects:

### Bad

```python
class PatientService:

    def create_patient(self):

        # Validate
        # Save MySQL
        # Call FHIR
        # Send Email
```

One class doing everything.

---

### Better Design

```python
PatientValidator
PatientRepository
FHIRClient
EmailService
PatientService
```

`PatientService` coordinates them.

This follows:

* SRP → Separate responsibilities
* OCP → Add new notification types
* DIP → Depend on interfaces
* ISP → Small contracts
* LSP → Safe inheritance

---

### Quick Interview Definitions

| Principle | Meaning                                              |
| --------- | ---------------------------------------------------- |
| SRP       | One class, one responsibility                        |
| OCP       | Open for extension, closed for modification          |
| LSP       | Child should safely replace parent                   |
| ISP       | Small, focused interfaces                            |
| DIP       | Depend on abstractions, not concrete implementations |

A common way to remember SOLID:

```text
S → One Responsibility
O → Extend, don't modify
L → Child behaves like Parent
I → Small Interfaces
D → Depend on Abstractions
```

When designing APIs, services, repositories, FHIR clients, database layers, and notification systems, SOLID principles help keep the codebase maintainable as it grows.
