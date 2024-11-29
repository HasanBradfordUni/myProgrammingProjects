/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/JSP_Servlet/Servlet.java to edit this template
 */
package uk.ac.bradford.activityenrollmentsystem;

import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 *
 * @author Hasan Akhtar
 */
@WebServlet(name = "EnrollmentServlet", urlPatterns = {"/enrollmentServlet"})
public class EnrollmentServlet extends HttpServlet {

    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String activityGroupName = request.getParameter("activityGroup");
        HttpSession session = request.getSession(false); // false means do not create a new session
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        if (session != null) {
            boolean userLoggedIn = (boolean) session.getAttribute("userLoggedIn");
            int UBnum = (int) session.getAttribute("UBnum");
            if (userLoggedIn) {
                String filePath = getServletContext().getRealPath("/") + "WEB-INF/Students-ActivityGroups.txt";
                InputStream file = getServletContext().getResourceAsStream("/Students-ActivityGroups.txt");
                DatabaseAdministrator.enrollStudent(UBnum, activityGroupName, file, filePath);
                // Call your Java class here and send some response
                out.println("Student with ID " + UBnum + " is now enrolled in activity with group name " + activityGroupName);
            }
        } else {
            out.println("Cannot enroll in activity! Not Logged in!");
        }
    }
}
