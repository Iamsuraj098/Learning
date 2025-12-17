package com.springstarter.springstarter.repository;

import com.springstarter.springstarter.entity.Category;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CategoryRepository extends JpaRepository<Category, Long> {

}

//Here we just pass the table (i.e, Category) and primary column datatype(i.e, Long).