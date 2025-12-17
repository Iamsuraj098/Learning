package com.product.ProductApplication.Annotation;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class ComponentAnnotation2 {
//    @Autowired
    private final ComponentAnnotation myComponent;

    @Autowired
    public ComponentAnnotation2(ComponentAnnotation myComponent){
        this.myComponent = myComponent;
    }

    public void run(){
        myComponent.getMessage();
    }
}
