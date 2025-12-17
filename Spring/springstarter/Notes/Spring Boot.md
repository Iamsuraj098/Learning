## Spring Boot
Spring Boot is an open-source Java-based framework used to build stand-alone, production-grade Spring applications quickly and easily with minimal configuration.

Spring Boot build over the Spring framework.

It remove the all the limitation of Spring framework(Like manual configuration, etc) and make fast development.

---
### Why use the spring boot ?
1. Zero XML Configuration
2. Auto Configuration
3. Embedding Server (Like Tomcat, Jetty etc)
4. microservice Friendly
5. Spring Initializer

---
### Popular Use cases of spring boot
1. Restful API
2. Microservices with Spring Cloud
3. Web application with Thymeleaf or JSP
4. Enterprise systems

---
| **Spring Framework**                                                                | **Spring Boot**                                                               |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| A **comprehensive Java framework** for building enterprise applications             | A **rapid application development tool** built **on top of Spring Framework** |
| Requires **manual setup and configuration**                                         | Provides **auto-configuration**, **defaults**, and **starter templates**      |
| Used for building **any kind** of Java application (web, desktop, enterprise, etc.) | Focused on **simplifying** Spring-based web and microservice development      |
| You need to configure XML or Java classes                                           | Auto-detects and configures most beans for you                                |
| Part of the **core Spring ecosystem**                                               | A **helper layer** over the Spring ecosystem                                  |

---
### Relation Between Spring Boot, Spring Framework and Servlet
1. *Servlet* - A low-level Java API class to handle HTTP requests/responses.
2. *Spring Framework* - A powerful Java framework providing MVC, Dependency Injection (DI), AOP, Data access, etc. Built on top of Servlet API.
3. *Spring boot* - Built on top of Spring Framework, and indirectly on Servlets.

---
### Why we leave the servlet ?
1. Manual Configuration (in web.xml or annotation)
2. No built-in MVC
3. No Dependency Injection
4. Hard to Scale
5. Verbose Code

### Why we leave the Spring Framework ?
1. Manual Setups - still need to configure XML or Java-based config files (e.g., beans, DB, MVC setup).
2. Server Deployment required
3. No auto-configuration

---
### Flow: Spring Boot → Spring Framework → Servlet
Spring Boot, Spring Framework, and the Servlet API are all layers that work together in a modern Java web application. At the lowest level, the **Servlet API** is part of Java EE (now Jakarta EE) and provides the fundamental mechanism to handle HTTP requests and responses through classes like `HttpServlet`. This is the core web technology that Java uses to build web servers and applications.

On top of this, the **Spring Framework** builds an abstraction by providing a more structured and modular way to handle web requests using features like `DispatcherServlet`, `@Controller`, `@RequestMapping`, and a powerful dependency injection system. Spring abstracts away the complexities of writing raw servlets and allows developers to write cleaner, maintainable code with built-in support for MVC, security, data access, and more.

Then comes **Spring Boot**, which sits on top of the Spring Framework. It simplifies the development process by auto-configuring many Spring components, embedding the server (like Tomcat or Jetty), and removing the need for complex XML or Java configurations. It uses Spring Framework under the hood and, indirectly, still depends on the Servlet API because the `DispatcherServlet` is ultimately just a specialized servlet. In essence, Spring Boot makes it faster and easier to build Spring Framework-based applications, which in turn depend on the underlying Servlet mechanism to process web requests.

So, the relationship is layered: **Spring Boot uses Spring Framework**, and **Spring Framework uses the Servlet API**. Each layer builds on the one below it to make Java web development more powerful and developer-friendly.





















