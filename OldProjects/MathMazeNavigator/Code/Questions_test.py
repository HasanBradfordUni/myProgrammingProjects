from time import sleep

def get_questions(fileName):
    questions = [] #initialises the variable 'questions' as an empty array
    if fileName != None: #checks if the file actually exists
        for line in fileName: #runs a FOR loop through each line of the file
            newLine = line.strip("\n").split(",") #creates the array which will be appended to 'questions'
            questions.append(newLine) #appends the array stored in 'newLine' to 'questions'
    return questions #returns the 'questions' 2D array to the app class

def open_question(questions):
    question = questions[0] #get the first question from the array
    print(question)
    questions.remove(question) #remove the previous question from the questions array

file = input("Enter the name of a question file: ")

if file == "GCSE":
    try:
        fileName = open("GCSE_qs.txt", mode='r')
    except:
        print("Question file missing or corrupt!")
elif file == "Easy":
    try:
        fileName = open("Easy_qs.txt", mode='r')
    except:
        print("Question file missing or corrupt!")
elif file == "Medium":
    try:
        fileName = open("Medium_qs.txt", mode='r')
    except:
        print("Question file missing or corrupt!")
elif file == "Hard":
    try:
        fileName = open("Hard_qs.txt", mode='r')
    except:
        print("Question file missing or corrupt!")
elif file == "NS":
    try:
        fileName = open("NS_qs.txt", mode='r')
    except:
        print("Question file missing or corrupt!")
else:
    print("An error has occured!")

questions = get_questions(fileName)
calls = 0

print(len(questions))
amountOfQs = len(questions)

while True:
    if calls < amountOfQs:
        open_question(questions) #calls the 'open_question' function
        calls += 1 #increment calls by 1
        sleep(1)
    else: 
        print("No more questions to display")
        break
