### IoC
Stands for *Inversion of Control*

Inversion of Control (IoC) is a design principle in which control of object creation and management is transferred from the program (developer) to a framework or container, like Spring.

---
| Without IoC (Traditional)                        | With IoC (Spring)                                        |
| ------------------------------------------------ | -------------------------------------------------------- |
| You create objects manually using `new` keyword. | Objects are created and managed by the Spring container. |
| You control dependencies.                        | Dependencies are injected automatically.                 |
| Code is tightly coupled.                         | Code is loosely coupled and more testable.               |

---
### How IoC Works in Spring ?
Spring uses an IoC Container (also called ApplicationContext) to:
   1. Create objects (beans)
   2. Manage their lifecycle
   3. Inject dependencies

---
Most frequently used annotations:
1. @Service
2. @autowired - when multiple constructor are used in single class then we use the autowired so spring can segregate the constructor.