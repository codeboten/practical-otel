package com.example.Checkout;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.ReactiveRedisTemplate;
import org.springframework.context.ApplicationContext;

import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.data.redis.serializer.Jackson2JsonRedisSerializer;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CheckoutController {

    @Autowired
    private ApplicationContext context;

    @PostMapping("/orders")
    Order newOrder(@RequestBody Order newOrder) {
        Order order = new Order();
        order.setItems(newOrder.getItems());
        StringRedisTemplate template = context.getBean(StringRedisTemplate.class);

        Jackson2JsonRedisSerializer<Order> serializer = new Jackson2JsonRedisSerializer<>(Order.class);
        template.convertAndSend("orders", new String(serializer.serialize(order)));
        return order;
    }
}