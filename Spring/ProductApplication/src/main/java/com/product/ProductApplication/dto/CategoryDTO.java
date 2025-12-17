package com.product.ProductApplication.dto;

import io.swagger.v3.oas.annotations.media.Schema;
import lombok.*;

import java.util.List;


@Schema(
        name = "Category",
        description = "It holds category information along with the products"
)
@Data
@NoArgsConstructor
@AllArgsConstructor
public class CategoryDTO {
    private Long id;
    private String name;
    private List<ProductDTO> products;
}
