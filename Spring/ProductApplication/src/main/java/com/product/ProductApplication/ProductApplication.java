package com.product.ProductApplication;

import io.swagger.v3.oas.annotations.ExternalDocumentation;
import io.swagger.v3.oas.annotations.OpenAPIDefinition;
import io.swagger.v3.oas.annotations.info.Contact;
import io.swagger.v3.oas.annotations.info.Info;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@OpenAPIDefinition(
        info = @Info(
                title="Product Service Rest API Documentation",
                description="Product Service Rest API",
                version="v1",
                contact=@Contact(
                        name="Mountain",
                        email="mountain@xmail.com"
                )
        ),
        externalDocs = @ExternalDocumentation(
                description = "Sharepoint URL Product Service",
                url = "https://example.com"
        )
)
@SpringBootApplication
public class ProductApplication {
    public static void main(String[] args) {
        System.out.println("Hello World");
        SpringApplication.run(ProductApplication.class, args);
    }
}
