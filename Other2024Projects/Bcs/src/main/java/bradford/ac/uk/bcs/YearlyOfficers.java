package bradford.ac.uk.bcs;

//Hasan Akhtar
//UB: 23011124
import java.util.*;
import java.io.*;
import java.util.regex.*;
import java.time.ZonedDateTime;

/**
 *The YearlyOfficers class is responsible for taking a file full of student UB
 * numbers, names and society roles and organise it into 4 new files based on
 * the year of registry for each student. It contains 3 methods, 
 * <a href="#openFiles(java.lang.String,java.lang.String,java.lang.String,java.lang.String)">openFiles()</a>,
 * <a href="#separateOfficers()">separateOfficers()</a> and 
 * <a href="#closeFiles()">closeFiles()</a>.
 * 
 * @author hakhta26
 */
public class YearlyOfficers {

    /**
     * The attribute storing the file name for the initial variable
     * (set in the constructor method) for the input file.
     * @see inputFile (attribute)
     */
    private String fileName;
    
    /**
     * The attribute storing the BufferedReader object for the
     * input file. Used in openFiles() with the fileName attribute.
     * @see fileName (attribute)
     */
    private BufferedReader inputFile;
    
    /**
     * The attribute storing the first outputFile as a file object for. 
     * Used in openFiles() to open a new file.
     * @see pw21 (attribute)
     */
    private File outputFile1;
    
    /**
     * The attribute storing the second outputFile as a file object for. 
     * Used in openFiles() to open a new file.
     * @see pw22 (attribute)
     */
    private File outputFile2;
    
    /**
     * The attribute storing the third outputFile as a file object for. 
     * Used in openFiles() to open a new file.
     * @see pw23 (attribute)
     */
    private File outputFile3;
    
    /**
     * The attribute storing the final outputFile as a file object for. 
     * Used in openFiles() to open a new file.
     * @see pw24 (attribute)
     */
    private File outputFile4;
    
    /**
     * An integer storing the officers count for the year 2021. 
     * This is incremented in separateOfficers() and displayed in closeFiles().
     */
    private int officersCount21;
    
    /**
     * An integer storing the officers count for the year 2022. 
     * This is incremented in separateOfficers() and displayed in closeFiles().
     */
    private int officersCount22;
    
    /**
     * An integer storing the officers count for the year 2023. 
     * This is incremented in separateOfficers() and displayed in closeFiles().
     */
    private int officersCount23;
    
    /**
     * An integer storing the officers count for the year 2024. 
     * This is incremented in separateOfficers() and displayed in closeFiles().
     */
    private int officersCount24;
    
    /**
     * The attribute storing the PrintWriter object for the
     * logger file. Used in openFiles() to open the logger file.
     */
    private PrintWriter loggerFile;
    
    /**
     * The attribute storing the PrintWriter object for the
     * first output file. Used in separateOfficers() to allow writing to the 
     * output file for the year 2021 in conjunction with the outputFile1 attribute.
     * @see outputFile1 (attribute)
     */
    private PrintWriter pw21 = null;
    
    /**
     * The attribute storing the PrintWriter object for the
     * second output file. Used in separateOfficers() to allow writing to the 
     * output file for the year 2022 in conjunction with the outputFile2 attribute.
     * @see outputFile2 (attribute)
     */
    private PrintWriter pw22 = null;
    
    /**
     * The attribute storing the PrintWriter object for the
     * third output file. Used in separateOfficers() to allow writing to the 
     * output file for the year 2023 in conjunction with the outputFile3 attribute.
     * @see outputFile3 (attribute)
     */
    private PrintWriter pw23 = null;
    
    /**
     * The attribute storing the PrintWriter object for the
     * final output file. Used in separateOfficers() to allow writing to the 
     * output file for the year 2024 in conjunction with the outputFile4 attribute.
     * @see outputFile4 (attribute)
     */
    private PrintWriter pw24 = null;

    /**
     * The constructor method for the YearlyOfficers class. It sets the name
     * for the main input file to be used accordingly in openFiles(), 
     * separateOfficers() and also closeFiles()
     * @param thisFileName - the name of the input to be used with this instance
     */
    public YearlyOfficers(String thisFileName) {
        fileName = thisFileName;
    }
    
