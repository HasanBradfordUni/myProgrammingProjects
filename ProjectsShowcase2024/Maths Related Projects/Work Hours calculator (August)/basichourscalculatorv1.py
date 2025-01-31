# -*- coding: utf-8 -*-
"""BasicHoursCalculatorV1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13wA01zVaI_umyCzR-nM05uYN1BNccmZp

# Basic Hours calculator

## A calculator that calulates the amount of hours you have worked for however many working days you want based on the inputs of:
 *   ### Start time
 *   ### End time
 *   ### Lunch start time
 *   ### Lunch end time

Essentialy it calculates the difference between the end time and start time on each day and subtracts the difference between the lunch start time and end time
It does this for each day is input and add the totals of the hours for a cumalutive total of hours worked across the days. It can also tell the average hours per day and if you input how many hours you should be working per day/week, the overtime/undertime based on those hours. In a future extension, the pay may be added as well so you can see how much pay you should be receiving for those hours based on either the pay per hour, day, week, month or year.

This is version 1 which is just purely based on the console, command-line interface and is just for testing the basic functionalities of the application before extra functionalities can be added and it can be adapted to host a graphical user interface.

> Basic imports first
"""

from datetime import datetime

"""> Core functionality, taking inputs and calling functions"""

dayNum = 1
totalHours = 0
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
  print("Day "+str(dayNum)+" :")
  startTime = input("Enter start time in 24 hour format (HH.MM): ")
  endTime = input("Enter end time in 24 hour format (HH.MM): ")
  lunchStart = input("Enter start time for lunch in 24 hour format (HH.MM): ")
  lunchEnd = input("Enter end time for lunch in 24 hour format (HH.MM): ")
  convertedST, convertedET, convertedLS, convertedLE = convertTimes(startTime, endTime, lunchStart, lunchEnd)
  hours = calculateHours(convertedST, convertedET, convertedLS, convertedLE)
  totalHours += hours
  outputHours(dayNum, hours, totalHours)
  addMoreDays = input("Do you want to add more days (Y/N): ")
  if addMoreDays.upper() == "N":
    break
  else:
    dayNum += 1

print("In total you worked "+str(round(totalHours, 2))+" hours in "+str(dayNum)+" days")
print("The average hours per day was about "+str(round((totalHours / dayNum), 0))+" hours")
hoursDifference, minutesDifference, overtime = calculateOvertimeUndertime(totalHours, dayNum, hoursPerDay)

if not overtime:
  keyword = "undertime"
else:
  keyword = "overtime"

print("Currently, you have done "+str(hoursDifference)+" hours and "+str(minutesDifference)+" minutes",keyword)

"""> Below is the function that takes the times entered as integers and converts them to actual datetime objects"""

def convertTimes(startTime, endTime, lunchStart, lunchEnd):
  newST = datetime.strptime(startTime, "%H.%M")
  newET = datetime.strptime(endTime, "%H.%M")
  newLS = datetime.strptime(lunchStart, "%H.%M")
  newLE = datetime.strptime(lunchEnd, "%H.%M")
  return newST, newET, newLS, newLE

"""> Below is the function that takes the converted times and works out the time difference in hours"""

def calculateHours(convertedST, convertedET, convertedLS, convertedLE):
  dayDifference = convertedET - convertedST
  breakTime = convertedLE - convertedLS
  dayHours = dayDifference.total_seconds() / 3600
  breakHours = breakTime.total_seconds() / 3600
  hours = dayHours - breakHours
  return hours

"""> Below is the function that outputs the hours"""

def outputHours(dayNum, hours, totalHours):
  print("The hours worked on Day "+str(dayNum)+" (in decimal format):")
  print(round(hours, 2))
  print("The total hours you have worked (so far) is:")
  print(totalHours)
  altOutput = input("Do you wish to view the hours in hours and minutes format (Y/N)? ")
  altHours = hours // 1
  altMinutes = round((hours - altHours) * 60, 0)
  altTotalHours = totalHours // 1
  altTotalMinutes = round((totalHours - altTotalHours) * 60, 0)
  print(altOutput.upper())
  if altOutput.upper() == "Y":
    print("The hours worked on Day "+str(dayNum)+" (in hours and minutes format):")
    print(str(altHours)+" hours and "+str(altMinutes)+" minutes")
    print("The total hours you have worked (so far) is:")
    print(str(altTotalHours)+" hours and "+str(altTotalMinutes)+" minutes")

"""> Tests devised to test the various functions"""

# Example usage:
startTime = "08.30"
endTime = "17.45"
lunchStart = "12.30"
lunchEnd = "13.30"
dayNum = 1
totalHours = 0

convertedST, convertedET, convertedLS, convertedLE = convertTimes(startTime, endTime, lunchStart, lunchEnd)
print(convertedST, convertedET, convertedLS, convertedLE)
hours = calculateHours(convertedST, convertedET, convertedLS, convertedLE)
print(hours)
totalHours += hours
outputHours(dayNum, hours, totalHours)

"""> Below is the function that checks the total hours against how many hours the worker should be doing"""

def calculateOvertimeUndertime(totalHours, dayNum, hoursPerDay):
  overtime = True
  hours = totalHours - (hoursPerDay * dayNum)
  absoluteHours = abs(hours)
  justHours = absoluteHours // 1
  justMinutes = round((absoluteHours - justHours) * 60, 0)
  if hours < 0:
    overtime = False
  return justHours, justMinutes, overtime