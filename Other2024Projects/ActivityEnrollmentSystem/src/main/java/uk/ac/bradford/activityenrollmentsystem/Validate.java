/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */
package uk.ac.bradford.activityenrollmentsystem;
import java.util.Scanner;
/**
 *
 * @author uzair
 */
public class Validate {

    public static boolean UBNumberValidation(String UBNumber) {
        // Checks that the UB number is 8 characters
    if (UBNumber.length() != 8){
        return false;
    }
        // Checks that the UB Number is only numbers
    if (!UBNumber.matches("[0-9]+")){
        return false;
    }
        // Checks that the UB Number starts with the correct prefix
    String[] correctPrefixes = {"21","22","23","24"};
    boolean correctPrefix = false;
    for (String prefix : correctPrefixes){
        if (UBNumber.startsWith(prefix)){
            correctPrefix = true;
            break;
        }
    }
    return correctPrefix;
    }
    public static void main(String[] args){
        Scanner userInput = new Scanner(System.in);
        // Takes the Users Input for the UB Number and outputs the result
        System.out.print("Enter UB Number: ");
        String UBNumber = userInput.nextLine();
        
        if(UBNumberValidation(UBNumber)){
            System.out.println("The UB Number is valid");
        } else{
            System.out.println("The UB Number is invalid");
        }
    }
}
