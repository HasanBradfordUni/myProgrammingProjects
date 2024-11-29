package uk.ac.bradford.activityenrollmentsystem;
import java.math.BigInteger;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author sulisla2
 */
public class User {
    private String name;
    private int userId;
    private String role;
    private String password;

    public User(String name, int userId, String role, String password) {
        this.name = name;
        this.userId = userId;
        this.role = role;
        if (password.length() > 30) {
            this.password = password;
        } else {
            this.password = hashPassword(password);
        }
    }

    public String getName() {
        return name;
    }

    public int getUserId() {
        return userId;
    }

    public String getRole() {
        return role;
    }
    
    public String getPassword() {
        return password;
    }
    
    public void setPassword(String hashedPassword) {
        this.password = hashedPassword;
    }
    
    public boolean verifyPassword(String passwordInput) {
        String hashedPasswordInput = hashPassword(passwordInput);
        if (this.password.equals(hashedPasswordInput)) {
            return true;
        } else {
            return false;
        }
    }

    
    public void viewAvailableActivities() {
       
    }

    
    public void enrollInActivity(String activityName) {
        if (role.equals("student")) {
            System.out.println("Enrolling in activity: " + activityName);
            
        } else {
            System.out.println("Only students can enroll in activities.");
        }
    }
    
    public static String hashPassword(String password) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hash = md.digest(password.getBytes(StandardCharsets.UTF_8));
            BigInteger number = new BigInteger(1, hash);
            StringBuilder hexString = new StringBuilder(number.toString(16));
            while (hexString.length() < 32) {
                hexString.insert(0, '0');
            }
            return hexString.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }
}
