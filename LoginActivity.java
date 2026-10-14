package com.example.inventorytracker;
import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.widget.*;
public class LoginActivity extends Activity {
    DatabaseHelper db;
    protected void onCreate(Bundle b){
        super.onCreate(b); db=new DatabaseHelper(this);
        // Original project used a direct Activity-to-database design.
    }
    void login(String user,String pass){
        if(db.login(user,pass)) startActivity(new Intent(this,InventoryActivity.class));
        else Toast.makeText(this,"Invalid login",Toast.LENGTH_SHORT).show();
    }
}
