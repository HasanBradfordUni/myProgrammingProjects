"""
Basic Hours calculator

A calculator that calulates the amount of hours you have worked for however many working days you want based on the inputs of:
 *   Start time
 *   End time
 *   Lunch start time
 *   Lunch end time

Essentialy it calculates the difference between the end time and start time on each day and subtracts the difference 
between the lunch start time and end time. It does this for each day that is input and add the totals of the hours for a 
cumalutive total of hours worked across the days. It can also tell the average hours per day and if you input how many hours 
you should be working per day/week, the overtime/undertime based on those hours. In a future extension, the pay may be added 
as well so you can see how much pay you should be receiving for those hours based on either the pay per hour, day, week, month or year.

This is now version 5 which is adapted from version 1 to host a graphical user interface and now extra functionalities can be added
"""
#Basic imports first

from datetime import datetime
from tkinter import *
from tkinter import ttk
from tkscrolledframe import ScrolledFrame
from math import *

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        widget.bind("<Enter>", self.show_tooltip)
        widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        if self.tooltip_window or not self.text:
            return
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tooltip_window = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(True)  # Remove window decorations
        tw.wm_geometry(f"+{x}+{y}")
        label = Label(tw, text=self.text, background="yellow", relief="solid", borderwidth=1, padx=5, pady=5)
        label.pack()

    def hide_tooltip(self, event=None):
        tw = self.tooltip_window
        self.tooltip_window = None
        if tw:
            tw.destroy()

class BasicApp():
  def __init__(self):
    self.dayNum = 1
    self.totalHours = 0
   
  #Below is the method that takes the times entered as integers and converts them to actual datetime objects 
  def convertTimes(self, startTime, endTime, lunchStart, lunchEnd):
    newST = datetime.strptime(startTime, "%H:%M")
    newET = datetime.strptime(endTime, "%H:%M")
    newLS = datetime.strptime(lunchStart, "%H:%M")
    newLE = datetime.strptime(lunchEnd, "%H:%M")
    return newST, newET, newLS, newLE
  
  #Below is the method that takes the converted times and works out the time difference in hours
  def calculateHours(self, convertedST, convertedET, convertedLS, convertedLE):
    dayDifference = convertedET - convertedST
    breakTime = convertedLE - convertedLS
    dayHours = dayDifference.total_seconds() / 3600
    breakHours = breakTime.total_seconds() / 3600
    hours = dayHours - breakHours
    return hours
  
  #Below is the method that outputs the hours
  def outputHours(self, hours):
    print("The hours worked on Day "+str(self.dayNum)+" (in decimal format):")
    print(round(hours, 2))
    print("The total hours you have worked (so far) is:")
    print(self.totalHours)
    altOutput = input("Do you wish to view the hours in hours and minutes format (Y/N)? ")
    altHours = hours // 1
    altMinutes = round((hours - altHours) * 60, 0)
    altTotalHours = self.totalHours // 1
    altTotalMinutes = round((self.totalHours - altTotalHours) * 60, 0)
    print(altOutput.upper())
    if altOutput.upper() == "Y":
      print("The hours worked on Day "+str(self.dayNum)+" (in hours and minutes format):")
      print(str(altHours)+" hours and "+str(altMinutes)+" minutes")
      print("The total hours you have worked (so far) is:")
      print(str(altTotalHours)+" hours and "+str(altTotalMinutes)+" minutes")

  #Below is the function that checks the total hours against how many hours the worker should be doing
  def calculateOvertimeUndertime(self, hoursPerDay):
    overtime = True
    hours = self.totalHours - (hoursPerDay * self.dayNum)
    absoluteHours = abs(hours)
    justHours = absoluteHours // 1
    justMinutes = round((absoluteHours - justHours) * 60, 0)
    if hours < 0:
      overtime = False
    return justHours, justMinutes, overtime
  
  #Core functionality, taking inputs and calling functions
  def takeInputs(self):
    print("You have chosen to use the basic insertion method")
    contractedHours = int(input("Enter how many hours you should be working: "))
    print("Is this either in:")
    print("1. Hours per day")
    print("2. Hours per week")
    perDayOrPerWeek = int(input("Enter either 1 or 2: "))
    hoursPerDay = 0
    if perDayOrPerWeek == 1:
      hoursPerDay = contractedHours
    elif perDayOrPerWeek == 2:
      hoursPerDay = contractedHours / 5

    while True:
      print("Day "+str(self.dayNum)+" :")
      times = input("Enter the working times for the day:\n")
      startTime = times[times.find("Start")+6:times.find(",")]
      endTime = times[times.find("End")+4:times.find("Lunch")-2]
      lunchStart = times[times.find("Lunch")+6:times.find("-")]
      lunchEnd = times[times.find("-")+1:]
      convertedST, convertedET, convertedLS, convertedLE = self.convertTimes(startTime, endTime, lunchStart, lunchEnd)
      hours = self.calculateHours(convertedST, convertedET, convertedLS, convertedLE)
      self.totalHours += hours
      self.outputHours(hours)
      addMoreDays = input("Do you want to add more days (Y/N): ")
      if addMoreDays.upper() == "N":
        break
      else:
        self.dayNum += 1

    print("In total you worked "+str(round(self.totalHours, 2))+" hours in "+str(self.dayNum)+" days")
    print("The average hours per day was about "+str(round((self.totalHours / self.dayNum), 0))+" hours")
    hoursDifference, minutesDifference, overtime = self.calculateOvertimeUndertime(hoursPerDay)

    if not overtime:
      keyword = "undertime"
    else:
      keyword = "overtime"

    print("Currently, you have done "+str(hoursDifference)+" hours and "+str(minutesDifference)+" minutes",keyword)


