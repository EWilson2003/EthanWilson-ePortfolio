package com.example.inventorytracker.service;
import com.example.inventorytracker.data.InventoryRepository; import com.example.inventorytracker.model.InventoryItem;
import com.example.inventorytracker.util.Validator; import java.util.List;
public class InventoryService {
    private final InventoryRepository repo;
    public InventoryService(InventoryRepository repo){this.repo=repo;}
    public long add(String name,int qty,int threshold){
        return repo.create(Validator.itemName(name),Validator.nonNegative(qty,"Quantity"),Validator.nonNegative(threshold,"Threshold"));
    }
    public boolean update(long id,String name,int qty,int threshold){
        if(id<=0) throw new IllegalArgumentException("Invalid item id.");
        return repo.update(id,Validator.itemName(name),Validator.nonNegative(qty,"Quantity"),Validator.nonNegative(threshold,"Threshold"));
    }
    public boolean delete(long id){if(id<=0)throw new IllegalArgumentException("Invalid item id.");return repo.delete(id);}
    public List<InventoryItem> search(String text){return text==null||text.trim().isEmpty()?repo.findAll():repo.search(text.trim());}
    public List<InventoryItem> lowStock(){return repo.findLowStock();}
}
