package com.product.ProductApplication.Annotation;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

@SpringBootApplication
public class App {
    public static void main(String[] args) {

//        1. @Component
//        a) MyComponent myComponent = new MyComponent(); here we manually create the object and inject it.
        ApplicationContext applicationContext = SpringApplication.run(App.class, args);
//        MyComponent myComponent = applicationContext.getBean(MyComponent.class);
//      b) At line 12, we not create the myComponent object but its object automatically created and injected into it.
//        c) Here we can also do it by using the another class inside another class we create the object of MyComponent and inject in it.
        ComponentAnnotation2 myComponent = applicationContext.getBean(ComponentAnnotation2.class);
        myComponent.run();
    }
}
