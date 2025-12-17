package com.product.ProductApplication.controller;

import com.product.ProductApplication.dto.CategoryDTO;
import com.product.ProductApplication.dto.ProductDTO;
import com.product.ProductApplication.service.ProductService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.AllArgsConstructor;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@Tag(
        name="Product Service",
        description = "Create Update Delete Read operation for product for rest api."
)
@RestController
@RequestMapping("/api/products")
@AllArgsConstructor
@EnableWebSecurity
public class ProductController {

    private ProductService productService;
//    get all product
    @Operation(
            summary = "Get all product",
            description = "REST API to get all product"
    )
    @GetMapping
    public List<ProductDTO> getAllProduct() {
        return productService.getAllProduct();
    }

// getProductById
    @Operation(
            summary = "Get product by id",
            description = "REST API to get product by id"
    )
    @GetMapping("/{id}")
    public ProductDTO getProductById(@PathVariable Long id){
        return productService.getProductById(id);
    }

//    create product
//    here fucntion createProduct() give 200 response which is sucess response but we know when any change
    @PreAuthorize("hasAuthority('ROLE_SELLER')")
    @Operation(
            summary = "Create product",
            description = "REST API to create product"
    )
    @ApiResponse(
            responseCode = "201",
            description = "CREATED"
    )
    @PostMapping
    public ProductDTO createProduct(@RequestBody ProductDTO productDTO){
        return productService.createProduct(productDTO);
    }

//    update product
    @Operation(
            summary = "Updated product by id",
            description = "REST API to update product by id"
    )

    @PutMapping("/{id}")
    public ProductDTO updateProduct(@PathVariable Long id, @RequestBody ProductDTO productDTO){
        return productService.updateProduct(id, productDTO);
    }

//    delete product
    @Operation(
            summary = "Delete product by id",
            description = "REST API to delete product by id"
    )
    @PreAuthorize("hasAuthority('ROLE_SELLER')")
    @DeleteMapping("/{id}")
    public String deleteProduct(@PathVariable Long id){
        return productService.deleteProduct(id);
    }
}
