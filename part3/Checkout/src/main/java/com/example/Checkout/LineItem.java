package com.example.Checkout;
import java.io.Serializable;
import org.springframework.data.redis.core.RedisHash;

@RedisHash("LineItem")
public class LineItem implements Serializable {
    public String id;
    public int quantity;
}