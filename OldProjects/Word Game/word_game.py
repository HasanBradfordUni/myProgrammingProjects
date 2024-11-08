#word game
from tkinter import *

class Window(Toplevel):
    def __init__(self, parent, starting_letter, substring, score):
        super().__init__(parent)

        self.title('Play word game!')

        letter = StringVar()
        letter.set(starting_letter)

        sub = StringVar()
        sub.set(substring)

        score1 = StringVar()
        score1.set(str(score))

        Label(self,text="Word Game").grid(row=0,columnspan=2)

        Label(self,text="Starting Letter:").grid(row=1,column=0)
        S_Letter = Entry(self, textvariable=letter)
        S_Letter.grid(row=1,column=1)

        Label(self,text="Substring:").grid(row=2,column=0)
        Substring = Entry(self, textvariable=sub)
        Substring.grid(row=2,column=1)

        Label(self,text="Score:").grid(row=3,column=0)
        Score = Entry(self, textvariable=score1)
        Score.grid(row=3,column=1)
        
        box = Text(self)
        box.grid(row=4,columnspan=2)

        Label(self,text="Enter word:").grid(row=5,column=0)
        Word = Entry(self)
        Word.grid(row=5,column=1)
        
        def show_rules():
            box.delete("1.0", END)
            box.insert("1.0", """The rules are as follows:
1. The word has to be between 3 and 10 letters
2. The word has to start with """+starting_letter+""" and contain """+substring+"""
3. The word you enter (if correct) will fill the column from top to end of word
4. Points are scored based on the length of the word""")

        def show_grid(grid):
            box.delete("1.0", END)
            for y in range(0,grid_height):
                for x in range(0,grid_width):
                    text = str(grid[y][x])+" "
                    box.insert(END, text)
                box.insert(END, "\n")

        def update_grid(grid,word,turn):
            for y in range(0, len(word)):
                grid[y][turn] = word[y]
            for y in range(len(word), 10):
                grid[y][turn] = "#"
            return grid

        def check_word(word,starting_letter,substring):
            fileIn = open("sowpods.txt", "r")
            for line in fileIn:
                line = line.strip("\n")
                if line == word:
                    word_valid = True
                else:
                    word_valid = False
            if word[0] == starting_letter:
                word_valid = True
            elif substring in word:
                word_valid = True
            else:
                word_valid = False
            fileIn.close()
            return word_valid

        def play_word(score,turn,grid):
            word_valid = False
            word = Word.get()
            word_valid = check_word(word,starting_letter,substring)
            while len(word) < 3 or len(word) > 10 or word_valid == False:
                if word == "x":
                    break
                box.insert(END, "Invalid word")
            else:
                update_grid(grid,word,turn)
            score += len(word)
            turn += 1
            show_grid(grid)    
            return turn

        Button(self,text='Rules',command=show_rules).grid(row=6, column=0)
        Button(self,text='Grid',command=lambda: show_grid(grid)).grid(row=6, column=1)
        Button(self,text='Play Word',command=lambda: play_word(score,turn,grid)).grid(row=7, column=0)
        Button(self,text='Close',command=self.destroy).grid(row=7, column=1)

class App(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x200')
        self.title('Login in to Word Game')

        label1 = Label(self, text="Login")
        label1.grid(row=0,columnspan=2)

        Label(self, text="Username:").grid(row=1, column=0)
        Label(self, text="Password:").grid(row=2, column=0)

        username = Entry(self)
        password = Entry(self)

        def open_game():
            fileOut = open("logins.txt", 'a')
            Username = username.get()
            Password = password.get()
            text = Username+","+Password+"\n"
            fileOut.write(text)
            fileOut.close()
            window = Window(self, starting_letter, substring, score)
            window.grab_set()

        username.grid(row=1, column=1, sticky="W")
        password.grid(row=2, column=1, sticky="W")
        
        Button(self,text='Submit',command=open_game).grid(row=3, column=0)
        Button(self,text='Exit',command=self.destroy).grid(row=3, column=1)


import random

grid_width = 10
grid_height = 10
grid = []
score = 0
turn = 0

def fill_grid(grid):
    for i in range(0, grid_height):
        line = []
        for j in range(0, grid_width):
            letter_num = random.randint(0,25)
            letter_num += 97
            line.append(chr(letter_num))
        grid.append(line)
    return grid

def get_letters():
    letters_list = ["a","b","c","d","e","f","g","h","i","j","k","l",
                    "m","n","o","p","r","s","t","u","v","w","y"]
    substring_list = ["oa","ea","as","aw","io","oi","oy","ar","ir",
                      "er","or","un","ae","at","ng","th","sh","ou",
                      "ay","ai","in","ad","al","ac","ab","an","on"]
    endList1 = (len(letters_list)-1)
    endList2 = (len(substring_list)-1)
    starting_letter = letters_list[random.randint(0,endList1)]
    substring = substring_list[random.randint(0,endList2)]
    return starting_letter, substring
    
def display_rules(starting_letter,substring):
    print("The rules are as follows: \n")
    print("1. The word has to be between 3 and 10 letters")
    print("2. The word has to start with \'"+starting_letter+"\' and contain \'"+substring+"\'")
    print("3. The word you enter (if correct) will fill the column from top to end of word")
    print("4. Points are scored based on the length of the word")
    print("5. You can enter below how wide the grid should be \n")
    grid_width = int(input("How wide should the grid be? "))
    return grid_width


#main
starting_letter, substring = get_letters()
fill_grid(grid)
app = App()
app.mainloop()
