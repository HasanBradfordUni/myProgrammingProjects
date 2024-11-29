package uk.ac.bradford.activityenrollmentsystem;
import java.util.HashMap;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author haalhala
 */
public class GroupMaxCounts {
    private static HashMap<String, Integer> activityCounts = new HashMap<>(); 
    
    public static void setMaxCount(String activityName, int maxCount) {
        activityCounts.put(activityName, maxCount);
    }
    
    public static Integer getMaxCount(String activityName) {
        return activityCounts.get(activityName);
    }
}
