/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package uk.ac.bradford.activityenrollmentsystem;

/**
 *
 * @author hakhta26
 */
// This is your Java Servlet that handles the form submission
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;
import javax.servlet.annotation.WebServlet;

@WebServlet("/loginServlet")
public class LoginServlet extends HttpServlet {

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        String name = request.getParameter("name");
        int UBnum = Integer.parseInt(request.getParameter("ubnumber"));
        String password = request.getParameter("password");

        AccessControl.getUsers();
        String role = AccessControl.authenticate(name, password);
        String pageRedirect = null;

        // Create or retrieve existing session
        HttpSession session = request.getSession();
        // Set user information as session attributes
        session.setAttribute("userLoggedIn", true);
        session.setAttribute("UBnum", UBnum);
        session.setAttribute("name", name);
        session.setAttribute("role", role);

        if (role != null) {
            if (role.equals("coordinator")) {
                pageRedirect = "<script>setTimeout(function(){ window.location.href = '/ActivityEnrollmentSystem/Co-ordinator.html'; }, 3000);</script>";
            } else if (role.equals("president")) {
                pageRedirect = "<script>setTimeout(function(){ window.location.href = '/ActivityEnrollmentSystem/President.html'; }, 3000);</script>";
            } else if (role.equals("student")) {
                pageRedirect = "<script>setTimeout(function(){ window.location.href = '/ActivityEnrollmentSystem/index.html'; }, 3000);</script>";
                String filePath = getServletContext().getRealPath("/") + "WEB-INF/Students.txt";
                DatabaseAdministrator.addStudent(name, UBnum, filePath);
            }
        } else {
            pageRedirect = "<script>setTimeout(function(){ window.location.href = '/ActivityEnrollmentSystem/index.html'; }, 3000);</script>";
        }

        // Send response back to the user
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<p>Login successful for user: " + name + "</p>");
        out.println("<p>Role: " + role + "</p>");
        out.println(pageRedirect);
        // ...
    }
}
