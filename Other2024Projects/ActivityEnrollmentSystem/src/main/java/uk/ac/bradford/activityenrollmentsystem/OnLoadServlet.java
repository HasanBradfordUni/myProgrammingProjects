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

@WebServlet("/onLoadServlet")
public class OnLoadServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        // Create or retrieve existing session
        HttpSession session = request.getSession();
        String firstLoad = (String) session.getAttribute("firstLoad");
        String role = (String) session.getAttribute("role");
        
        // Send response back to the user
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        
        if (firstLoad == null) {
            session.setAttribute("firstLoad", "true");
        } else {
            session.setAttribute("firstLoad", "false");
        }
        // Set user information as session attributes
        firstLoad = (String) session.getAttribute("firstLoad");
        if (firstLoad.equals("true")) {
            session.setAttribute("userLoggedIn", false);
            session.setAttribute("UBnum", null);
            session.setAttribute("username", null);
            session.setAttribute("role", null);        
        } else {
            session.setAttribute("userLoggedIn", (String) session.getAttribute("userLoggedIn"));
            session.setAttribute("UBnum", (String) session.getAttribute("UBnum"));
            session.setAttribute("username", (String) session.getAttribute("username"));
            session.setAttribute("role", (String) session.getAttribute("role"));  
        }
        // ...
    }
}
