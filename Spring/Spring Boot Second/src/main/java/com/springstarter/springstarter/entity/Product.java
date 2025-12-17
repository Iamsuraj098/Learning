package com.springstarter.springstarter.entity;
import lombok.Getter;
import lombok.Setter;
import jakarta.persistence.*;

@Entity
@Getter @Setter
public class Product {

    @Id
    @GeneratedValue(strategy=GenerationType.IDENTITY)
    private long id;
    private String name;
    private  String description;
    private Double price;
    @ManyToOne
    @JoinColumn(name="category_id", nullable = false)
    private Category category;
}
