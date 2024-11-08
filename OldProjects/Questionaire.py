from tkinter import *

def submit():
    hobbies = []
    name = Name.get()
    age = Age.get()
    gender = Gender.get()
    text0 = "The results are: \n"
    text1 = "Your name is: "+name+"\n"
    text2 = "Your age is: "+str(age)+"\n"
    text3 = "Your gender is: "+gender+"\n"
    if Hobby1.get() == 1:
        hobby = hobby1["text"]
        hobbies.append(hobby)
    if Hobby2.get() == 1:
        hobby = hobby2["text"]
        hobbies.append(hobby)
    if Hobby3.get() == 1:
        hobby = hobby3["text"]
        hobbies.append(hobby)
    if Hobby4.get() == 1:
        hobby = hobby4["text"]
        hobbies.append(hobby)
    if Hobby5.get() == 1:
        hobby = hobby5["text"]
        hobbies.append(hobby)
    if Hobby6.get() == 1:
        hobby = hobby6["text"]
        hobbies.append(hobby)
    if Hobby7.get() == 1:
        hobby = hobby7["text"]
        hobbies.append(hobby)
    if Hobby8.get() == 1:
        hobby = hobby8["text"]
        hobbies.append(hobby)
    if Hobby9.get() == 1:
        hobby = hobby9["text"]
        hobbies.append(hobby)
    if Hobby0.get() == 1:
        hobby = hobby0["text"]
        hobbies.append(hobby)
    text4 = "Your favourite hobbies are: \n"
    text5 = ""
    for num in range(0,len(hobbies)):
        text5 += hobbies[num]+", "
    textbox.delete(0.0, END)
    textbox.insert(END, text0)
    textbox.insert(END, text1)
    textbox.insert(END, text2)
    textbox.insert(END, text3)
    textbox.insert(END, text4)
    textbox.insert(END, text5)

window = Tk()
window.title("Questionaire")
window.configure(bg="Green")

menubar = Menu(window)

firstMenu = Menu(menubar, tearoff = 0)
firstMenu.add_command(label="Quit!", command=window.destroy)
menubar.add_cascade(label="Quit program", menu=firstMenu)

window.config(menu=menubar)

Age = IntVar()
Gender = StringVar()

Hobby1 = IntVar()
Hobby2 = IntVar()
Hobby3 = IntVar()
Hobby4 = IntVar()
Hobby5 = IntVar()
Hobby6 = IntVar()
Hobby7 = IntVar()
Hobby8 = IntVar()
Hobby9 = IntVar()
Hobby0 = IntVar()

label1 = Label(window, text = "A Short Questionaire for you to fill in", bg="green", fg="white")
label2 = Label(window, text = "Name:", bg="green", fg="white")
label3 = Label(window, text = "Age:", bg="green", fg="white")
label4 = Label(window, text = "Gender:", bg="green", fg="white")
label5 = Label(window, text = "Select your hobbies:", bg="green", fg="white")

Name = Entry(window, bg="green", fg="white")
spin_age = Spinbox(window, textvariable=Age, from_=1, to = 99, bg="green", fg="white")
gender1 = Radiobutton(window, text="Male", variable=Gender, value="Male", bg="green")
gender1.grid(row=4,column=0)
gender2 = Radiobutton(window, text="Female", variable=Gender, value="Female", bg="green")
gender2.grid(row=5,column=0)

hobby1 =  Checkbutton(window, text = "Chess", variable=Hobby1, bg="green")
hobby2 =  Checkbutton(window, text = "Swimming", variable=Hobby2, bg="green")
hobby3 =  Checkbutton(window, text = "Running", variable=Hobby3, bg="green")
hobby4 =  Checkbutton(window, text = "Walking", variable=Hobby4, bg="green")
hobby5 =  Checkbutton(window, text = "Playstation", variable=Hobby5, bg="green")
hobby6 =  Checkbutton(window, text = "Reading", variable=Hobby6, bg="green")
hobby7 =  Checkbutton(window, text = "Football", variable=Hobby7, bg="green")
hobby8 =  Checkbutton(window, text = "Tennis", variable=Hobby8, bg="green")
hobby9 =  Checkbutton(window, text = "Cricket", variable=Hobby9, bg="green")
hobby0 =  Checkbutton(window, text = "Other sports", variable=Hobby0, bg="green")

textbox = Text(window, width=20, height=10, bg="green", fg="white")
submit_button = Button(window, width=10, text="Submit", command=submit, bg="green", fg="white")

label1.grid(row=0,columnspan=2)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)
label4.grid(row=3,column=0)
label5.grid(row=6,column=0)

Name.grid(row=1,column=1)
spin_age.grid(row=2,column=1)

hobby1.grid(row=7,column=0)
hobby2.grid(row=8,column=0)
hobby3.grid(row=9,column=0)
hobby4.grid(row=10,column=0)
hobby5.grid(row=11,column=0)
hobby6.grid(row=12,column=0)
hobby7.grid(row=13,column=0)
hobby8.grid(row=14,column=0)
hobby9.grid(row=15,column=0)
hobby0.grid(row=16,column=0)

textbox.grid(row=17,columnspan=2)
submit_button.grid(row=18,column=0)

window.mainloop()
