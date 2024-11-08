#Maths quiz game
from tkinter import *
from random import *

#the 'get_questions' function which imports the questions from a file and returns them as a 2D array
def get_questions():
    questions = [] #initialises the variable 'questions' as an empty array
    file = open("maths_qs.txt", "r") #opens the file title 'maths_qs.txt'
    for line in file: #runs a FOR loop through each line of the file
        newLine = line.strip("\n").split(",") #creates the array which will be appended to 'questions'
        questions.append(newLine) #appends the array stored in 'newLine' to 'questions'
    return questions #returns the 'questions' 2D array to the app class

#Class for the tertiary Tkinter window called 'Results'
class Results(Toplevel):
    def __init__(self, parent, score):
        super().__init__(parent) #uses the super constructor for the parent window

        #set the window attributes up
        self.geometry('410x200')
        self.title('Results')
        self.configure(bg="#12AAE6")

        #set the main text label up and arrange using the grid method in row 0
        label1 = Label(self, text="The results are in", bg="#12AAE6")
        label1.config(font=('Helvetica bold',40))
        label1.grid(row=0,columnspan=2)

        #set up the text which will be used in the secondary text label
        thisText = f"You scored: {score} / 10"

        #set the secondary text label up and arrange using the grid method in row 0
        label2 = Label(self, text=thisText, bg="#12AAE6")
        label2.config(font=('Helvetica bold',25))
        label2.grid(row=1, columnspan=2)

#Class for the secondary Tkinter window called 'Window'
class Window(Tk):
    def __init__(self, calls, questions, score):
        super().__init__() #uses the super construcor for 'Tk'

        #set the window attributes up
        self.geometry('2000x500')
        self.title('Questions')
        self.configure(bg="#12AAE6")

        #set the question up for the main label
        self.question = questions[0]
        thisQuestion = self.question[0]

        #set the multi-choice answers for the buttons
        answer1 = self.question[1]
        answer2 = self.question[2]
        answer3 = self.question[3]
        answer4 = self.question[4]

        #set the correcAnswer and textvariable for the score box
        correctAnswer = answer1
        self.Score = StringVar()

        #set a variable which will be returned to the 'Main' program
        self.movesLeft = 0
        self.currentScore = score

        #set the question text label up
        label1 = Label(self, text=thisQuestion, bg="#12AAE6")
        label1.config(font=('Helvetica bold',20))
        label1.grid(row=0,columnspan=2) #arrange using the grid method in row 0

        #set up the buttons for the answer choices
        number1 = Button(self, text=answer1, bg="#12AAE6", command=lambda: self.ansPressed(answer1, correctAnswer))
        number1.grid(row=1, column=0) #arrange using the grid method in row 1, col 0
        number2 = Button(self, text=answer2, bg="#12AAE6", command=lambda: self.ansPressed(answer2, correctAnswer))
        number2.grid(row=1, column=1) #arrange using the grid method in row 1, col 1
        number3 = Button(self, text=answer3, bg="#12AAE6", command=lambda: self.ansPressed(answer3, correctAnswer))
        number3.grid(row=2, column=0) #arrange using the grid method in row 2, col 0 
        number4 = Button(self, text=answer4, bg="#12AAE6", command=lambda: self.ansPressed(answer4, correctAnswer))
        number4.grid(row=2, column=1) #arrange using the grid method in row 2, col 1

        #set the score box as a disabled entry that only the program can update
        self.scoreBox = Entry(self, bg="#12AAE6", textvariable=self.Score)
        self.scoreBox.config(state= "disabled")
        self.scoreBox.grid(row=3, column=1) #arrange this using grid method in row 3, col 1

        #set the score text label up
        label2 = Label(self, text="Score:", bg="#12AAE6")
        label2.config(font=('Helvetica bold',10))
        label2.grid(row=3, column=0) #arrange using the grid method in row 3, col 0

        #set up a button which closes the window
        Button(self,text='Close',bg="#12AAE6",command=self.destroy).grid(row=4, column=1)

    def ansPressed(self, answer, correctAnswer):
        if answer == correctAnswer: #check if the answer the user chose is correct
            print("Correct!") #if it is, print 'Correct!'
            self.currentScore += 1 #increment the score by 1
            self.movesLeft = 5
        else: #otherwise
            print("Incorrect!") #print 'Incorrect!'
            self.currentScore -= 1  #decrement the score by 1
            self.movesLeft = 1
        self.Score.set(str(self.currentScore)) #set the 'Score' text variable to be the attribute 'currentScore'

    def open_window(self, score, questions):
        global calls #make calls a global variable
        questions.remove(self.question) #remove the previous question from the questions array
        calls += 1 #increment calls by 1
        self.destroy() #close the previous window
        if calls < 10: #check if calls is less than 10
            window = Window(app, calls, questions) #if it is, calls itself for next question
            window.grab_set() #allows events to happen within the window object
        else: #otherwise
            results = Results(app, score) #calls the results window
            results.grab_set() #allows events to happen within the results object

    def return_info(self):
        return self.currentScore, self.movesLeft

#Class for the main Tkinter window called 'App'
class App(Tk):
    def __init__(self, score, calls): #the constructor method with 2 arguments
        super().__init__()
        
        #set the window attributes up
        self.geometry('825x500')
        self.title('Maths Maze Navigator')
        self.configure(bg="#12AAE6")

        #set the main text label up and arrange using the grid method in row 0
        label1 = Label(self, text="Welcome to Maths Maze Navigator", bg="#12AAE6")
        label1.config(font=('Helvetica bold',40))
        label1.grid(row=0,columnspan=2)

        #set up a button which opens the new window for the questions
        Button(self,text='Open questions',bg="#12AAE6",command=self.open_window).grid(row=1, column=0)
        #set up a button which closes the window
        Button(self,text='Close',bg="#12AAE6",command=self.destroy).grid(row=1, column=1)

    #set up a method to open the questions window
    def open_window(self):
        calls = 0 #initialises the variable 'calls' as 0
        questions = get_questions() #calls the 'get_questions' function and stores the result
        window = Window(self, calls, questions) #creates the window object from the class definition
        window.grab_set() #allow events to happen within the window object

#constantly runs unless there is an error
if __name__ == "__main__":
    score = 0 #initialises the variable 'score' as 0
    calls = 0 #initialises the variable 'calls' as 0
    app = App(score, calls) #creates the app object from the class definition
    app.mainloop() #allow events to happen within the app object
