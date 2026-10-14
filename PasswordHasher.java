package com.example.inventorytracker.security;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
public final class PasswordHasher {
    private PasswordHasher(){}
    public static String sha256(String value){
        try{
            byte[] h=MessageDigest.getInstance("SHA-256").digest(value.getBytes(StandardCharsets.UTF_8));
            StringBuilder b=new StringBuilder(); for(byte x:h)b.append(String.format("%02x",x)); return b.toString();
        }catch(Exception e){throw new IllegalStateException("Unable to hash password",e);}
    }
}
