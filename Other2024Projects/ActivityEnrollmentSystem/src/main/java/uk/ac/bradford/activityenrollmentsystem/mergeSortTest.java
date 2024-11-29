package uk.ac.bradford.activityenrollmentsystem;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Random;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

/**
 *
 * @author hakhta26
 */
public class mergeSortTest {
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        List<Integer> activityGroupCounts = new ArrayList<Integer>();
        List<CustomMap> activityMapping = new ArrayList<>();
        Random rng = new Random();
        for (int i = 0; i < 4; i++) {
            int num = rng.nextInt(10);
            activityGroupCounts.add(num);
            int count = num;
            while (activityGroupCounts.contains(num)) {
                num = rng.nextInt(100);
            }
            String group = "foo"+num;
            activityMapping.add(new CustomMap(group, count));
        }
        System.out.println("The original counts are: ");
        for (int i = 0; i < activityMapping.size(); i++) {
            System.out.println("Activity: "+activityMapping.get(i).getFirst());
            System.out.println("Count: "+activityMapping.get(i).getSecond());
        }
        List<CustomMap> sortedGroupCounts = sortActivities(activityMapping);
        System.out.println("The sorted group counts are: ");
        for (int i = 0; i < activityMapping.size(); i++) {
            System.out.println("Activity: "+sortedGroupCounts.get(i).getFirst());
            System.out.println("Count: "+sortedGroupCounts.get(i).getSecond());
        }
    }
    
    public static List<CustomMap> sortActivities(List<CustomMap> groupCounts) {
        List<Integer> groups1, groups2;
        int listSize = groupCounts.size();
        if (groupCounts.size() > 1) {
            int m = groupCounts.size() / 2;
         
            List<CustomMap> L = new ArrayList<>(m);
            List<CustomMap> R = new ArrayList<>(listSize - m);

            for (int h = 0; h < m; h++)
                L.add(groupCounts.get(h));
            for (int b = m; b < listSize; b++)
                R.add(groupCounts.get(b));

            sortActivities(L);
            sortActivities(R);

            int i = 0, j = 0, k = 0;

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

            while (i < L.size()) {
                groupCounts.set(k, L.get(i));
                i++;
                k++;
            }

            while (j < R.size()) {
                groupCounts.set(k, R.get(j));
                j++;
                k++;
            }
        }
        return groupCounts;
    }
}