    /**
     * Method openFiles() - this method uses a try and catch to first assign a 
     * BufferedReader object for the <strong>bcs.txt</strong> file into a variable,
     * this variable is declared at the top of the class before any methods. 
     * It then uses 4 try and catches to create each of the files that are to be 
     * written to individually <i>(i.e. one at a time)</i> 
     * [the files <strong>bcs21.txt</strong>, <strong>bcs22.txt</strong>, 
     * <strong>bcs23.txt</strong> and <strong>bcs24.txt</strong>] 
     * based on the parameters passed in for each file name. 
     * Also a logger file is opened in append mode.
     * The logger file is also written to upon any errors with the current time
     * of the error (including the date) and also the actual error.
     * @see <a href="https://howtodoinjava.com/java/io/java-append-to-file/">
     * Appending to a File in Java, Gupta, 2022</a>
     * @param outputFileName1 - for the file name of the first output file
     * @param outputFileName2 - for the file name of the second output file
     * @param outputFileName3 - for the file name of the third output file
     * @param outputFileName4 - for the file name of the final output file
     */
    public void openFiles(String outputFileName1, String outputFileName2,
            String outputFileName3, String outputFileName4) {
        try {
            loggerFile = new PrintWriter(new FileWriter("errorLogger.txt", true));
        } catch (Exception e) {
            System.out.println("Error opening file! Cannot be logged!");
        }
        try {
            inputFile = new BufferedReader(new FileReader(fileName));
        } catch (FileNotFoundException e) {
            System.out.println("Error: File not found!");
            ZonedDateTime now = ZonedDateTime.now();
            loggerFile.print(now);
            loggerFile.print("\r\n");
            loggerFile.print(e);
            loggerFile.print("\r\n");
        } catch (IOException e) {
            System.out.println("Error: File cannot be opened!");
            ZonedDateTime now = ZonedDateTime.now();
            loggerFile.print(now);
            loggerFile.print("\r\n");
            loggerFile.print(e);
            loggerFile.print("\r\n");
        }
        try {
            outputFile1 = new File(outputFileName1);
        } catch (Exception e) {
            System.out.println("Error: File cannot be created!");
            ZonedDateTime now = ZonedDateTime.now();
            loggerFile.print(now);
            loggerFile.print("\r\n");
            loggerFile.print(e);
            loggerFile.print("\r\n");
        }
        try {
            outputFile2 = new File(outputFileName2);
        } catch (Exception e) {
            System.out.println("Error: File cannot be created!");
            ZonedDateTime now = ZonedDateTime.now();
            loggerFile.print(now);
            loggerFile.print("\r\n");
            loggerFile.print(e);
            loggerFile.print("\r\n");
        }
        try {
            outputFile3 = new File(outputFileName3);
        } catch (Exception e) {
            System.out.println("Error: File cannot be created!");
            ZonedDateTime now = ZonedDateTime.now();
            loggerFile.print(now);
            loggerFile.print("\r\n");
            loggerFile.print(e);
            loggerFile.print("\r\n");
        }
        try {
            outputFile4 = new File(outputFileName4);
        } catch (Exception e) {
            System.out.println("Error: File cannot be created!");
            ZonedDateTime now = ZonedDateTime.now();
            loggerFile.print(now);
            loggerFile.print("\r\n");
            loggerFile.print(e);
            loggerFile.print("\r\n");
        }

    }

