package com.example.inventorytracker;
import android.content.*;
import android.database.Cursor;
import android.database.sqlite.*;
public class DatabaseHelper extends SQLiteOpenHelper {
    public DatabaseHelper(Context c){ super(c,"inventory.db",null,1); }
    public void onCreate(SQLiteDatabase db){
        db.execSQL("CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT, password TEXT)");
        db.execSQL("CREATE TABLE inventory(id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER)");
    }
    public void onUpgrade(SQLiteDatabase db,int oldV,int newV){}
    public boolean register(String u,String p){
        ContentValues v=new ContentValues(); v.put("username",u); v.put("password",p);
        return getWritableDatabase().insert("users",null,v)!=-1;
    }
    public boolean login(String u,String p){
        Cursor c=getReadableDatabase().rawQuery(
            "SELECT id FROM users WHERE username=? AND password=?",new String[]{u,p});
        boolean ok=c.moveToFirst(); c.close(); return ok;
    }
    public long addItem(String name,int qty){
        ContentValues v=new ContentValues(); v.put("name",name); v.put("quantity",qty);
        return getWritableDatabase().insert("inventory",null,v);
    }
    public Cursor getItems(){ return getReadableDatabase().rawQuery("SELECT * FROM inventory",null); }
    public int updateItem(int id,String name,int qty){
        ContentValues v=new ContentValues(); v.put("name",name); v.put("quantity",qty);
        return getWritableDatabase().update("inventory",v,"id=?",new String[]{String.valueOf(id)});
    }
    public int deleteItem(int id){
        return getWritableDatabase().delete("inventory","id=?",new String[]{String.valueOf(id)});
    }
}
