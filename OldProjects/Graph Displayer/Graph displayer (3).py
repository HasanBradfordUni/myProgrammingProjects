#graph displayer
import pygame

class Vertex(object):
    def __init__(self, size, colour, locX, locY, text, surf):
        self.__size = size
        self.__text = text
        self.__colour = colour
        self.__surf = surf
        self.__locX = locX
        self.__locY = locY

    def blit_text(self):
        font = pygame.font.SysFont("Arial", self.__size)
        textSurf = font.render(self.__text, 1, self.__colour)
        W = textSurf.get_width()
        H = textSurf.get_height()
        self.__surf.blit(textSurf, [self.__locX-W/2, self.__locY-H/2])

    def draw_circle(self):
        pygame.draw.circle(self.__surf, color=(0,0,255),
                           center=[self.__locX, self.__locY], radius=25)

class Arc(object):
    def __init__(self, size, colour, locX, locY, text, surf):
        self.__size = size
        self.__text = text
        self.__colour = colour
        self.__surf = surf
        self.__locX = locX
        self.__locY = locY

    def blit_text(self):
        startX = self.__locX[0]
        startY = self.__locY[0]
        endX = self.__locX[1]
        endY = self.__locY[1]
        midX = (startX + endX) // 2
        midY = (startY + endY) // 2
        font = pygame.font.SysFont("Arial", self.__size)
        textSurf = font.render(self.__text, 1, self.__colour)
        self.__surf.blit(textSurf, [midX, midY])
        
    def draw_line(self):
        pygame.draw.line(self.__surf, color=(0,0,0),
                         start_pos=self.__locX, end_pos=self.__locY)

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

def get_locX(vertices_list,item):
    letter = vertices_list[item]
    if letter == "A":
        location = 50
    elif letter == "B":
        location = 200
    elif letter == "C":
        location = 400
    elif letter == "D":
        location = 200
    elif letter == "E":
        location = 200
    elif letter == "F":
        location = 400
    elif letter == "G":
        location = 500
    elif letter == "H":
        location = 600
    else:
        location = 750
    return location

def get_locY(vertices_list,item):
    letter = vertices_list[item]
    if letter == "A":
        location = 150
    elif letter == "B":
        location = 50
    elif letter == "C":
        location = 50
    elif letter == "D":
        location = 150
    elif letter == "E":
        location = 250
    elif letter == "F":
        location = 250
    elif letter == "G":
        location = 250
    elif letter == "H":
        location = 125
    else:
        location = 450
    return location

def get_start_pos(vertex1):
    if vertex1 == "A":
        location = [75, 150]
    elif vertex1 == "B":
        location = [225, 50]
    elif vertex1 == "C":
        location = [425, 50]
    elif vertex1 == "D":
        location = [225, 150] 
    elif vertex1 == "E":
        location = [225, 200]
    elif vertex1 == "F":
        location = [425, 250]
    elif vertex1 == "G":
        location = [500, 225]
    elif vertex1 == "H":
        location = [600, 50]
    else:
        location = [750, 750]
    return location
        

def get_end_pos(vertex2):
    if vertex2 == "A":
        location = [75, 150]
    elif vertex2 == "B":
        location = [175, 50]
    elif vertex2 == "C":
        location = [375, 50]
    elif vertex2 == "D":
        location = [175, 150] 
    elif vertex2 == "E":
        location = [200, 225]
    elif vertex2 == "F":
        location = [375, 250]
    elif vertex2 == "G":
        location = [475, 250]
    elif vertex2 == "H":
        location = [575, 50]
    else:
        location = [750, 750]
    return location

def draw_graph(vertices_list, weights_list):
    pygame.init()

    win = pygame.display.set_mode((800, 500))
    pygame.display.set_caption("Graph displayer")

    vertices = []
    arcs = []

    for item in range(0,len(vertices_list)):
        vertex_name = vertices_list[item]
        text = "Vertex "+vertex_name
        locX = get_locX(vertices_list,item)
        locY = get_locY(vertices_list,item)
        vertex = Vertex(10, "white", locX, locY, text, win)
        vertices.append(vertex)

    for item in range(0,len(weights_list)):
        Arcs = list(weights_list.keys())
        arc_name = Arcs[item]
        weight = weights_list[arc_name]
        text = arc_name+" - "+str(weight)
        vertex1 = arc_name[0]
        vertex2 = arc_name[1]
          
        start_pos = get_start_pos(vertex1)
        end_pos = get_end_pos(vertex2)
        arc = Arc(10, "black", start_pos, end_pos, text, win)
        arcs.append(arc)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        win.fill((255,255,255))
        for vertex in vertices:
            vertex.draw_circle()
            vertex.blit_text()
        for arc in arcs:
            arc.draw_line()
            arc.blit_text()
        pygame.display.update()

    if not run:
        pygame.quit()



def main(selected_choice,adj_list,adj_matrix,vertices_list, weights_list):
    noexit = True
    while noexit:    
        if selected_choice == 1:
            name = input("Enter name of vertex: ")
            vertices_list.append(name)
            connected = int(input("Enter how many vertices are connected: "))
            adj_list.create_dict()
            letter_num1 = ord(name.upper())-65
            for num in range(0,connected):
                connection = input("Enter name of connected vertex "+str(num+1)+": ")
                vertices_list.append(connection)
                arc = name+connection
                weight = int(input("Enter a weighted value for vertex "+arc+": "))
                weights_list[arc] = weight
                adj_list.add_item(connection,weight)
                letter_num2 = ord(connection.upper())-65
                adj_matrix.add_value(weight,letter_num1,letter_num2)
            adj_list.end_dict()
            menu()
            selected_choice = choice()
            main(selected_choice,adj_list,adj_matrix,vertices_list, weights_list)
        elif selected_choice == 2:
            print(adj_list.return_dicts())
            menu()
            selected_choice = choice()
            main(selected_choice,adj_list,adj_matrix,vertices_list, weights_list)
        elif selected_choice == 3:
            adj_matrix.return_matrix()
            menu()
            selected_choice = choice()
            main(selected_choice,adj_list,adj_matrix,vertices_list, weights_list)
        elif selected_choice == 4:
            draw_graph(vertices_list, weights_list)
            menu()
            selected_choice = choice()
            main(selected_choice,adj_list,adj_matrix,vertices_list, weights_list)
        elif selected_choice == 5:
            noexit = False
            print("Bye...")
            break
        else:
            print("Please enter an integer between 1 & 5")
            menu()
            selected_choice = choice()
            main(selected_choice,adj_list,adj_matrix,vertices_list, weights_list)

#Main
print("Welcome to the official graph displayer!")
vertices_list = []
weights_list = {}
adj_list = List()
adj_matrix = Matrix()
menu()
selected_choice = choice()
main(selected_choice,adj_list,adj_matrix,vertices_list, weights_list)

