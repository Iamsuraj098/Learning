package com.springstarter.springstarter.service;

import com.springstarter.springstarter.dto.CategoryDTO;
import com.springstarter.springstarter.entity.Category;
import com.springstarter.springstarter.mapper.CategoryMapper;
import com.springstarter.springstarter.repository.CategoryRepository;
import org.springframework.stereotype.Service;

@Service
public class CategoryService {

    private final CategoryRepository categoryRepository;

    public CategoryService(CategoryRepository categoryRepository) {
        this.categoryRepository = categoryRepository;
    }

    // create category
    public CategoryDTO createCategory(CategoryDTO categoryDTO) {
        Category category = CategoryMapper.toCategoryEntity(categoryDTO);
        category = categoryRepository.save(category);
        return CategoryMapper.toCategoryDTO(category);
    }
}