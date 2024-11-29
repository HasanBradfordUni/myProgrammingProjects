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
import java.nio.file.*;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

@WebServlet("/addActivityServlet")
public class AddActivityServlet extends HttpServlet {

    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {
        String groupName = request.getParameter("activityGroupName");
        String filePathString = getServletContext().getRealPath("/") + "WEB-INF/ActivityGroups.txt";
        Path path = Paths.get(filePathString);
        boolean exists = Files.exists(path);

        if (exists) {
            System.out.println("The file path exists.");
            System.out.println(filePathString);
        } else {
            System.out.println("The file path does not exist.");
        }
        String filePath = getServletContext().getRealPath("/") + "WEB-INF/ActivityGroups.txt";
        InputStream file = getServletContext().getResourceAsStream(filePath);
        DatabaseAdministrator.activityGroup(groupName, filePath, file);
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        // Call your Java class here and send some response
        out.println("Activity group added");
    }
}