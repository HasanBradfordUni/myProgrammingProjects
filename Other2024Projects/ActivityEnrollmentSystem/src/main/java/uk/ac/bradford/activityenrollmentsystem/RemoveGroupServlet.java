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
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

@WebServlet("/removeGroupServlet")
public class RemoveGroupServlet extends HttpServlet {

    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {
        String groupName = request.getParameter("groupToRemove");
        String filePath1 = getServletContext().getRealPath("/") + "WEB-INF/ActivityGroups.txt";
        String filePath2 = getServletContext().getRealPath("/") + "WEB-INF/Students-ActivityGroups.txt";
        InputStream file1 = getServletContext().getResourceAsStream("/ActivityGroups.txt");
        InputStream file2 = getServletContext().getResourceAsStream("/Students-ActivityGroups.txt");
        DatabaseAdministrator.removeActivityGroup(groupName, filePath1, filePath2, file1, file2);
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("Group removed successfully");
    }
}

