package com.example.inventorytracker;
import android.app.Activity;
import android.os.Bundle;
public class InventoryActivity extends Activity {
    DatabaseHelper db;
    protected void onCreate(Bundle b){ super.onCreate(b); db=new DatabaseHelper(this); }
    void add(String name,int qty){ db.addItem(name,qty); }
    void update(int id,String name,int qty){ db.updateItem(id,name,qty); }
    void delete(int id){ db.deleteItem(id); }
}
