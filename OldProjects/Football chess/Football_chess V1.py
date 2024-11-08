#Football chess

class Board():
    def __init__(self, array, width, length):
        self.__array = array
        self.__width = width
        self.__length = length

    def set_array(self, array):
        self.__array = array

    def draw(self):
        pass

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
    print(array, width, length)

if __name__ == "__main__":
    main()
