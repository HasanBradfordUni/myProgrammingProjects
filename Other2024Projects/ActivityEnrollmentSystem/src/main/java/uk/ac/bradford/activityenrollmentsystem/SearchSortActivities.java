package uk.ac.bradford.activityenrollmentsystem;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;

/**
 * The class that will be used to process the admin commands of searching 
 * through and sorting activity groups using the members count by the 
 * Activity Co-ordinator. It has a few methods, including a binary search and 
 * merge sort method being the main ones. The other methods are used to aid 
 * with the searching/sorting processes.
 */
public class SearchSortActivities {
    
    /**
     * The first attribute is a constant (meaning it can't be changed at run time)
     * and stores the activity groups list for when the class is first instantiated.
     * The type is a List of Strings and the name is ALL_GROUPS.
     * It is used to keep track of all the activity groups that exist from the database.
     */
    private static File file1 = new File("ActivityGroups.txt");
    private static File file2 = new File("Student-ActivityGroups.txt");
    private static InputStream inputStream;
    private static List<String> ALL_GROUPS;
    /**
     * The second attribute is not a constant (meaning it can be changed at run time)
     * and stores the students enrolled in activity groups list.
     * The type is an ArrayList of Strings and the name is studentAndActivityGroup.
     * It is used to count the number of students enrolled in each group.
     */
    private static ArrayList<String> studentAndActivityGroup;

    /**
     * This method returns a linked hash map of  the activity groups and their 
     * members based on the groups list and enrolment list.
     * @param allGroups
     * @param studentAndActivityGroup
     * @return activityStudentsMapping
     */
    public static LinkedHashMap<String, Integer> getActivityCountMapping(List<String> allGroups, ArrayList<String> studentAndActivityGroup) {
        //Initialising variables
        Integer count = 0;
        LinkedHashMap<String, Integer> activityStudentsMapping = new LinkedHashMap<>();
        //Using a for loop to iterate over the lists
        for (String activityGroup : allGroups) {
            //Adding the activity with a count of 0 to the linked hash map
            activityStudentsMapping.put(activityGroup, 0);
        }
        for (String line : studentAndActivityGroup) {
            //Obtaing only the activity from the enrollment list
            String activity = line.strip().split(" ", 2)[1];
            if (activityStudentsMapping.containsKey(activity)) {
                //incrementing the count and adding it back into the linked hash map
                count = activityStudentsMapping.get(activity);
                count++;
                activityStudentsMapping.put(activity, count);
            }
        }
        return activityStudentsMapping;
    }

    /**
     * This method maps the linked hash map returned from the previous method 
     * to a list that utilises a custom data type so it can be sorted.
     * @param activityCountMapping
     * @return activityGroupCounts
     */
    public static List<CustomMap> getGroupCounts(HashMap<String, Integer> activityCountMapping) {
        //Initialising variables
        List<CustomMap> activityGroupCounts = new ArrayList<>();
        int index = 0;
        //Uisng a for loop to iterate over the linked hash map
        for (String activityGroup : activityCountMapping.keySet()) {
            //Using the custom data type to map a linked hash map to a list
            activityGroupCounts.add(new CustomMap(activityGroup, activityCountMapping.get(activityGroup)));
            index++;
        }
        return activityGroupCounts;
    }

    /**
     * This method uses merge sort to sort the integer parts of the custom data
     * type stored in the list while maintaining the position of the activity groups
     * with their respective member counts.
     * @param groupCounts
     * @return groupCounts
     */
    public static List<CustomMap> sortActivities(List<CustomMap> groupCounts) {
        //Setting up variables
        List<Integer> groups1, groups2;
        int listSize = groupCounts.size();
        //If statement used to distinguish between base case and normal case
        if (groupCounts.size() > 1) {
            //Setting up internal variables
            int m = groupCounts.size() / 2;
         
            List<CustomMap> L = new ArrayList<>(m);
            List<CustomMap> R = new ArrayList<>(listSize - m);

            //Setting up left and right lists
            for (int h = 0; h < m; h++)
                L.add(groupCounts.get(h));
            for (int b = m; b < listSize; b++)
                R.add(groupCounts.get(b));

            //Calling itself recursively
            sortActivities(L);
            sortActivities(R);
            
            //Setting up varaibles required for merging/sorting
            int i = 0, j = 0, k = 0;

            //Using the while loop to merge together right and left lists in a sorted manner
            while (i < L.size() && j < R.size()) {
                if (L.get(i).getSecond() <= R.get(j).getSecond()) {
                    groupCounts.set(k, L.get(i));
                    i++;
                } else {
                    groupCounts.set(k, R.get(j));
                    j++;
                }
                k++;
            }
            
            //Merging together any leftover elements from the right list
            while (i < L.size()) {
                groupCounts.set(k, L.get(i));
                i++;
                k++;
            }

            //Merging together any leftover elements from the left list
            while (j < R.size()) {
                groupCounts.set(k, R.get(j));
                j++;
                k++;
            }
        }
        return groupCounts;
    }

