package com.product.ProductApplication.service;

import com.product.ProductApplication.dto.CategoryDTO;
import com.product.ProductApplication.dto.ProductDTO;
import com.product.ProductApplication.entity.Category;
import com.product.ProductApplication.entity.Product;
import com.product.ProductApplication.exception.CategoryNotFoundException;
import com.product.ProductApplication.mapper.ProductMapper;
import com.product.ProductApplication.repository.CategoryRepository;
import com.product.ProductApplication.repository.ProductRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ProductService {

    private ProductRepository productRepository;
    private CategoryRepository categoryRepository;
    // Constructor injection ensures both repositories are auto-wired
    public ProductService(ProductRepository productRepository, CategoryRepository categoryRepository) {
        this.productRepository = productRepository;
        this.categoryRepository = categoryRepository;
    }
    public ProductDTO createProduct(ProductDTO productDTO){
/**
 * Here we get the name, description, price and categoryId
 * First we have to find categoryId present in database or not.
 * **/
//        So to check categoryId is present or not we used the CategoryRepository -
        Category category =  categoryRepository.findById(productDTO.getCategoryId()).orElseThrow(()->new CategoryNotFoundException("category "+ productDTO.getCategoryId() + "not find!"));
//        We can not save the DTO to database so we have to change it to Entity.
//        DTO -> Entity
        Product product =  ProductMapper.toProductEntity(productDTO, category);
        product = productRepository.save(product);
//        Entity -> DTO
        return ProductMapper.toProductDTO(product);
    }

//    get ALl product
    public List<ProductDTO> getAllProduct(){
        return productRepository.findAll().stream().map(ProductMapper::toProductDTO).toList();
    }

//    Get List by id
    public ProductDTO getProductById(Long id){
        Product product = productRepository.findById(id).orElseThrow(()->new RuntimeException("Product Not Found"));
        return ProductMapper.toProductDTO(product);
    }

    // Update Product
    public ProductDTO updateProduct(Long id, ProductDTO productDTO){
        Product product = productRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Product not found!"));
        Category category = categoryRepository.findById(productDTO.getCategoryId())
                .orElseThrow(() -> new RuntimeException("Category not found!"));

        product.setName(productDTO.getName());
        product.setDescription(productDTO.getDescription());
        product.setPrice(productDTO.getPrice());
        product.setCategory(category);
        productRepository.save(product);
        return ProductMapper.toProductDTO(product);
    }

//    Delete product
    public String deleteProduct(Long id){
        productRepository.deleteById(id);
        return "Product Deleted Successfully.";
    }

}

//After giving annotation @Service - spring automatically understand this have some business logic.