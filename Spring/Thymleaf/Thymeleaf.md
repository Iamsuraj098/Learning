# Thymleaf
Thymeleaf in Spring Boot is a server‑side Java template engine that Spring uses to render dynamic HTML views for MVC web applications. 

Thymleaf is a java library and template engine that can process HTML, XML, JS, CSS and plain text to generate the dynamic content.
### How it works in Spring Boot
When you add the spring-boot-starter-thymleaf dependency, Spring Boot autoconfigure the thymleaf as a view technology and wires into Spring MVC as a drop in replacement for JSP.

Controller methods returns the logical view name, and spring resolve then to .html templates under the src/main/resources/templates, rendering them with model data into the final HTML sent to browser.
### Why it’s popular in Spring Boot
Thymleaf integrates tightly with Spring, allowing direct binding to model attributes form‑backing objects using attributes like **th:object** and **th:field**, which simplifies form handling.
### Custom Attributes in Thymeleaf:
- Core display attributes:
	- **th:test** - sets the text content of a tag from an expression, escaping HTML by default.
	- **th:utext** - like th:text but outputs unescaped HTML (used carefully for trusted HTML content).
	- **th:attr** -  sets one or more arbitrary HTML attributes in one shot
- Conditionals and loops
	- **th:if**/**th:unless** - conditionally exclude or include an element based on a boolean expression.
	- **th:each** - iterate over the collections, repeating the tags for each items.
	- **th:switch**/**th:case** - multi-branch conditional logic similar to switch/case in Java.
- Links, Urls and Forms:
	- **th:href**, **th:src**, **th:action** - build dynamic URLs for links, images, and form actions, typically using @{...} expressions
	- **th:value**, **th:placeholder**, **th:onclick** - shorthand for setting common attributes without using th:attr
	- **th:object**/**th:feild** - bind a form to a backing object and its properties, integrating cleanly with Spring MVC model attributes.
- Fragments, layout, and miscellaneous
	- **th:fragment** - defines a reusable fragment (header, footer, etc.) that other templates can include.
	- **th:insert**, **th:replace**, **th:include** -  include or replace parts of a page with defined fragments for layout composition
	- **th:with** - define local variables within a tag scope; th:classappend, th:styleappend
### How JSP and Thymeleaf related to each other ?
JSP (JavaServer Pages) and Thymeleaf both implement the “V” (View) in the Spring MVC pattern: a controller returns a view name, and either a JSP or a Thymeleaf template is used to build the response. In practice, you choose one of them as your view technology, configure the corresponding view resolver, and they play the same architectural role in the application.
### Difference between Thymeleaf and JSP.
| Aspect      | JSP                                                          | Thymeleaf                                                          |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------------ |
| Technology  | Page technology compiled to servlets.                        | Template engine that parses HTML templates.                        |
| Syntax      | HTML mixed with JSP tags/Java code.                          | Pure HTML plus th:*attributes.                                      |
| Spring Boot | Official docs suggest avoiding JSP with embedded containers. | First-class auto-configuration support; recommended for MVC views. |









