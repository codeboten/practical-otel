// CheckoutController.java
package com.example.checkout;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;

import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.data.redis.serializer.Jackson2JsonRedisSerializer;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import io.opentelemetry.extension.annotations.WithSpan;
import io.opentelemetry.api.trace.Span;

@RestController
public class CheckoutController {

    @Autowired
    private ApplicationContext context;

    @WithSpan
    String serializeOrder(Order order) {
        Span span = Span.current();
        span.setAttribute("order-id", order.id);
        Jackson2JsonRedisSerializer<Order> serializer = new Jackson2JsonRedisSerializer<>(Order.class);
        return new String(serializer.serialize(order));
    }

    @WithSpan
    void sendMessage(String message) {
        StringRedisTemplate template = context.getBean(StringRedisTemplate.class);
        template.convertAndSend("orders", message);
    }

    @PostMapping("/orders")
    Order newOrder(@RequestBody Order newOrder) {
        Order order = new Order();
        order.setItems(newOrder.getItems());
        String serializedOrder = serializeOrder(order);
        sendMessage(serializedOrder);
        return order;
    }
}