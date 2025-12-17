package com.product.ProductApplication.repository;

import com.product.ProductApplication.entity.Category;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface CategoryRepository extends JpaRepository<Category, Long> {
    Optional<Category> findByName(String categoryName);
}

//Here we just pass the table (i.e, Category) and primary column datatype(i.e, Long).