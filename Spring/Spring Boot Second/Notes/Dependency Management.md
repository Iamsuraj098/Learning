### What is Dependencies
Dependencies are the external llibraries(Jar files) that your appllication need work in order.
These include everything from Spring components (like Spring Web, Data, Security) to third-party tools (like MySQL drivers, Jackson for JSON, Lombok, etc.).

---
### Why Dependencies Are Important
Spring Boot apps are modular and need different libraries based on what you're building:
 - Want to build a REST API? → Need spring-boot-starter-web
 - Want to use JPA with a database? → Need spring-boot-starter-data-jpa
 - Want to use Security? → Add spring-boot-starter-security

Spring Boot simplifies this by offering "starter" dependencies.

--- 
These dependencies are added in the POM.xml(in maven project) files and
its automatically install in our environment.

We can get these dependencies from the **Maven Central** website
