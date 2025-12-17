## 1. What is Lombok?

Lombok is a Java library that reduces boilerplate code (like getters, setters, constructors, builders, loggers).
It uses annotations and **compile-time code generation** via the annotation processor.

Instead of writing repetitive code manually, Lombok injects it during compilation.

---

## 2. How Lombok Works

* You add Lombok annotations to your classes.
* The **annotation processor** generates the corresponding methods (e.g., `getName()`, `setName(String name)`) into the compiled `.class` files.
* Your source code stays clean, but the compiled code has all the methods.

To make it work:

1. Lombok dependency in `pom.xml` (for Maven).
2. Lombok plugin in your IDE (IntelliJ, Eclipse, VS Code) so it understands generated code.

---

## 3. Commonly Used Annotations

### a) **@Getter and @Setter**

Automatically generates getters and setters for fields.

```java
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class Product {
    private Long id;
    private String name;
}
```

Generates:

```java
public Long getId() { return id; }
public void setId(Long id) { this.id = id; }
```

---

### b) **@Data**

Shortcut for:

* `@Getter`
* `@Setter`
* `@ToString`
* `@EqualsAndHashCode`
* `@RequiredArgsConstructor`

```java
import lombok.Data;

@Data
public class Product {
    private Long id;
    private String name;
}
```

---

### c) **@NoArgsConstructor, @AllArgsConstructor, @RequiredArgsConstructor**

Creates constructors:

* `@NoArgsConstructor`: no-argument constructor
* `@AllArgsConstructor`: constructor with all fields
* `@RequiredArgsConstructor`: constructor with `final` fields or fields marked `@NonNull`

```java
@NoArgsConstructor
@AllArgsConstructor
@RequiredArgsConstructor
public class Product {
    private Long id;
    @NonNull private String name;
}
```

---

### d) **@Builder**

Implements the Builder pattern.

```java
import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class Product {
    private Long id;
    private String name;
}
```

Usage:

```java
Product p = Product.builder()
                   .id(1L)
                   .name("Laptop")
                   .build();
```

---

### e) **@Value**

Immutable version of `@Data`.

* All fields are `private final`
* Class is `final`
* Only getters, no setters

```java
import lombok.Value;

@Value
public class Product {
    Long id;
    String name;
}
```

---

### f) **@Slf4j**

Generates a `private static final Logger log = LoggerFactory.getLogger(...)`.

```java
import lombok.extern.slf4j.Slf4j;

@Slf4j
public class ProductService {
    public void save() {
        log.info("Saving product...");
    }
}
```

Other loggers supported: `@Log4j`, `@Log4j2`, `@CommonsLog`, etc.

---

### g) **@EqualsAndHashCode, @ToString**

For custom equals/hashCode and string representations.

```java
import lombok.EqualsAndHashCode;
import lombok.ToString;

@EqualsAndHashCode
@ToString
public class Product {
    private Long id;
    private String name;
}
```

---

### h) **@With**

Creates a new instance with a modified value (useful for immutables).

```java
import lombok.With;

public class Product {
    @With private final Long id;
    @With private final String name;
}
```

Usage:

```java
Product p1 = new Product(1L, "Phone");
Product p2 = p1.withName("Tablet");
```

---

## 4. Lombok in `pom.xml`

```xml
dependency
    groupidorg.projectlombok
    artifactidlombok
    version1.18.34
  
<scope>provided</scope>



```

---

## 5. Lombok with IDEs

* **IntelliJ IDEA**: Install **Lombok plugin** + enable *Annotation Processing* in Settings → Build, Execution, Deployment → Compiler → Annotation Processors.
* **Eclipse**: Install Lombok plugin (via Lombok JAR).
* **VS Code**: Java extensions usually support it directly.

---

## 6. Best Practices

* Use `@Data` for DTOs, but avoid it in Entities (because `equals/hashCode` on mutable entities can break persistence).
* For Entities → prefer `@Getter`, `@Setter`, and explicit constructors.
* Use `@Builder` for complex object creation (especially in tests).
* Use `@Slf4j` instead of manually writing logger code.
