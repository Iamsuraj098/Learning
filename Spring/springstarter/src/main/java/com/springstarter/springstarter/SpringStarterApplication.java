package com.springstarter.springstarter;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

@SpringBootApplication
public class SpringStarterApplication {

	public static void main(String[] args) {
//		SpringApplication.run(SpringStarterApplication.class, args);
//		var OrderService = new OrderService(new UPI());
//		var OrderService = new OrderService();
//		OrderService.setPaymentService(new StripPaymentService());
//		OrderService.placeOrder();

//		above we manually pass the object
//		IoC
		ApplicationContext context = SpringApplication.run(SpringStarterApplication.class, args);
//		var OrderService = new OrderService(new UPI());
		var OrderService = context.getBean(com.springstarter.springstarter.OrderService.class);
		OrderService.setPaymentService(new StripPaymentService());
		OrderService.placeOrder();
	}

}