    /**
     * This method uses binary search methods to find a range of values that match 
     * the parameter item which is declared as an Integer.
     * @param groupCounts
     * @param item
     * @return filteredActivities
     */
    public static HashMap<String, Integer> searchActivities(List<CustomMap> groupCounts, Integer item) {
        //Calls the two binary search methods to find the indices of the first and last occurrence of item in the list
        int startIndex = findStart(groupCounts, item);
        int endIndex = findEnd(groupCounts, item);
        //Initailises a new hash map that is returned
        HashMap<String, Integer> filteredActivities = new HashMap<String, Integer>();
        //Uses a for loop to insert all the elements between the starting and ending indices into the hash map
        for (int i = startIndex; i <= endIndex; i++) {
            filteredActivities.put(groupCounts.get(i).getFirst(), groupCounts.get(i).getSecond());
        }
        return filteredActivities;
    }

    /**
     * This method uses a binary search to find the first occurrence of an 
     * Integer item in a list.
     * @param array
     * @param key
     * @return left 
     */
    public static int findStart(List<CustomMap> array, int key) {
        //Inialises some variables first
        int left = 0;
        int right = array.size() - 1;

        //Uses a while loop to actually carry out the search
        while (left < right) {
            //Calculates the new middle index
            int mid = left + (right - left) / 2;
            //Uses the if statement to check if the middle element is less than the key
            if (array.get(mid).getSecond() < key) {
                //If it is, left becomes the middle index + 1
                left = mid + 1;
            } else {
                //Otherwise, right becomes the middle index
                right = mid;
            }
        }

        return left;
    }

    /**
     * This method uses a binary search to find the last occurrence of an 
     * Integer item in a list.
     * @param array
     * @param key
     * @return left 
     */
    public static int findEnd(List<CustomMap> array, int key) {
        //Inialises some variables first
        int left = 0;
        int right = array.size() - 1;

        //Uses a while loop to actually carry out the search
        while (left < right) {
            //Calculates the new middle index
            int mid = left + (right - left + 1) / 2;
            //Uses the if statement to check if the middle element is less than or equal to the key
            if (array.get(mid).getSecond() <= key) {
                //If it is, left becomes the middle index
                left = mid;
            } else {
                //Otherwise, right becomes the middle index - 1
                right = mid - 1;
            }
        }

        return right;
    }
    
    /**
     * This method returns all the activity groups and their counts if their 
     * counts are less than 3 by calling the binary search methods above and 
     * merging the hash maps together for 0, 1 & 2 members.
     * @param sortedGroupCounts
     * @return filteredActivities
     */
    public static HashMap<String, Integer> filterActivities(List<CustomMap> sortedGroupCounts) {
        //Inialises some variables first
        HashMap<String, Integer> filteredActivities = new HashMap<>();
        HashMap<String, Integer> searchedActivities = new HashMap<>();
        
        //Uses a for loop from 2 to (and including) 0 and calls the searchActivities method each time
        for (int i = 2; i >= 0; i--) {
            searchedActivities = searchActivities(sortedGroupCounts, i);
            //Also merges the 2 hash maps together each time
            filteredActivities.putAll(searchedActivities);
        }
        return filteredActivities;
    }

    /**
     * Main method for testing code while building, calling the methods and 
     * ensure they work properly (no syntax errors, run-time errors etc).
     * @param args 
     */
    public static void main(String[] args) {
        try {
            inputStream = new FileInputStream(file1);
            ALL_GROUPS = DatabaseAdministrator.getAllActivityGroups(inputStream);
            inputStream = new FileInputStream(file2);
            studentAndActivityGroup = DatabaseAdministrator.getStudentActivityGroups(inputStream);
        } catch (Exception e) {
            System.out.println("An exception with files: "+e);
        }
        LinkedHashMap<String, Integer> activityCountMapping = getActivityCountMapping(ALL_GROUPS, studentAndActivityGroup);
        System.out.println("The original list of activities and their member counts is as follows:");
        for (String i : activityCountMapping.keySet()) {
            System.out.println("Activity: " + i + ", Members: " + activityCountMapping.get(i));
        } 
        List<CustomMap> groupCounts = getGroupCounts(activityCountMapping);
        List<CustomMap> sortedGroupCounts = sortActivities(groupCounts);
        HashMap<String, Integer> allFilteredActivities = filterActivities(sortedGroupCounts);
        System.out.println("The sorted list of activities and their member counts is as follows:");
        for (int i = 0; i < groupCounts.size(); i++) {
            System.out.println("Activity: "+sortedGroupCounts.get(i).getFirst());
            System.out.println("Members Count: "+sortedGroupCounts.get(i).getSecond());
        }
        System.out.println("The filtered [for less than 3 members] list of activities and their member counts is as follows:");
        for (String i : allFilteredActivities.keySet()) {
            System.out.println("Activity: " + i + ", Members: " + allFilteredActivities.get(i));
        }
    }
}
