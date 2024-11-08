#Maths quiz game
from tkinter import *
from random import *

def get_questions():
    questions = []
    file = open("maths_qs.txt", "r")
    for line in file:
        newLine = line.strip("\n").split(",")
        questions.append(newLine)
    return questions

class Results(Toplevel):
    def __init__(self, parent, score):
        super().__init__(parent)

        self.geometry('410x200')
        self.title('Results')
        self.configure(bg="#12AAE6")

        label1 = Label(self, text="The results are in", bg="#12AAE6")
        label1.config(font=('Helvetica bold',40))
        label1.grid(row=0,columnspan=2)

        thisText = f"You scored: {score} / 10"

        label2 = Label(self, text=thisText, bg="#12AAE6")
        label2.config(font=('Helvetica bold',25))
        label2.grid(row=1, columnspan=2)

class Window(Toplevel):
    def __init__(self, parent, calls, questions):
        super().__init__(parent)

        self.geometry('2000x500')
        self.title('Questions')
        self.configure(bg="#12AAE6")

        self.question = questions[0]
        thisQuestion = self.question[0]

        answer1 = self.question[1]
        answer2 = self.question[2]
        answer3 = self.question[3]
        answer4 = self.question[4]

        correctAnswer = answer1
        self.Score = StringVar()

        label1 = Label(self, text=thisQuestion, bg="#12AAE6")
        label1.config(font=('Helvetica bold',20))
        label1.grid(row=0,columnspan=2)

        number1 = Button(self, text=answer1, bg="#12AAE6", command=lambda: self.ansPressed(answer1, correctAnswer))
        number1.grid(row=1, column=0)
        number2 = Button(self, text=answer2, bg="#12AAE6", command=lambda: self.ansPressed(answer2, correctAnswer))
        number2.grid(row=1, column=1)
        number3 = Button(self, text=answer3, bg="#12AAE6", command=lambda: self.ansPressed(answer3, correctAnswer))
        number3.grid(row=2, column=0)
        number4 = Button(self, text=answer4, bg="#12AAE6", command=lambda: self.ansPressed(answer4, correctAnswer))
        number4.grid(row=2, column=1)

        self.scoreBox = Entry(self, bg="#12AAE6", textvariable=self.Score)
        self.scoreBox.config(state= "disabled")
        self.scoreBox.grid(row=3, column=1)

        label2 = Label(self, text="Score:", bg="#12AAE6")
        label2.config(font=('Helvetica bold',10))
        label2.grid(row=3, column=0)
        
        Button(self,text="Next Question",bg="#12AAE6",command=lambda: self.open_window(score, questions)).grid(row=4, column=0)
        Button(self,text='Close',bg="#12AAE6",command=self.destroy).grid(row=4, column=1)

    def ansPressed(self, answer, correctAnswer):
        global score
        if answer == correctAnswer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            score -= 1
        self.Score.set(str(score))

    def open_window(self, score, questions):
        global calls
        questions.remove(self.question)
        calls += 1
        self.destroy()
        if calls < 10:
            window = Window(app, calls, questions)
            window.grab_set()
        else:
            results = Results(app, score)
            results.grab_set()

class App(Tk):
    def __init__(self, score, calls):
        super().__init__()

        self.geometry('825x500')
        self.title('Maths Maze Navigator')
        self.configure(bg="#12AAE6")

        label1 = Label(self, text="Welcome to Maths Maze Navigator", bg="#12AAE6")
        label1.config(font=('Helvetica bold',40))
        label1.grid(row=0,columnspan=2)
        
        Button(self,text='Open questions',bg="#12AAE6",command=self.open_window).grid(row=1, column=0)
        Button(self,text='Close',bg="#12AAE6",command=self.destroy).grid(row=1, column=1)

    def open_window(self):
        calls = 0
        questions = get_questions()
        window = Window(self, calls, questions)
        window.grab_set()


if __name__ == "__main__":
    score = 0
    calls = 0
    app = App(score, calls)
    app.mainloop()
