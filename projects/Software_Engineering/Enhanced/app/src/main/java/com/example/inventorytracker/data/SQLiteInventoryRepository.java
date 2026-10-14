package com.example.inventorytracker.data;
import android.content.*; import android.database.Cursor; import android.database.sqlite.*;
import com.example.inventorytracker.model.InventoryItem; import java.util.*;
public class SQLiteInventoryRepository extends SQLiteOpenHelper implements InventoryRepository {
    public SQLiteInventoryRepository(Context c){super(c,"inventory.db",null,2);}
    public void onCreate(SQLiteDatabase db){
        db.execSQL("CREATE TABLE users(id INTEGER PRIMARY KEY,username TEXT UNIQUE NOT NULL,password_hash TEXT NOT NULL)");
        db.execSQL("CREATE TABLE inventory(id INTEGER PRIMARY KEY,name TEXT NOT NULL,quantity INTEGER NOT NULL CHECK(quantity>=0),low_stock_threshold INTEGER NOT NULL DEFAULT 5 CHECK(low_stock_threshold>=0))");
        db.execSQL("CREATE INDEX idx_inventory_name ON inventory(name)");
    }
    public void onUpgrade(SQLiteDatabase db,int oldV,int newV){
        if(oldV<2){ db.execSQL("ALTER TABLE inventory ADD COLUMN low_stock_threshold INTEGER NOT NULL DEFAULT 5"); }
    }
    public long create(String n,int q,int t){ ContentValues v=values(n,q,t); return getWritableDatabase().insertOrThrow("inventory",null,v); }
    public boolean update(long id,String n,int q,int t){return getWritableDatabase().update("inventory",values(n,q,t),"id=?",new String[]{String.valueOf(id)})==1;}
    public boolean delete(long id){return getWritableDatabase().delete("inventory","id=?",new String[]{String.valueOf(id)})==1;}
    public List<InventoryItem> findAll(){return query("SELECT id,name,quantity,low_stock_threshold FROM inventory ORDER BY name",null);}
    public List<InventoryItem> search(String s){return query("SELECT id,name,quantity,low_stock_threshold FROM inventory WHERE name LIKE ? ORDER BY name",new String[]{"%"+s+"%"});}
    public List<InventoryItem> findLowStock(){return query("SELECT id,name,quantity,low_stock_threshold FROM inventory WHERE quantity<=low_stock_threshold ORDER BY quantity,name",null);}
    private ContentValues values(String n,int q,int t){ContentValues v=new ContentValues();v.put("name",n);v.put("quantity",q);v.put("low_stock_threshold",t);return v;}
    private List<InventoryItem> query(String sql,String[] args){
        List<InventoryItem> out=new ArrayList<>(); Cursor c=getReadableDatabase().rawQuery(sql,args);
        try{while(c.moveToNext())out.add(new InventoryItem(c.getLong(0),c.getString(1),c.getInt(2),c.getInt(3)));}finally{c.close();}
        return out;
    }
}