    /**
     * Method seperateOfficers() – This method first initialises some variables for
     * the reading of the <b>bcs.txt</b> file and then sets up some regular expression patterns
     * (Java Regular Expressions, Refsnes Data) for the processing of each line read 
     * from <b>bcs.txt</b>. Next, the PrintWriter class is used to make each file available 
     * for writing to. Each pattern is then matched to the word using the .matcher() 
     * method of each pattern. (Java Regular Expressions, Refsnes Data) 
     * The .find() method of each pattern is then used in if statements to check 
     * which pattern matches with the UB number and therefore that corresponding file 
     * is written to and that corresponding <i>officersCount</i> is incremented. 
     * If it doesn't match any pattern, then a suitable message is outputted and the 
     * line isn't appended to any of the files, nor any of the <i>officersCount</i>
     * attributes incremented. It does this until it reaches the end of the file 
     * (<i>line</i> equal to <b><i>null</i></b>) in a do-while loop. 
     * It also includes exception handling and error logging. 
     * @see <a href="https://www.w3schools.com/java/java_regex.asp">Java Regex</a>
     * @see Pattern matcher
     * @see Pattern find
     */
    public void separateOfficers() {
        String line = " ";
        StringTokenizer tokenizer = null;
        String thisWord = null;
        
        Pattern pattern1 = Pattern.compile("^21");
        Pattern pattern2 = Pattern.compile("^22");
        Pattern pattern3 = Pattern.compile("^23");
        Pattern pattern4 = Pattern.compile("^24");
        
        boolean matchFound21;
        boolean matchFound22;
        boolean matchFound23;
        boolean matchFound24;

        try {
            pw21 = new PrintWriter(outputFile1);
            pw22 = new PrintWriter(outputFile2);
            pw23 = new PrintWriter(outputFile3);
            pw24 = new PrintWriter(outputFile4);
        } catch (FileNotFoundException e) {
            System.out.println("Error: File not found!");
            ZonedDateTime now = ZonedDateTime.now();
            loggerFile.print(now);
            loggerFile.print("\r\n");
            loggerFile.print(e);
            loggerFile.print("\r\n");
        } catch (IOException e) {
            System.out.println("Error: File cannot be opened!");
            ZonedDateTime now = ZonedDateTime.now();
            loggerFile.print(now);
            loggerFile.print("\r\n");
            loggerFile.print(e);
            loggerFile.print("\r\n");
        } finally {
            do {
                try {
                    line = inputFile.readLine();
                    if (line != null) {
                        tokenizer = new StringTokenizer(line);
                        if (tokenizer.hasMoreTokens()) {
                            thisWord = tokenizer.nextToken();
                            
                            Matcher matcher21 = pattern1.matcher(thisWord);
                            Matcher matcher22 = pattern2.matcher(thisWord);
                            Matcher matcher23 = pattern3.matcher(thisWord);
                            Matcher matcher24 = pattern4.matcher(thisWord);
                            matchFound21 = matcher21.find();
                            matchFound22 = matcher22.find();
                            matchFound23 = matcher23.find();
                            matchFound24 = matcher24.find();
                            
                            if (matchFound21) {
                                pw21.println(line);
                                officersCount21++;
                            } else if (matchFound22) {
                                pw22.println(line);
                                officersCount22++;
                            } else if (matchFound23) {
                                pw23.println(line);
                                officersCount23++;
                            } else if (matchFound24) {
                                pw24.println(line);
                                officersCount24++;
                            } else {
                                System.out.println("Record doesn't fit in a file!");
                            }
                        }
                    }
                } catch (IOException e) {
                    System.out.println("Error: File cannot be read from!");
                    ZonedDateTime now = ZonedDateTime.now();
                    loggerFile.print(now);
                    loggerFile.print("\r\n");
                    loggerFile.print(e);
                    loggerFile.print("\r\n");
                    break;
                } catch (NullPointerException e) {
                    System.out.println("Error: File not defined!");
                    ZonedDateTime now = ZonedDateTime.now();
                    loggerFile.print(now);
                    loggerFile.print("\r\n");
                    loggerFile.print(e);
                    loggerFile.print("\r\n");
                    break;
                }
            } while (line != null);
        }
    }

    /**
     * Method closeFiles() – This method firstly initialises an array of integers of 
     * length 4 for the <i>officersCount</i> attributes. 
     * Then it uses exception handling to close the files, catching and 
     * logging any errors that arise from this. It also uses exception handling 
     * to insert the <i>officersCount</i> attributes into their respective 
     * positions in the array and to output them, catching and logging any 
     * errors arising from this also. 
     * Finally, it returns the <i>officersCountList</i>.
     * @return officersCountList - a list of the counts of the officers for each year
     */
    public int[] closeFiles() {
        int[] officersCountList = new int[4];
        try {
            inputFile.close();
        } catch (Exception e) {
            System.out.println("An error occured!");
            ZonedDateTime now = ZonedDateTime.now();
            loggerFile.print(now);
            loggerFile.print("\r\n");
            loggerFile.print(e);
            loggerFile.print("\r\n");
        } try {
            pw21.close();
            pw22.close();
            pw23.close();
            pw24.close();
        }  catch (Exception e) {
            System.out.println("An error occured!");
            ZonedDateTime now = ZonedDateTime.now();
            loggerFile.print(now);
            loggerFile.print("\r\n");
            loggerFile.print(e);
            loggerFile.print("\r\n");
        } try {
            officersCountList[0] = officersCount21;
            officersCountList[1] = officersCount22;
            officersCountList[2] = officersCount23;
            officersCountList[3] = officersCount24;
            for (int i = 0; i < officersCountList.length; i++) {
                String year = String.valueOf(i+21);
                int index = fileName.indexOf(".");
                String fileNameYear = fileName.substring(0, index)+
                        year+fileName.substring(index);
                System.out.println("The officers count for "+
                        fileNameYear+" is: "+officersCountList[i]);
            }
        } catch (Exception e) {
            System.out.println("An error occured!");
            ZonedDateTime now = ZonedDateTime.now();
            loggerFile.print(now);
            loggerFile.print("\r\n");
            loggerFile.print(e);
            loggerFile.print("\r\n");
        } try {
            loggerFile.close();
        }  catch (Exception e) {
            System.out.println("An error occured!");
            ZonedDateTime now = ZonedDateTime.now();
            loggerFile.print(now);
            loggerFile.print("\r\n");
            loggerFile.print(e);
            loggerFile.print("\r\n");
        }
        return officersCountList;
    }
}
