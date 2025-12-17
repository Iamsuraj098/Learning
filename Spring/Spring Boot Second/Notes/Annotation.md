### Annotation

An **annotation** is metadata that you attach to code elements such as classes, methods, variables, parameters, or packages.
It does not directly affect how the code runs, but it provides extra information that can be used by the compiler, tools, or frameworks (like Spring).

---

### Commonly Used Spring Annotations

**@Component**

* Class-level annotation.
* Marks a class as a Spring-managed bean.
* Spring automatically detects and creates an object (bean) of this class and puts it into the `ApplicationContext`.
* No need to manually create the object using `new`.
* Best practice: inject dependencies using a constructor instead of field injection.

**@Bean**

* Method-level annotation, used inside a `@Configuration` class.
* Defines and returns a Spring bean.
* Useful when you cannot use `@Component` (e.g., third-party classes).
* Ensures the bean is created and managed by the Spring container.

**@Autowired**

* Used for **dependency injection (DI)**.
* Tells Spring to automatically inject a matching bean into another bean.
* Eliminates the need to create objects manually.
* Can be used on constructors, fields, or setter methods.

**@Configuration**

* Class-level annotation.
* Marks a class as a source of bean definitions.
* Methods inside it, annotated with `@Bean`, define beans.
* Spring ensures that each bean is created only once (singleton by default), even if the method is called multiple times.
* A single `@Configuration` class can define multiple beans.

**@Controller**

* Specialized version of `@Component`.
* Used in Spring MVC for handling web requests.
* Spring maps HTTP requests to methods in a `@Controller` class (using annotations like `@RequestMapping`, `@GetMapping`, etc.).
* Also participates in view resolution (returning a view name for rendering).

**@RestController**

* Specialized version of `@Controller`, used for building RESTful web services.
* Combines `@Controller` and `@ResponseBody`.
* Methods return data directly (usually JSON or XML) instead of a view.

**@Service**

* Specialized version of `@Component`.
* Indicates that the class holds **business logic**.
* Using `@Service` improves readability and clarifies the role of the class.

**@Repository**

* Specialized version of `@Component`, used for the **data access layer (DAO classes)**.
* Provides a mechanism for translating database-related exceptions into Spring’s `DataAccessException` hierarchy.
* Simplifies exception handling in database operations.
