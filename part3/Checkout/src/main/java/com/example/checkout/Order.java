package com.example.checkout;

import java.io.Serializable;
import java.util.List;
import java.util.UUID;

public class Order implements Serializable {
    public String id;
    public List<LineItem> items;

    public Order() {
        id = UUID.randomUUID().toString();
    }

    public List<LineItem> getItems() {
        return items;
    }

    public void setItems(List<LineItem> items) {
        this.items = items;
    }
}
