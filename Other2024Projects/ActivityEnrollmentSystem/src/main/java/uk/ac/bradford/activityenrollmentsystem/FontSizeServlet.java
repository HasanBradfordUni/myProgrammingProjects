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

@WebServlet("/fontSizeServlet")
public class FontSizeServlet extends HttpServlet {

    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response)
    throws ServletException, IOException {
        int newSize = Integer.parseInt(request.getParameter("textSize"));
        AccessibilityFeatures.setTextSize(newSize);
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        // Call your Java class here and send some response
        out.println(newSize);
    }
}

