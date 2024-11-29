


/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/UnitTests/JUnit5TestClass.java to edit this template
 */

//Hasan Akhtar
//UB: 23011124

import bradford.ac.uk.bcs.YearlyOfficers;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 *
 * @author hakhta26
 */
/*TEST DATA IS AS FOLLOWS (testOfficers.txt):
21204703 Erik Sutton Social Secretary
22667742 Gohar Kinsey Inclusion Officer
23819237 Michaeas Padilla President
24458589 Lucinda Reese Social Secretary
26309298 Nanaea Twist Campus Leagues Sports Rep
*/
public class TestOfficers {
    private static YearlyOfficers yo;
    
    public TestOfficers() {
    }
    
    @BeforeAll
    public static void setUpClass() {
        yo = new YearlyOfficers("testOfficers.txt");
    }
    
    @AfterAll
    public static void tearDownClass() {
    }
    
    @BeforeEach
    public void setUp() {
        yo.openFiles("testOfficers21.txt", "testOfficers22.txt", 
                "testOfficers23.txt", "testOfficers24.txt");
    }
    
    @AfterEach
    public void tearDown() {
        yo.closeFiles();
    }
    
    @Test
    public void testSepOfficers() {
        yo.separateOfficers();
    }
}
