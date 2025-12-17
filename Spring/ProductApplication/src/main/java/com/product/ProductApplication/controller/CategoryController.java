package com.product.ProductApplication.controller;

import com.product.ProductApplication.dto.CategoryDTO;
import com.product.ProductApplication.exception.CategoryAlreadyExistsException;
import com.product.ProductApplication.service.CategoryService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Tag(
        name="Category Service",
        description = "Create Update Delete Read operation for category for rest api."
)
@RestController
@RequestMapping("/api/categories")
@AllArgsConstructor
@EnableWebSecurity
public class CategoryController {

    private CategoryService categoryService;
//    get categories
    @Operation(
            summary = "Get all category",
            description = "REST API to get all category"
    )
    @GetMapping
    public List<CategoryDTO> getAllCategories(){
        return categoryService.getAllCategories();
    }

//    create categories
//    public ResponseEntity<CategoryDTO> createCategory(@RequestBody CategoryDTO categoryDTO){
//    This question make it to take any type of output.
    @Operation(
            summary = "Create category",
            description = "REST API to create category"
    )
    @ApiResponse(
            responseCode = "201",
            description = "CREATED"
    )
    @PreAuthorize("hasAuthority('ROLE_ADMIN')")
    @PostMapping
    public ResponseEntity<?> createCategory(@RequestBody CategoryDTO categoryDTO){
        CategoryDTO savedCategory = categoryService.createCategory(categoryDTO);
        return ResponseEntity.status(HttpStatus.CREATED).body(savedCategory);
    }

//    get category by id
    @Operation(
            summary = "Get category by id",
            description = "REST API to get category by id"
    )

    @GetMapping("/{id}")
    public CategoryDTO getCategoryById(@PathVariable Long id){
        return categoryService.getCategoryById(id);
    }

//    delete category
    @Operation(
            summary = "Delete category by id",
            description = "REST API to delete category by id"
    )
    @PreAuthorize("hasAuthority('ROLE_ADMIN')")
    @DeleteMapping("/{id}")
    public String delete(@PathVariable Long id){
        return categoryService.deleteCategory(id);
    }
}
