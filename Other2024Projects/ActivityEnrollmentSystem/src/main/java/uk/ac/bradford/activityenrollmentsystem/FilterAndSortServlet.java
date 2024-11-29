package uk.ac.bradford.activityenrollmentsystem;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
/**
 *
 * @author hakhta26
 */
import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

@WebServlet("/filterAndSortServlet")
public class FilterAndSortServlet extends HttpServlet {

    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String filter = request.getParameter("filter");
        System.out.println(filter);
        String filePathString1 = getServletContext().getRealPath("/") + "WEB-INF/ActivityGroups.txt";
        String filePathString2 = getServletContext().getRealPath("/") + "WEB-INF/Students-ActivityGroups.txt";
        InputStream file1 = getServletContext().getResourceAsStream(filePathString1);
        InputStream file2 = getServletContext().getResourceAsStream(filePathString2);
        List<String> groups = DatabaseAdministrator.getAllActivityGroups(file1);
        ArrayList<String> groupMappings = DatabaseAdministrator.getStudentActivityGroups(file2);
        LinkedHashMap<String, Integer> activityCountMapping = SearchSortActivities.getActivityCountMapping(groups, groupMappings);
        List<CustomMap> groupCounts = SearchSortActivities.getGroupCounts(activityCountMapping);
        List<CustomMap> sortedGroupCounts = SearchSortActivities.sortActivities(groupCounts);
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        if (filter.equalsIgnoreCase("true")) {
            HashMap<String, Integer> allFilteredActivities = SearchSortActivities.filterActivities(sortedGroupCounts);
            for (String i : allFilteredActivities.keySet()) {
                String line = i + " " + allFilteredActivities.get(i);
                out.println(line);
            }
        } else {
            for (int i = 0; i < sortedGroupCounts.size(); i++) {
                String line = sortedGroupCounts.get(i).getFirst() + " " + sortedGroupCounts.get(i).getSecond();
                out.println(line);
            }
        }
    }
}
