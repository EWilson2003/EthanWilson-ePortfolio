package com.example.inventorytracker.ui;
import android.app.Activity; import android.os.Bundle;
import com.example.inventorytracker.data.SQLiteInventoryRepository;
import com.example.inventorytracker.service.InventoryService;
public class InventoryActivity extends Activity {
    private InventoryService service;
    protected void onCreate(Bundle b){super.onCreate(b);service=new InventoryService(new SQLiteInventoryRepository(this));}
    // UI event handlers call service.add/update/delete/search/lowStock.
    // Business rules and SQL are intentionally kept out of the Activity.
}
