package uk.ac.bradford.activityenrollmentsystem;
import java.util.*;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author hakhta26
 */

public class CustomMap {
    String first;
    int second;

    public CustomMap (String first, int second) {
        this.first = first;
        this.second = second;
    }
    
    public String getFirst() {
        return this.first;
    }
    
    public int getSecond() {
        return this.second;
    }
    
    public String getFirstFromSecond(int second) {
        String first; 
        if (this.second == second) {
            first = this.first;
        } else {
            first = null;
        } return first;
    }
    
    public int getSecondFromFirst(String first) {
        int second; 
        if (first.equalsIgnoreCase(this.first)) {
            second = this.second;
        } else {
            second = -1;
        } return second;
    }
    
    public void changeSecond(int second) {
       this.second = second;
    }
    
    public void changeFirst(String first) {
        this.first = first;
    }
    
    public String outputAsString(boolean output) {
        if (output) {
            System.out.println("First: "+this.first+" Second: "+this.second);
        }
        return first+" "+second;
    }
}