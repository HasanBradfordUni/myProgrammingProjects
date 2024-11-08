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
                        print(" ", end= " | ")
                    else:
                        rowLabel = y
                        print(rowLabel, end=" | ")
                if y == 0 and x != 0:
                    colLabel = chr((x+96))
                    print(colLabel, end=" | ")
                if x != 0 and y != 0:
                    piece = self.__array[x-1][y-1]
                    if piece == None:
                        piece = " "
                    print(piece, end=" | ")
            print()

    def get_array(self):
        return self.__array

    def get_width(self):
        return self.__width

    def get_length(self):
        return self.__length

def setup_array(width, length):
    array = []
    for x in range(0, width):
        row = []
        for y in range(0, length):
            row.append(None)
        array.append(row)
    return array
    
def main():
    width = int(input("Enter a width for the board: "))
    length = int(input("Enter a length for the board: "))
    array = setup_array(width, length)
    board = Board(array, width, length)
    array = board.get_array()
    width = board.get_width()
    length = board.get_length()
    board.draw()

if __name__ == "__main__":
    main()
