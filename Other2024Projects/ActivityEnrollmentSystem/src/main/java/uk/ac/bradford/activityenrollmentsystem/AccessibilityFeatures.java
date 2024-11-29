package uk.ac.bradford.activityenrollmentsystem;

import java.util.*;
/**
 *
 * @author sullah19
 */
public class AccessibilityFeatures {
    private static Random rng = new Random();
    private static String[] colours = {"black", "white"};
    private static String defaultColour = "white";
    private static Scanner keyboard = new Scanner(System.in);
    
    public static String getColour() {
        String thisColour = null;
        return thisColour;
    }
    
    public static String setColour(boolean colourButtonPressed, String currentColour) {
        String colour = null;
        if (colourButtonPressed) {
            if (currentColour.equalsIgnoreCase(colours[0])) {
                colour = colours[1];
            } else {
                colour = colours[0];
            }
            System.out.println("the webpage will now become: "+colour);
        }
        return colour;
    }
    
    public static String getTextFromScreen() {
        String text = null;
        System.out.println("Enter text for the screen reader: ");
        text = keyboard.nextLine();
        return text;
    }
    
    public static void useScreenReader(boolean srButtonPressed) {
        String thisText = getTextFromScreen();
        readFromScreen(thisText);
    }
    
    public static void readFromScreen(String textToRead) {
        try {
            TextToSpeech.speakText(textToRead);
        } catch (Exception e) {
            e.printStackTrace();
        }
    } 
    
    public static int getTextSize() {
        System.out.println("Enter the new text size (10-50): ");
        int textSize = keyboard.nextInt();
        return textSize;
    }
    
    public static void setTextSize(int newTextSize) {
        System.out.println("The new text size has been set to: "+newTextSize);
    }
    
    public static void changeTextSize(boolean tsButtonPressed) {
        int thisTextSize = getTextSize();
        setTextSize(thisTextSize);
    }
    
    public static void main(String[] args) {
        setColour(true, "black");
        useScreenReader(true);
        changeTextSize(true);
    }
}
