package com.springstarter.springstarter.repository;

import com.springstarter.springstarter.entity.Product;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProductRepository extends JpaRepository<Product, Long> {

}
