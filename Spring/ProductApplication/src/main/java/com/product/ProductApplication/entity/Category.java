package com.product.ProductApplication.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.util.ArrayList;
import java.util.List;

@Entity
@Getter @Setter
public class Category {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;

    @OneToMany(mappedBy = "category", cascade = CascadeType.ALL, fetch = FetchType.EAGER)
    private List<Product> products = new ArrayList<>();
}

/**
 * @GeneratedValue(strategy = GenerationType.IDENTITY) => this code automatically created the new unique ids.
 * Here we are giving one-to-many relationship because a single type category have multiple product. Like Category may be Toy then product mey be car, robo, gun etc.
 * cascade = CascadeType.ALL -> this show we want to delete all product in that category of that type products.
*/