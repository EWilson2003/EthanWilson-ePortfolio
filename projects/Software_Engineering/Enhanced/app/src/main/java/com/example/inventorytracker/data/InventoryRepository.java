package com.example.inventorytracker.data;
import com.example.inventorytracker.model.InventoryItem;
import java.util.List;
public interface InventoryRepository {
    long create(String name,int quantity,int threshold);
    boolean update(long id,String name,int quantity,int threshold);
    boolean delete(long id);
    List<InventoryItem> findAll();
    List<InventoryItem> search(String text);
    List<InventoryItem> findLowStock();
}
