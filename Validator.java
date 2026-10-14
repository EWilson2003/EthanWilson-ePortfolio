package com.example.inventorytracker.util;
public final class Validator {
    private Validator(){}
    public static String username(String v){
        v=v==null?"":v.trim();
        if(v.length()<3 || v.length()>40) throw new IllegalArgumentException("Username must be 3-40 characters.");
        return v;
    }
    public static String password(String v){
        if(v==null || v.length()<8) throw new IllegalArgumentException("Password must be at least 8 characters.");
        return v;
    }
    public static String itemName(String v){
        v=v==null?"":v.trim();
        if(v.isEmpty() || v.length()>80) throw new IllegalArgumentException("Item name is required.");
        return v;
    }
    public static int nonNegative(int v,String field){
        if(v<0) throw new IllegalArgumentException(field+" cannot be negative."); return v;
    }
}
