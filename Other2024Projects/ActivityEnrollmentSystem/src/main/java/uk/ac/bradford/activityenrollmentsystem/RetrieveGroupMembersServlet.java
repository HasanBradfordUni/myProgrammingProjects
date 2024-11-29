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
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

@WebServlet("/retrieveGroupMembersServlet")
public class RetrieveGroupMembersServlet extends HttpServlet {

    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {
        String groupName = "Pisoc";
        InputStream file2 = getServletContext().getResourceAsStream("/Students-ActivityGroups.txt");
        ArrayList<String> studentInGroups = President.retrieveEnrolledStudents(groupName, file2);
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        for (int i = 0; i < studentInGroups.size(); i++) {
            out.println(studentInGroups.get(i));
        }
        out.println(studentInGroups.size());
    }
}