class UploadApp():
  def __init__(self):
    self.dayNum = 0
    self.totalHours = 0
   
  #Below is the method that takes the times entered as integers and converts them to actual datetime objects 
  def convertTimes(self, startTime, endTime, lunchStart, lunchEnd):
    newST = datetime.strptime(startTime, "%H:%M")
    newET = datetime.strptime(endTime, "%H:%M")
    newLS = datetime.strptime(lunchStart, "%H:%M")
    newLE = datetime.strptime(lunchEnd, "%H:%M")
    return newST, newET, newLS, newLE
  
  #Below is the method that takes the converted times and works out the time difference in hours
  def calculateHours(self, convertedST, convertedET, convertedLS, convertedLE):
    dayDifference = convertedET - convertedST
    breakTime = convertedLE - convertedLS
    dayHours = dayDifference.total_seconds() / 3600
    breakHours = breakTime.total_seconds() / 3600
    hours = dayHours - breakHours
    return hours
  
  #Below is the method that outputs the hours
  def outputHours(self, hours):
    print("In total you worked "+str(round(self.totalHours, 2))+" hours in "+str(self.dayNum)+" days")
    print("The average hours per day was about "+str(round((self.totalHours / self.dayNum), 0))+" hours")
    altOutput = input("Do you wish to view the hours in hours and minutes format (Y/N)? ")
    altTotalHours = self.totalHours // 1
    altTotalMinutes = round((self.totalHours - altTotalHours) * 60, 0)
    print(altOutput.upper())
    if altOutput.upper() == "Y":
      print("In total you have worked:")
      print(str(altTotalHours)+" hours and "+str(altTotalMinutes)+" minutes")

  #Below is the function that checks the total hours against how many hours the worker should be doing
  def calculateOvertimeUndertime(self, hoursPerDay):
    overtime = True
    hours = self.totalHours - (hoursPerDay * self.dayNum)
    absoluteHours = abs(hours)
    justHours = absoluteHours // 1
    justMinutes = round((absoluteHours - justHours) * 60)
    if hours < 0:
      overtime = False
    return justHours, justMinutes, overtime
  
  def extractHoursFromFile(self, fileName):
    hoursArray = []
    with open(fileName, 'r') as f:
      print("The contents of the work hours file is as follows:")
      for line in f.readlines():
        print(line)
        hoursArray.append(line)
    return hoursArray
  
  #Core functionality, taking file inputs and calling functions
  def getUpload(self):
    print("You have chosen to use the file upload method")
    contractedHours = int(input("First enter how many hours you should be working: "))
    print("Is this either in:")
    print("1. Hours per day")
    print("2. Hours per week")
    perDayOrPerWeek = int(input("Enter either 1 or 2: "))
    hoursPerDay = 0
    if perDayOrPerWeek == 1:
      hoursPerDay = contractedHours
    elif perDayOrPerWeek == 2:
      hoursPerDay = contractedHours / 5
    print("Please note that the file has to be a plaintext file (.txt)")
    filePath = input("What is the path of your work hours file? ").strip('"')
    hoursArray = self.extractHoursFromFile(filePath)
    for line in hoursArray:
      times = line.strip()
      startTime = times[times.find("Start")+6:times.find(",")]
      endTime = times[times.find("End")+4:times.find("Lunch")-2]
      lunchStart = times[times.find("Lunch")+6:times.find("-")]
      lunchEnd = times[times.find("-")+1:]
      convertedST, convertedET, convertedLS, convertedLE = self.convertTimes(startTime, endTime, lunchStart, lunchEnd)
      hours = self.calculateHours(convertedST, convertedET, convertedLS, convertedLE)
      self.totalHours += hours
      self.dayNum += 1
    self.outputHours(hours)
    hoursDifference, minutesDifference, overtime = self.calculateOvertimeUndertime(hoursPerDay)

    if not overtime:
      keyword = "undertime"
    else:
      keyword = "overtime"

    print("Currently, you have done "+str(hoursDifference)+" hours and "+str(minutesDifference)+" minutes",keyword)


