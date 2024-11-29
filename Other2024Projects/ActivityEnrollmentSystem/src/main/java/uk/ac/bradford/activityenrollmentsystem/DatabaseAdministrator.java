/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package uk.ac.bradford.activityenrollmentsystem;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;
import java.util.function.Predicate;

/**
 *
 * @author abdul
 */
public class DatabaseAdministrator {

    private static final String Students_File = "Students.txt";
    private static final String Activity_Groups_File = "ActivityGroups.txt";
    private static final String Student_Activity_Groups_File = "Student-ActivityGroups.txt";

    // Initialize the database files if they don't exist
    public static void initializeDatabase() {
        try {
            // Create file objects for each database file
            File studentsFile = new File(Students_File);
            File activityGroupsFile = new File(Activity_Groups_File);
            File studentActivityGroupsFile = new File(Student_Activity_Groups_File);
// Create the files if they don't exist
            if (!studentsFile.exists()) {
                studentsFile.createNewFile();
            }

            if (!activityGroupsFile.exists()) {
                activityGroupsFile.createNewFile();
            }

            if (!studentActivityGroupsFile.exists()) {
                studentActivityGroupsFile.createNewFile();
            }
        } catch (IOException e) {
            // Handle/checks any errors that occur during file creation
            System.err.println("Error initializing database: " + e.getMessage());
        }
    }

