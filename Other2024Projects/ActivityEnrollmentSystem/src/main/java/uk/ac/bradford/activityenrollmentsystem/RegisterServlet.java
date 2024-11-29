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

@WebServlet("/registerServlet")
public class RegisterServlet extends HttpServlet {
  @Override
  protected void doPost(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, IOException {
    
    String name = request.getParameter("name");
    String UBnum = request.getParameter("ubnumber");
    String password = request.getParameter("password");
    String password2 = request.getParameter("password2");
    
    String role = null;
    boolean UBnumValid;
    String pageContent = null;
    
    if (UBnum.startsWith("11") && UBnum.length() == 8) {
        role = "coordinator";
        UBnumValid = true;
    } else if (UBnum.startsWith("21") && UBnum.length() == 8) {
        role = "president";
        UBnumValid = true;
    } else {
        if (Validate.UBNumberValidation(UBnum)) {
            role = "student";
            UBnumValid = true;
        } else {
            role = null;
            UBnumValid = false;
        }
    }
    
    if (password.equals(password2) && UBnumValid) {
        AccessControl.getUsers();
        AccessControl.addUser(new User(name, Integer.parseInt(UBnum), role, password));
        pageContent = "<p>Registeration successful for user: " + name + "</p>";
    } else {
        pageContent = "<p>Registration unsuccessful for user: " + name + "</p>";
    }
    // Send response back to the user
    response.setContentType("text/html");
    PrintWriter out = response.getWriter();
    out.println(pageContent);
    out.println("<script>setTimeout(function(){ window.location.href = '/ActivityEnrollmentSystem/Login.html'; }, 1000);</script>");
    // ...
  }
}

