package com.example.inventorytracker.model;
public class InventoryItem {
    private final long id; private final String name; private final int quantity; private final int lowStockThreshold;
    public InventoryItem(long id,String name,int quantity,int threshold){
        this.id=id; this.name=name; this.quantity=quantity; this.lowStockThreshold=threshold;
    }
    public long getId(){return id;} public String getName(){return name;}
    public int getQuantity(){return quantity;} public int getLowStockThreshold(){return lowStockThreshold;}
    public boolean isLowStock(){return quantity<=lowStockThreshold;}
}
