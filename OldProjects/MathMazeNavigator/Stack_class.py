#Stack class

class MovesStack(object):
    def __init__(self):
        self.maxsize = 5 #set the max size of the stack
        self.pointer = -1 #set the pointer to be -1 to begin with
        self.used_positions = 0 #set the used positions
        self.array = [" "] * 5 #set up the array that is used for the stack

    def isEmpty(self): #method to check if the stack is empty
        if self.pointer == -1: #checks if the pointer is at -1
            return True #if it is, returns True
        else: #otherwise...
            return False #returns False

    def isFull(self): #method to check if the stack is full
        end = self.maxsize - 1 #gets the end index
        if self.pointer == end: #checks if the pointer is at 'end'
            return True #if it is, returns True
        else: #otherwise...
            return False #returns False

    def peek(self): #method to check the top item of stack
        data = None #sets up a variable called 'data'
        empty = self.isEmpty() #checks if the stack is empty
        if empty: #if it is empty...
            print("Stack underflow!") #prints a suitable error message
        else: #otherwise...
            data = self.array[self.pointer] #sets data to be the top item of the stack
        return data #returns said item

    def push(self,data): #method to push onto the stack
        full = self.isFull() #checks if the stack is full
        if full: #if it is full...
            print("Stack overflow!") #prints a suitable error message
        else: #otherwise...
            self.pointer += 1 #increments pointer by 1
            self.array[self.pointer] = data #sets the top item of the stack to be 'data'
            self.used_positions += 1 #increments 'used_positions' by 1

    def pop(self): #method to pop from the stack
        data = None #sets up a variable called 'data'
        empty = self.isEmpty() #checks if the stack is empty
        if empty: #if it is empty...
            print("Stack underflow!") #prints a suitable error message
        else: #otherwise...
            data = self.array[self.pointer] #sets data to be the top item of the stack
            self.pointer -= 1 #decrements the pointer by 1
            self.used_positions -= 1 #decrements 'used_positions' by 1
        return data #returns 'data'

    def reversePop(self):
        first = self.array[0]
        self.array.remove(first)
        for num in range(1, len(self.array)):
            temp = self.array[num]
            self.array[num-1] = temp
        self.pointer -= 1 #decrements the pointer by 1
        self.used_positions -= 1 #decrements 'used_positions' by 1
        last = self.maxsize - 1
        self.array.append(" ")

    def return_stack(self): #method to return stack when testing
        print(self.array) #prints the stack array
        #prints other information about the stack
        print("Info: Pointer("+str(self.pointer)+") Used Positions("+str(self.used_positions)+")")

class MovesQueue(object):
    def __init__(self):
        self.array = [""] * 5
        self.maxsize = 5
        self.front = 0
        self.rear = -1
        self.used_positions = 0

    def isEmpty(self):
        if self.used_positions == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.used_positions == self.maxsize:
            return True
        else:
            return False

    def enQueue(self,item):
        full = self.isFull()
        if full:
            print("Queue is full!")
        else:
            self.rear += 1
            if self.rear < self.maxsize:
                self.array[self.rear] = item
                self.used_positions += 1

    def deQueue(self):
        empty = self.isEmpty()
        if empty:
            print("Queue is empty!")
        else:
            item = self.array[self.front]
            self.array[self.front] = " "
            self.front += 1
            self.rear -= 1
            self.used_positions -= 1
            return item

    def return_queue(self):
        print(self.array)
        print("Info: Front("+str(self.front)+"),Rear("+str(self.rear)+"),Used Positions("+str(self.used_positions)+")")
