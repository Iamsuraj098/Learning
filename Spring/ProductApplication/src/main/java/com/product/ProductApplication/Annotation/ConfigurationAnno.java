package com.product.ProductApplication.Annotation;
import org.springframework.beans.factory.annotation.Configurable;
import org.springframework.context.annotation.Bean;

@Configurable
public class ConfigurationAnno {

    @Bean
    public ComponentAnnotation componentAnnotation(){
        return new ComponentAnnotation();
    }
}
