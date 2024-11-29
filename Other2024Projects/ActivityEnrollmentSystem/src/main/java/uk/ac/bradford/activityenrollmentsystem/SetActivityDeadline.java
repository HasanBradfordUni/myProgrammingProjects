package uk.ac.bradford.activityenrollmentsystem;

import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class SetActivityDeadline {

    public void setDeadline(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String dateString = request.getParameter("date");
        
        SimpleDateFormat dateFormat = new SimpleDateFormat("dd MM y");
        try {
            Date date = dateFormat.parse(dateString);
            System.out.println("Chosen deadline date: " + date);
        } catch (ParseException e) {
            System.out.println("Deadline could not be set: " + e.getMessage());
        }
    }
}
