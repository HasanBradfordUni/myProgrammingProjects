from tkinter import *

class Results(Toplevel):
    def __init__(self, parent, Answers, answer1, answer2, answer3, answer4, answer5):
        super().__init__(parent)

        self.geometry('300x500')
        self.title('Your results')

        def check_results(Answers):
            answersCorrect = 0
            text = "Answers correct: "
            if Answers[0] == answer1:
                answersCorrect += 1
            if Answers[1] == answer2:
                answersCorrect += 1
            if Answers[2] == answer3:
                answersCorrect += 1
            if Answers[3] == answer4:
                answersCorrect += 1
            if Answers[4] == answer5:
                answersCorrect += 1
            textBox.delete(0.0, END)
            textBox.insert(END, text+str(answersCorrect))

        Label(self,text="The results are in...").grid(row=0,columnspan=2)
        textBox = Text(self)
        textBox.grid(row=1, columnspan=2)

        Button(self,text='Reveal',command=lambda: check_results(Answers)).grid(row=2, column=0)
        Button(self,text='Close',command=self.destroy).grid(row=2, column=1)

class Window(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x500')
        self.title('Fill out Computer Science Quiz')

        Label(self,text="Computer Science Quiz").grid(row=0,columnspan=2)

        Answer1 = StringVar()
        Answer2 = StringVar()
        Answer3 = StringVar()
        Answer4 = StringVar()
        Answer5 = StringVar()

        def open_results():
            answer1 = Answer1.get()
            answer2 = Answer2.get()
            answer3 = Answer3.get()
            answer4 = Answer4.get()
            answer5 = Answer5.get()
            window1 = Results(self, Answers, answer1, answer2, answer3, answer4, answer5)
            window1.grab_set()

        Label(self,text="Which of these is NOT software?").grid(row=1, column=0)
        q1_option1 = Radiobutton(self, text="Linux OS", variable=Answer1, value="Linux OS")
        q1_option1.grid(row=2,column=0,sticky="W")
        q1_option2 = Radiobutton(self, text="Python", variable=Answer1, value="Python")
        q1_option2.grid(row=3,column=0,sticky="W")
        q1_option3 = Radiobutton(self, text="Hard Drive", variable=Answer1, value="Hard Drive")
        q1_option3.grid(row=4,column=0,sticky="W")
        q1_option4 = Radiobutton(self, text="MS Word", variable=Answer1, value="MS Word")
        q1_option4.grid(row=5,column=0,sticky="W")

        Label(self,text="What are the 2 parts of a computer instruction?").grid(row=6, column=0)
        q2_option1 = Radiobutton(self, text="Op-code and operator", variable=Answer2, value="Op-code and operator")
        q2_option1.grid(row=7,column=0,sticky="W")
        q2_option2 = Radiobutton(self, text="Op-code and Opstate", variable=Answer2, value="Op-code and Opstate")
        q2_option2.grid(row=8,column=0,sticky="W")
        q2_option3 = Radiobutton(self, text="Opcode and Operand", variable=Answer2, value="Opcode and Operand")
        q2_option3.grid(row=9,column=0,sticky="W")
        q2_option4 = Radiobutton(self, text="Opcommand and Opmemory", variable=Answer2, value="Opcommand and Opmemory")
        q2_option4.grid(row=10,column=0,sticky="W")

        Label(self,text="What is a multitasking computer?").grid(row=11, column=0)
        q3_option1 = Radiobutton(self, text="Multiple users can be logged in at the same time", variable=Answer3, value="Multiple users can be logged in at the same time")
        q3_option1.grid(row=12,column=0,sticky="W")
        q3_option2 = Radiobutton(self, text="A CPU core that can run more than one process at a time", variable=Answer3, value="A CPU core that can run more than one process at a time")
        q3_option2.grid(row=13,column=0,sticky="W")
        q3_option3 = Radiobutton(self, text="Multiple programs can be running at the same time", variable=Answer3, value="Multiple programs can be running at the same time")
        q3_option3.grid(row=14,column=0,sticky="W")
        q3_option4 = Radiobutton(self, text="A computer that can handle multiple input devices", variable=Answer3, value="A computer that can handle multiple input devices")
        q3_option4.grid(row=15,column=0,sticky="W")

        Label(self,text="What type of code is Bytecode?").grid(row=16, column=0)
        q4_option1 = Radiobutton(self, text="Machine Code", variable=Answer4, value="Machine Code")
        q4_option1.grid(row=17,column=0,sticky="W")
        q4_option2 = Radiobutton(self, text="Assembly Language", variable=Answer4, value="Assembly Language")
        q4_option2.grid(row=18,column=0,sticky="W")
        q4_option3 = Radiobutton(self, text="Source Code", variable=Answer4, value="Source Code")
        q4_option3.grid(row=19,column=0,sticky="W")
        q4_option4 = Radiobutton(self, text="Intermediate Code", variable=Answer4, value="Intermediate Code")
        q4_option4.grid(row=20,column=0,sticky="W")

        Label(self,text="Which of these are real programming paradigms?").grid(row=21, column=0)
        q5_option1 = Radiobutton(self, text="OOP and procedural", variable=Answer5, value="OOP and procedural")
        q5_option1.grid(row=22,column=0,sticky="W")
        q5_option2 = Radiobutton(self, text="Real and Boolean", variable=Answer5, value="Real and Boolean")
        q5_option2.grid(row=23,column=0,sticky="W")
        q5_option3 = Radiobutton(self, text="Functional and OOP", variable=Answer5, value="Functional and OOP")
        q5_option3.grid(row=24,column=0,sticky="W")
        q5_option4 = Radiobutton(self, text="Sequence and procedural", variable=Answer5, value="Sequence and procedural")
        q5_option4.grid(row=25,column=0,sticky="W")

        Button(self,text='Submit',command=open_results).grid(row=26, column=0)
        Button(self,text='Close',command=self.destroy).grid(row=26, column=1)

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x200')
        self.title('Login in to Computer Science Quiz')

        label1 = Label(self, text="Login")
        label1.grid(row=0,columnspan=2)

        Label(self, text="Username:").grid(row=1, column=0)
        Label(self, text="Password:").grid(row=2, column=0)

        username = Entry(self)
        password = Entry(self)

        def open_questionaire():
            file = open("logins.txt", 'a')
            Username = username.get()
            Password = password.get()
            text = Username+","+Password+"\n"
            file.write(text)
            window = Window(self)
            window.grab_set()

        username.grid(row=1, column=1, sticky="W")
        password.grid(row=2, column=1, sticky="W")
        
        Button(self,text='Submit',command=open_questionaire).grid(row=3, column=0)
        Button(self,text='Exit',command=self.destroy).grid(row=3, column=1)

    

if __name__ == "__main__":
    Answers = ["Hard Drive","Opcode and Operand","Multiple programs can be running at the same time","Intermediate Code","OOP and procedural"]
    app = App()
    app.mainloop()
