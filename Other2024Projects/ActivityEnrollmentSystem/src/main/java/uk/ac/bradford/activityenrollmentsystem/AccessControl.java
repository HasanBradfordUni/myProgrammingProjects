/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package uk.ac.bradford.activityenrollmentsystem;

/**
 *
 * @author sulisla2
 */
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class AccessControl {

    private static List<User> users = new ArrayList<>();
    private static List<President> presidents = new ArrayList<>();
    private static List<Coordinator> coordinators = new ArrayList<>();

    public AccessControl() {
        users.clear();
        presidents.clear();
        coordinators.clear();
    }

    public static String authenticate(String username, String password) {
        String role = null;
        getUsers();
        for (User user : users) {
            if (user.getName().equals(username) && user.verifyPassword(password)) {
                System.out.println("User info: " + user.getName() + " " + user.getUserId() + " " + user.getRole() + " " + user.getPassword());
                role = user.getRole();
                President presidentUser = new President(user.getName(), user.getUserId(), password);
                Coordinator coordinatorUser = new Coordinator(user.getName(), user.getUserId(), password);
                if (role.equals("president") && !presidents.contains(presidentUser)) {
                    presidents.add(presidentUser);
                    System.out.println("Presidents list is now: " + presidents.toString());
                } else if (role.equals("coordinator") && !coordinators.contains(coordinatorUser)) {
                    coordinators.add(coordinatorUser);
                    System.out.println("Co-ordinators list is now: " + coordinators.toString());
                }
                break;
            }
        }
        return role;
    }

    public static void getUsers() {
        int userID;
        String name, password, role;
        try (Scanner scanner = new Scanner(new File("Users.txt"))) {
            // Read each line from the Students.txt file and add it to the list of students
            while (scanner.hasNextLine()) {
                String[] userLine = scanner.nextLine().strip().split(" ");
                userID = Integer.parseInt(userLine[0]);
                name = userLine[1];
                password = userLine[2];
                role = userLine[3];
                User userToAdd = new User(name, userID, role, password);
                users.add(userToAdd);
                System.out.println("User info: " + userToAdd.getName() + " " + userToAdd.getUserId() + " " + userToAdd.getRole() + " " + userToAdd.getPassword());

            }
        } catch (FileNotFoundException e) {
            System.err.println("Users file not found: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("An error occurred:");
            System.out.println(e);
        }
    }

    public static void addUser(User thisUser) {
        String usersLine = thisUser.getUserId() + " " + thisUser.getName() + " " + thisUser.getPassword() + " " + thisUser.getRole();
        try (PrintWriter writer = new PrintWriter(new FileWriter("Users.txt", true))) {
            if (users.contains(thisUser)) {
                System.out.println("User already exists");
            } else {
                users.add(thisUser);
                writer.println(usersLine);
                System.out.println("User added successfully.");
            }
            writer.close();
        } catch (IOException e) {
            System.err.println("Error adding user: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        users.add(new User("student1", 23000110, "student", "Zx357]m2}<Hv"));
        users.add(new User("coordinator1", 11111111, "coordinator", "12I8q'8OJ>%\\"));
        users.add(new User("president1", 21004561, "president", "3cX2\\9BrbD!4"));
        System.out.println(authenticate("coordinator1", "12I8q'8OJ>%\\"));
        System.out.println(authenticate("president1", "3cX2\\9BrbD!4"));
        System.out.println(presidents.toString());
        System.out.println(coordinators.toString());
    }
}
