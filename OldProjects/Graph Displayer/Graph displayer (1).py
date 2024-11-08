#graph displayer

class Matrix(object):
    def __init__(self):
        self.__array = []
        for x in range(10):
            row = []
            for y in range(26):
                row.append("")
            self.__array.append(row)

    def add_value(self,value,value_x,value_y):
        self.__array[value_x][value_y] = value
        
    def return_matrix(self):
        for x in range(10):
            print("[",end="")
            for y in range(26):
                if self.__array[x][y] == "":
                    print("0",end=",")
                else:
                    print(self.__array[x][y],end=",")
            print("]",end="\n")

class List(object):
    def __init__(self):
        self.__dicts = []

    def create_dict(self):
        self.__dict = Dictionary()

    def add_item(self,key,value):
        self.__dict.add_item(key,value)

    def end_dict(self):
        self.__dicts.append(self.__dict.Return())
    
    def return_dicts(self):
        return self.__dicts

class Dictionary(object):
    def __init__(self):
        self.__self = {}

    def add_item(self,key,value):
        self.__self[key] = value

    def Return(self):
        return self.__self

def menu():
    print("""1. Create vertex in graph;
2. Show graph in adjacency matrix;
3. Show graph in adjacency list;
4. Draw graph;
5. Exit program.""")

def choice():
    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Please enter an integer between 1 & 5")
        selected_choice = choice()
    return choice
    
def draw_graph():
    print("Function coming soon!")
        
def main(selected_choice,adj_list,adj_matrix):
    noexit = True
    while noexit:    
        if selected_choice == 1:
            name = input("Enter name of vertex: ")
            connected = int(input("Enter how many vertices are connected: "))
            adj_list.create_dict()
            letter_num1 = ord(name.upper())-65
            for num in range(0,connected):
                connection = input("Enter name of connected vertex "+str(num+1)+": ")
                weight = int(input("Enter a weighted value for vertex "+name+connection+": "))
                adj_list.add_item(connection,weight)
                letter_num2 = ord(connection.upper())-65
                adj_matrix.add_value(weight,letter_num1,letter_num2)
            adj_list.end_dict()
            menu()
            selected_choice = choice()
            main(selected_choice,adj_list,adj_matrix)
        elif selected_choice == 2:
            print(adj_list.return_dicts())
            menu()
            selected_choice = choice()
            main(selected_choice,adj_list,adj_matrix)
        elif selected_choice == 3:
            print(adj_matrix.return_matrix())
            menu()
            selected_choice = choice()
            main(selected_choice,adj_list,adj_matrix)
        elif selected_choice == 4:
            draw_graph()
            menu()
            selected_choice = choice()
            main(selected_choice,adj_list,adj_matrix)
        elif selected_choice == 5:
            noexit = False
            print("Bye...")
            break
        else:
            print("Please enter an integer between 1 & 5")
            menu()
            selected_choice = choice()
            main(selected_choice,adj_list,adj_matrix)

#Main
print("Welcome to the official graph displayer!")
adj_list = List()
adj_matrix = Matrix()
menu()
selected_choice = choice()
main(selected_choice,adj_list,adj_matrix)

