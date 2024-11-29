/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package bradford.ac.uk.bcs;

/**
 *
 * @author hakhta26
 */
public class NewMain {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        YearlyOfficers yo = new YearlyOfficers("bcs.txt");
        yo.openFiles("bcs21.txt", "bcs22.txt", 
                "bcs23.txt", "bcs24.txt");
        yo.separateOfficers();
        yo.closeFiles();
    }
    
}