    // Add a new student to the database
    public static void addStudent(String name, int id, String filepath) {
        try (Scanner scanner = new Scanner(new File(filepath))) {
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] parts = line.split(" ");
                if (parts.length == 2 && parts[1].equals(String.valueOf(id))) {
                    System.out.println("Student with ID " + id + " already exists.");
                    return; // Exit if student with the same ID already exists
                }
            }
        } catch (FileNotFoundException e) {
            System.err.println("Students file not found: " + e.getMessage());
            return;
        }
        // If student with the same ID doesn't exist, add it to the file
        try (PrintWriter writer = new PrintWriter(new FileWriter(filepath, true))) {
            // Adds the student's name and ID to the Students.txt file
            writer.println(name + " " + id);
            System.out.println("Student added successfully.");
            writer.close();
        } catch (IOException e) {
            System.err.println("Error adding student: " + e.getMessage());
        }
    }

    // Add a new activity group to the database
    public static void activityGroup(String groupName, String filePath, InputStream file) {
        List<String> allGroups = getAllActivityGroups(file);
        try (PrintWriter writer = new PrintWriter(new FileWriter(filePath, true))) {
            if (allGroups.contains(groupName)) {
                System.out.println("Activity Group already exists");
            } else {
                writer.println(groupName);
                System.out.println("Activity group added successfully.");
            }
            writer.close();
        } catch (IOException e) {
            System.err.println("Error adding activity group: " + e.getMessage());
        }
    }

    // Enroll a student in an activity group
    public static void enrollStudent(int studentId, String groupName, InputStream file, String filepath) {
        List<String> allStuAcGroups = getStudentActivityGroups(file);
        try (PrintWriter writer = new PrintWriter(new FileWriter(filepath, true))) {
            if (allStuAcGroups.contains(studentId + " " + groupName)) {
                System.out.println("Student already exist in activity group");
            } else {
                writer.println(studentId + " " + groupName);
                System.out.println("Student enrolled in activity group successfully.");
            }
            writer.close();
        } catch (IOException e) {
            System.err.println("Error enrolling student in activity group: " + e.getMessage());
        }
    }

    // Retrieve all students from the database
    public static List<String> getAllStudents() {
        List<String> students = new ArrayList<>();
        try (Scanner scanner = new Scanner(new File(Students_File))) {
            // Read each line from the Students.txt file and add it to the list of students
            while (scanner.hasNextLine()) {
                students.add(scanner.nextLine());
            }
        } catch (FileNotFoundException e) {
            System.err.println("Students file not found: " + e.getMessage());
        }
        return students;
    }

    // Retrieve all activity groups from the database
    public static List<String> getAllActivityGroups(InputStream file) {
        List<String> groups = new ArrayList<>();
        try (Scanner scanner = new Scanner(file)) {
            while (scanner.hasNextLine()) {
                groups.add(scanner.nextLine());
            }
        } catch (Exception e) {
            System.err.println("Activity groups file not found: " + e.getMessage());
        }
        return groups;
    }

    public static ArrayList<String> getStudentActivityGroups(InputStream file) {
        ArrayList<String> studentGroups = new ArrayList<>();
        try (Scanner scanner = new Scanner(file)) {
            while (scanner.hasNextLine()) {
                studentGroups.add(scanner.nextLine());
            }
        } catch (Exception e) {
            System.err.println("Student Activity groups file not found: " + e.getMessage());
        }
        return studentGroups;
    }

    public static void removeStudent(String studentName, int studentID) {
        List<String> students = getAllStudents();
        String thisStudent = studentName + " " + studentID;
        Iterator<String> iterator = students.iterator();
        while (iterator.hasNext()) {
            String student = iterator.next().strip();
            if (thisStudent.equals(student)) {
                System.out.println("Student removed successfully");
                iterator.remove(); // Use the iterator to remove the element
            }
        }

        System.out.println("Students list is now: ");
        try (PrintWriter writer = new PrintWriter(Students_File)) {
            for (String student : students) {
                System.out.println(student);
                writer.println(student);
            }
            writer.close();
            System.out.println("Students file rewritten successfully.");
        } catch (Exception e) {
            System.err.println("Error rewriting to files: " + e.getMessage());
        }
    }

    public static void removeActivityGroup(String groupName, String filePath1, String filePath2, InputStream file1, InputStream file2) {
        List<String> allGroups = getAllActivityGroups(file1);
        ArrayList<String> enrolledGroups = getStudentActivityGroups(file2);
        Iterator<String> iterator = allGroups.iterator();
        while (iterator.hasNext()) {
            String group = iterator.next().strip();
            if (groupName.equals(group)) {
                System.out.println("Group removed successfully");
                iterator.remove(); // Use the iterator to remove the element
            }
        }
        // Create a predicate that checks if the second part of the string matches 'partToRemove'
        Predicate<String> condition = s -> {
            String[] parts = s.split("\\s+");
            return parts.length > 1 && parts[1].equals(groupName);
        };

        // Remove elements that match the predicate
        enrolledGroups.removeIf(condition);
        
        System.out.println("Groups list is now: ");
        try (PrintWriter writer = new PrintWriter(Activity_Groups_File)) {
            for (String group : allGroups) {
                System.out.println(group);
                writer.println(group);
            }
            writer.close();
            System.out.println("Groups file rewritten successfully.");
        } catch (Exception e) {
            System.err.println("Error rewriting to file: " + e.getMessage());
        }
        
        System.out.println("Groups enrollment list is now: ");
        try (PrintWriter writer = new PrintWriter(Student_Activity_Groups_File)) {
            for (String line : enrolledGroups) {
                System.out.println(line);
                writer.println(line);
            }
            writer.close();
            System.out.println("Groups enrollment file rewritten successfully.");
        } catch (Exception e) {
            System.err.println("Error rewriting to file: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        // Example
        /*initializeDatabase();
        addStudent("Yasmirah", 23001891, "Students.txt");
        activityGroup("PiSoc", "ActivityGroups.txt");
        enrollStudent(23001891, "PiSoc", "Student-ActivityGroups.txt");

        addStudent("Gary", 23145617, "Students.txt");
        activityGroup("Football", "ActivityGroups.txt");
        enrollStudent(23145617, "Football", "Student-ActivityGroups.txt");
        
        addStudent("Sarah", 21012495, "Students.txt");
        activityGroup("PiSoc", "ActivityGroups.txt");
        enrollStudent(21012495, "PiSoc", "Student-ActivityGroups.txt");

        // Retrieve and print all students
        System.out.println("All Students:");
        List<String> allStudents = getAllStudents();
        for (String student : allStudents) {
            System.out.println(student);
        }

        // Retrieve and print all activity groups
        System.out.println("\nAll Activity Groups:");
        List<String> allGroups = getAllActivityGroups("ActivityGroups.txt");
        for (String group : allGroups) {
            System.out.println(group);
        }*/
    }
}
