package uk.ac.bradford.activityenrollmentsystem;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author Hasan Akhtar
 */
import java.io.*;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

@WebServlet("/readFromScreenServlet")
public class ReadFromScreenServlet extends HttpServlet {

    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {
        
        String textToRead = request.getParameter("textToRead");
        AccessibilityFeatures.readFromScreen(textToRead);
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        // Call your Java class here and send some response
        out.println("Screen reader working");
    }
}
