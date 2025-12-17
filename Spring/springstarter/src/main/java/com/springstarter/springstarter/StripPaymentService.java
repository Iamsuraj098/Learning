package com.springstarter.springstarter;

import org.springframework.stereotype.Service;

@Service
public class StripPaymentService implements PaymentService {
    @Override
    public void processPayment(double amount){
        System.out.println("Striped");
        System.out.println("Amount: " + amount);
    }
}
