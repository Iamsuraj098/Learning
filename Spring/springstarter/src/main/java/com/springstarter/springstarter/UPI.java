package com.springstarter.springstarter;

import org.springframework.stereotype.Service;

@Service
public class UPI implements PaymentService{
    @Override
    public void processPayment(double amount) {
        System.out.println("UPI");
        System.out.println("Amount: " + amount);
    }
}
