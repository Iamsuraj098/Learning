### Spring MVC
Spring MVC (Model-View-Controller) is a web framework built on top of the Servlet API, part of the broader Spring Framework, used for building robust and scalable Java web applications — especially those that expose REST APIs, serve HTML views, or handle form-based input.


- it stands for Model View Controller
- Model: Business Logic + Connect with databases
- View: What the user sees(JSP, HTML, CSS, JS, JSON or Thymeleaf)
- Controller: Handles HTTP requests, calls services, and returns model + view.

---
### Annotation
An annotation in Java is a special kind of metadata that can be added to classes, methods, variables, parameters, or packages to give the compiler or frameworks extra instructions.

In Spring (and Spring Boot), annotations are used heavily to configure your application without needing verbose XML files.
#### Common Annotations in Spring:
- @Component
- @Service
- @Controller
- @Autowired
- @GetMapping, @PostMapping, @RequestMapping