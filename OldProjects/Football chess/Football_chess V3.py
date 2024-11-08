#Football chess

class Board():
    def __init__(self, array, width, length):
        self.__array = array
        self.__width = width
        self.__length = length

    def set_array(self, array):
        self.__array = array

    def draw(self):
        for x in range(0, self.__width+1):
            for y in range(0, self.__length+1):
                if x == 0 and y == 0:
                    print(" ")
                if x == 0 and 0 <= y <= 8:
                    if y == 0:
                        print(" ", end= " |  ")
                    else:
                        rowLabel = y
                        print(rowLabel, end="  |  ")
                if y == 0 and x != 0:
                    colLabel = chr((x+96))
                    print(colLabel, end=" | ")
                if x != 0 and y != 0:
                    piece = self.__array[x-1][y-1]
                    if piece == None:
                        piece = "   "
                    print(piece, end=" | ")
            print()

    def get_array(self):
        return self.__array

    def get_width(self):
        return self.__width

    def get_length(self):
        return self.__length

def initialisePieces(width, length):
    piecesArray = []
    for x in range(0, width):
        piecesRow = []
        for y in range(0, length):
            piecesRow.append(None)
        piecesArray.append(piecesRow)
    piecesArray[0][0] = "cdm"
    piecesArray[0][1] = "rb"
    piecesArray[0][2] = "cb"
    piecesArray[0][3] = ":gk:"
    piecesArray[0][4] = ":  :"
    piecesArray[0][5] = "cb"
    piecesArray[0][6] = "lb"
    piecesArray[0][7] = "cm"
    piecesArray[1][2] = "lw"
    piecesArray[1][3] = "cam"
    piecesArray[1][4] = "st"
    piecesArray[1][5] = "rw"
    piecesArray[6][2] = "LW"
    piecesArray[6][3] = "ST"
    piecesArray[6][4] = "CAM"
    piecesArray[6][5] = "RW"
    piecesArray[7][0] = "CDM"
    piecesArray[7][1] = "RB"
    piecesArray[7][2] = "CB"
    piecesArray[7][3] = ";  ;"
    piecesArray[7][4] = ";GK;"
    piecesArray[7][5] = "CB"
    piecesArray[7][6] = "LB"
    piecesArray[7][7] = "CM"
    return piecesArray

def menu():
    print("1. New Game")
    print("2. How to play")
    print("3. About this game")
    print("4. Quit")
    return [1, 2, 3, 4]

def get_choice():
    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Choice not valid - please enter again!")
        choice = get_choice()
    return choice

def check_choice(choice, options):
    choiceValid = False
    if choice in options:
        choiceValid = True
    else:
        choiceValid = False
        print("Choice not valid - please enter again!")
        choice = get_choice()
    return choiceValid, choice

def new_game():
    width = 8
    length = 8
    piecesArray = initialisePieces(width, length)
    array = setup_array(width, length)
    board = Board(array, width, length)
    array = setup_pieces(array, piecesArray)
    board.set_array(array)
    board.draw()

def setup_array(width, length):
    array = []
    for x in range(0, width):
        row = []
        for y in range(0, length):
            row.append(None)
        array.append(row)
    return array

def setup_pieces(array, piecesArray):
    for x in range(0, len(array)):
        for y in range(0, len(array)):
            if piecesArray[x][y] != None:
                array[x][y] = piecesArray[x][y]
    return array
    
def main():
    options = menu()
    choice = get_choice()
    choiceValid, choice = check_choice(choice, options)
    if choiceValid and choice == 1:
        new_game()
    

if __name__ == "__main__":
    main()
