package com.product.ProductApplication.service;

import com.product.ProductApplication.dto.CategoryDTO;
import com.product.ProductApplication.entity.Category;
import com.product.ProductApplication.exception.CategoryAlreadyExistsException;
import com.product.ProductApplication.mapper.CategoryMapper;
import com.product.ProductApplication.repository.CategoryRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;

@Service
public class CategoryService {

    private CategoryRepository categoryRepository;

    public CategoryService(CategoryRepository categoryRepository) {
        this.categoryRepository = categoryRepository;
    }

    // create category
    public CategoryDTO createCategory(CategoryDTO categoryDTO) {

        Optional<Category> optionalCategory = categoryRepository.findByName(categoryDTO.getName());
        if(optionalCategory.isPresent()){
            throw new CategoryAlreadyExistsException("Category "+ categoryDTO.getName() +" already exits!");
        }
        Category category = CategoryMapper.toCategoryEntity(categoryDTO);  // Here mapper call to explicit type convert the categoryDTO to category.
        category = categoryRepository.save(category); // Save to Database
        return CategoryMapper.toCategoryDTO(category); // Explicit type conversion from category to CategoryDTO
    }

//    get All Category
    public List<CategoryDTO> getAllCategories(){
        return categoryRepository.findAll().stream().map(CategoryMapper::toCategoryDTO).toList(); // it will return all category in Category Entity return type.
    }
//    get Category by id
    public CategoryDTO getCategoryById(Long id){
        Category category = categoryRepository.findById(id).orElseThrow(()->new RuntimeException("Category not found"));
        return CategoryMapper.toCategoryDTO(category);
    }

//    Delete by id
    public String deleteCategory(Long id){
        categoryRepository.deleteById(id);
        return "Category Successfully deleted";
    }
}
/**
 * When we need the trasformation then we can use "stream()"
 **/