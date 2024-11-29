/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package uk.ac.bradford.activityenrollmentsystem;

import java.io.InputStream;
import java.util.ArrayList;

/**
 *
 * @author hakhta26
 */
public class President extends User {
    public President(String name, int userId, String password) {
        super(name, userId, "President", password);
    }

    public static ArrayList<String> retrieveEnrolledStudents(String groupName, InputStream file) {
        ArrayList<String> studentAndActivityGroup = DatabaseAdministrator.getStudentActivityGroups(file);
        int count = 0;
        ArrayList<String> students = new ArrayList<>();
        for (int i = 0; i < studentAndActivityGroup.size(); i++) {
            String activityGroup = studentAndActivityGroup.get(i).strip().split(" ")[1];
            String studentID = studentAndActivityGroup.get(i).strip().split(" ")[0];
            if (activityGroup.equals(groupName)) {
                students.add(studentID);
            }
        }
        return students;
    }
}