#Basic app structure
class App(Tk):
    def __init__(self):
        # Call super constructor
        super().__init__()

        # Set basic attributes inc Window title, size, etc.
        self.title("Work Hours Calculator")
         # Create a list to keep track of the widgets for each day
        self.day_widgets = {}
        self.daysVisible = [True, False]
        self.geometry("1200x600")  # Increase window size for better layout

        # Create a top frame and place it using grid
        empty_label = Label(self, text="                  ")
        empty_label1 = Label(self, text=" ")
        self.output_box = Text(self, state="disabled", height=5, width=100)
        empty_label.grid(row=2, column=0, columnspan=2)
        frame_top = Frame(self, width=1050, height=300)
        frame_top.grid(row=2, column=2, columnspan=5, sticky="nsew")

        # Configure the root window's grid to allow the frame to expand
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(7, weight=1)

        # Create a ScrolledFrame widget and place it using grid
        sf = ScrolledFrame(frame_top, width=1050, height=300)
        sf.grid(row=0, column=2, columnspan=5, sticky="nsew")

        # Configure the frame_top's grid to allow the ScrolledFrame to expand
        frame_top.grid_rowconfigure(0, weight=1)
        frame_top.grid_columnconfigure(0, weight=1)

        # Bind the arrow keys and scroll wheel
        sf.bind_arrow_keys(frame_top)
        sf.bind_scroll_wheel(frame_top)

        # Create a frame inside the ScrolledFrame to hold the content
        self.scrollable_frame = sf.display_widget(Frame, fit_width=True)

        # Frame for day 1
        frame_day1 = Frame(self.scrollable_frame, width=1000, height=100)
        frame_day1.grid(row=0, column=0, columnspan=9, padx=10, pady=10, sticky="nsew")
        frame_day1.rowconfigure([0, 1], minsize=10, weight=1)

        # Grid configuration
        for i in range(10):
            frame_day1.columnconfigure(i, weight=1)

        # Create labels, entry widgets, and buttons
        self.title_label = Label(self, text="Work Hours Calculator")
        self.contracted_hours_label = Label(self, text="Enter contracted hours:")
        self.contracted_hours_entry = Entry(self)
        # Create a Combobox with the options "Per week" and "Per day"
        options = ["Per week", "Per day"]
        self.contracted_hours_dropdown = ttk.Combobox(self, values=options)
        self.title_label.config(font = ("Courier New", 18, "bold"))
        
        # Create a String Var for the text variable of each basic input field
        starting_time = StringVar()
        starting_time.trace_add("write", lambda *args: self.limit_length(starting_time))
        ending_time = StringVar()
        ending_time.trace_add("write", lambda *args: self.limit_length(ending_time))
        lunch_starting_time = StringVar()
        lunch_starting_time.trace_add("write", lambda *args: self.limit_length(lunch_starting_time))
        lunch_ending_time = StringVar()
        lunch_ending_time.trace_add("write", lambda *args: self.limit_length(lunch_ending_time))

        # Day 1 section
        self.day1_label = Label(frame_day1, text="Day 1:")
        self.start_time_label1 = Label(frame_day1, text="Start Time:")
        self.start_time_entry1 = Entry(frame_day1, textvariable=starting_time)
        self.end_time_label1 = Label(frame_day1, text="End Time:")
        self.end_time_entry1 = Entry(frame_day1, textvariable=ending_time)
        self.lunch_start_label1 = Label(frame_day1, text="Lunch Start:")
        self.lunch_start_entry1 = Entry(frame_day1, textvariable=lunch_starting_time)
        self.lunch_end_label1 = Label(frame_day1, text="Lunch End:")
        self.lunch_end_entry1 = Entry(frame_day1, textvariable=lunch_ending_time)
        self.day1_button = Button(frame_day1, text="Add/Remove Day", command=lambda: self.add_remove_day(1))

        self.add_placeholder(self.start_time_entry1, "08:30")
        ToolTip(self.start_time_entry1, "Enter a start time for your work hours calculation. 24 hour format (HH:MM)")
        self.add_placeholder(self.end_time_entry1, "08:30")
        ToolTip(self.end_time_entry1, "Enter an end time for your work hours calculation. 24 hour format (HH:MM)")
        self.add_placeholder(self.lunch_start_entry1, "08:30")
        ToolTip(self.lunch_start_entry1, "Enter a lunch start time for your work hours calculation. 24 hour format (HH:MM)")
        self.add_placeholder(self.lunch_end_entry1, "08:30")
        ToolTip(self.lunch_end_entry1, "Enter a lunch end time for your work hours calculation. 24 hour format (HH:MM)")
        self.add_placeholder(self.contracted_hours_entry, "35")
        ToolTip(self.contracted_hours_entry, "Enter a number for your contracted work hours, either hours per day or per week")

        self.calculate_button = Button(self, text="Calculate", command=self.calculate_hours)
        self.clear_button = Button(self, text="Clear", command=self.clear_fields)

        # Arrange widgets using grid as per intended design
        self.title_label.grid(row=0, column=0, columnspan=10, pady=10)
        self.contracted_hours_label.grid(row=1, column=3, pady=10)
        self.contracted_hours_entry.grid(row=1, column=4, pady=10)
        self.contracted_hours_dropdown.grid(row=1, column=5, pady=10)
        empty_label1.grid(row=2, column=6)
        self.output_box.grid(row=3, column=1, columnspan=7, pady=20)
        self.calculate_button.grid(row=4, column=3, sticky="s")
        self.clear_button.grid(row=4, column=5, sticky="s")

        self.day1_label.grid(row=0, column=0, columnspan=10, sticky="w")
        self.start_time_label1.grid(row=1, column=0, sticky="w")
        
        self.start_time_entry1.grid(row=1, column=1, padx=18)
        self.end_time_label1.grid(row=1, column=2, sticky="w")
        self.end_time_entry1.grid(row=1, column=3, padx=18)
        self.lunch_start_label1.grid(row=1, column=4, sticky="w")
        self.lunch_start_entry1.grid(row=1, column=5, padx=18)
        self.lunch_end_label1.grid(row=1, column=6, sticky="w")
        self.lunch_end_entry1.grid(row=1, column=7, padx=18)
        self.day1_button.grid(row=1, column=8, columnspan=2, pady=10)

    # Function to limit entry length to 5 characters
    def limit_length(self, entry_text):
        if len(entry_text.get()) > 5:
            entry_text.set(entry_text.get()[:5])

    # Placeholder handling
    def add_placeholder(self, entry, placeholder):
        entry.insert(0, placeholder)
        entry.config(fg='grey')  # Set placeholder color to grey
        entry.bind("<FocusIn>", lambda e: self.clear_placeholder(e, placeholder))
        entry.bind("<FocusOut>", lambda e: self.restore_placeholder(e, placeholder))

    def clear_placeholder(self, event, placeholder):
        if event.widget.get() == placeholder:
            event.widget.delete(0, END)
            event.widget.config(fg='black')  # Set text color back to black when typing

    def restore_placeholder(self, event, placeholder):
        if event.widget.get() == "":
            event.widget.insert(0, placeholder)
            event.widget.config(fg='grey')  # Set color back to grey when placeholder is restored

    def calculate_hours(self):
        self.output_box.configure(state="normal")
        day1_start_time = self.start_time_entry1.get()
        day1_end_time = self.end_time_entry1.get()
        day1_lunch_start = self.lunch_start_entry1.get()
        day1_lunch_end = self.lunch_end_entry1.get()
        total_hours = 0
        hours = self.calculate_hours2(day1_start_time, day1_end_time, day1_lunch_start, day1_lunch_end)
        total_hours += hours
        for num in range(0, len(self.day_widgets)):
          widgets = self.day_widgets.get(num+1)
          if widgets and self.daysVisible[num+1]:
            day_start_time = widgets["start_time_entry"].get()
            day_end_time = widgets["end_time_entry"].get()
            day_lunch_start = widgets["lunch_start_entry"].get()
            day_lunch_end = widgets["lunch_end_entry"].get()
            hours = self.calculate_hours2(day_start_time, day_end_time, day_lunch_start, day_lunch_end)
            total_hours += hours
        total_whole_hours = int(total_hours // 1)
        total_minutes = int((total_hours % 1)*60)
        total_days = sum(self.daysVisible)
        average_per_day = round(total_hours / total_days)
        self.output_box.delete("1.0", END)
        contracted_timeframe = self.contracted_hours_dropdown.get()
        if contracted_timeframe == "Per week":
           contracted_hours = int(self.contracted_hours_entry.get()) // 5
        else:
           contracted_hours = int(self.contracted_hours_entry.get())
        overtime_hours, overtime_mins, is_overtime = self.calculate_overtime(total_days, contracted_hours, total_hours)
        if not is_overtime:
          keyword = "undertime"
        else:
          keyword = "overtime"

        overtime_string = f"Currently, you have done {overtime_hours} hour(s) and {overtime_mins} minutes {keyword}\n"
        contracted_hours_string = f"You should be working {contracted_hours} hour(s) per day as per your contract\n"
        total_hours_string = f"In total you have worked {total_hours} hour(s) or {total_whole_hours} hour(s) and {total_minutes} minutes\n"
        days_and_average_string = f"You've worked for a total of {total_days} day(s) and you've done {average_per_day} hour(s) per day on average\n"

        self.output_box.insert("1.0", total_hours_string)
        self.output_box.insert(END, contracted_hours_string)
        self.output_box.insert(END, days_and_average_string)
        self.output_box.insert(END, overtime_string)
        self.output_box.configure(state="disabled")

    def calculate_hours2(self, startTime, endTime, lunchStart, lunchEnd):
      convertedST = datetime.strptime(startTime, "%H:%M")
      convertedET = datetime.strptime(endTime, "%H:%M")
      convertedLS = datetime.strptime(lunchStart, "%H:%M")
      convertedLE = datetime.strptime(lunchEnd, "%H:%M")
      dayDifference = convertedET - convertedST
      breakTime = convertedLE - convertedLS
      dayHours = dayDifference.total_seconds() / 3600
      breakHours = breakTime.total_seconds() / 3600
      hours = dayHours - breakHours
      return hours
    
    def calculate_overtime(self, days, contracted, total):
      overtime = True
      hours = total - (contracted * days)
      absoluteHours = abs(hours)
      justHours = int(absoluteHours // 1)
      justMinutes = int((absoluteHours % 1)*60)
      if hours < 0:
        overtime = False
      return justHours, justMinutes, overtime

    def clear_fields(self):
        # Hide the widgets by removing them from the grid
        self.start_time_entry1.delete(0, END)
        self.end_time_entry1.delete(0, END)
        self.lunch_start_entry1.delete(0, END)
        self.lunch_end_entry1.delete(0, END)
        self.contracted_hours_entry.delete(0, END)
        for num in range(0, len(self.day_widgets)):
          widgets = self.day_widgets.get(num+1)
          if widgets:
            for widget in widgets.values():
              try:
                 widget.delete(0, END)
              except:
                 pass
        self.output_box.configure(state="normal")
        self.output_box.delete("1.0", END)
        self.output_box.configure(state="disabled")

    def add_remove_day(self, day_num):
        # Use exception handling to make sure array out of bounds error doesn't happen
        try:
            # Toggle visibility
            self.daysVisible[day_num] = not self.daysVisible[day_num]
        except IndexError:
            self.daysVisible.append(True)

        # Setup the day string
        dayString = "Day " + str(day_num + 1) + ":"

        if self.daysVisible[day_num]:

            # Create widgets if not already created
            if day_num not in self.day_widgets:
                day_frame = Frame(self.scrollable_frame, width=1000, height=150)
                day_frame.rowconfigure([0, 1], minsize=10, weight=1)
                day_frame.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], minsize=10, weight=1)

                # Create a String Var for the text variable of each basic input field
                starting_time = StringVar()
                starting_time.trace_add("write", lambda *args: self.limit_length(starting_time))
                ending_time = StringVar()
                ending_time.trace_add("write", lambda *args: self.limit_length(ending_time))
                lunch_starting_time = StringVar()
                lunch_starting_time.trace_add("write", lambda *args: self.limit_length(lunch_starting_time))
                lunch_ending_time = StringVar()
                lunch_ending_time.trace_add("write", lambda *args: self.limit_length(lunch_ending_time))

                day_label = Label(day_frame, text=dayString)
                start_time_label = Label(day_frame, text="Start Time:")
                start_time_entry = Entry(day_frame, textvariable=starting_time)
                end_time_label = Label(day_frame, text="End Time:")
                end_time_entry = Entry(day_frame, textvariable=ending_time)
                lunch_start_label = Label(day_frame, text="Lunch Start:")
                lunch_start_entry = Entry(day_frame, textvariable=lunch_starting_time)
                lunch_end_label = Label(day_frame, text="Lunch End:")
                lunch_end_entry = Entry(day_frame, textvariable=lunch_ending_time)
                day_button = Button(day_frame, text="Add/Remove Day", command=lambda: self.add_remove_day(day_num+1))

                self.add_placeholder(start_time_entry, "08:30")
                ToolTip(start_time_entry, "Enter a start time for your work hours calculation. 24 hour format (HH:MM)")
                self.add_placeholder(end_time_entry, "08:30")
                ToolTip(end_time_entry, "Enter an end time for your work hours calculation. 24 hour format (HH:MM)")
                self.add_placeholder(lunch_start_entry, "08:30")
                ToolTip(lunch_start_entry, "Enter a lunch start time for your work hours calculation. 24 hour format (HH:MM)")
                self.add_placeholder(lunch_end_entry, "08:30")
                ToolTip(lunch_end_entry, "Enter a lunch end time for your work hours calculation. 24 hour format (HH:MM)")

                # Store widgets in a dictionary for each day
                self.day_widgets[day_num] = {
                    "frame": day_frame,
                    "day_label": day_label,
                    "start_time_label": start_time_label,
                    "start_time_entry": start_time_entry,
                    "end_time_label": end_time_label,
                    "end_time_entry": end_time_entry,
                    "lunch_start_label": lunch_start_label,
                    "lunch_start_entry": lunch_start_entry,
                    "lunch_end_label": lunch_end_label,
                    "lunch_end_entry": lunch_end_entry,
                    "day_button": day_button
                }

            # Retrieve the widgets
            widgets = self.day_widgets[day_num]
            day_frame = widgets["frame"]

            # Display the widgets
            day_frame.grid(row=day_num + 2, column=0, columnspan=10)
            widgets["day_label"].grid(row=2, column=0, columnspan=10, sticky="w")
            widgets["start_time_label"].grid(row=3, column=0, sticky="w")
            widgets["start_time_entry"].grid(row=3, column=1, padx=18)
            widgets["end_time_label"].grid(row=3, column=2, sticky="w")
            widgets["end_time_entry"].grid(row=3, column=3, padx=18)
            widgets["lunch_start_label"].grid(row=3, column=4, sticky="w")
            widgets["lunch_start_entry"].grid(row=3, column=5, padx=18)
            widgets["lunch_end_label"].grid(row=3, column=6, sticky="w")
            widgets["lunch_end_entry"].grid(row=3, column=7, padx=18)
            widgets["day_button"].grid(row=3, column=8, columnspan=2, pady=10)
        else:
            # Hide the widgets by removing them from the grid
            widgets = self.day_widgets.get(day_num)
            if widgets:
                widgets["frame"].grid_forget()
                for widget in widgets.values():
                    widget.grid_forget()

        
if __name__ == "__main__":
    print("Welcome to the Akhtar Hasan work hours calculator!")
    print("""Please choose one of the following options below for insertion format:
            1. Basic app
            2. Advanced app (GUI version)
            3. Upload text file
          Please indicate with your choice below""")
    choice = int(input("Enter a number (1,2 or 3) for your choice: "))
    if choice == 1:
       basicApp = BasicApp()
       basicApp.takeInputs()
    elif choice == 2:
       app = App()
       app.mainloop()
    elif choice == 3:
       uploadApp = UploadApp()
       uploadApp.getUpload()

