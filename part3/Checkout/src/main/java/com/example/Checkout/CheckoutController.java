package com.example.Checkout;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CheckoutController {

//  @Autowired
 OrderRepository repository;

  @PostMapping("/checkout")
  Order newOrder(@RequestBody Order newOrder) {
    return repository.save(newOrder);
  }
}