class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        #add a main menu with different options based on the user's choice
        self.main_menu = {1: "Main program (Infinite insertion but no searching)", 2: "Set up hash table", 3: "Insert value(s)", 4: "Search for a value", 5: "Display the hash table", 6: "Exit"}
        #add a menu based dictionary for different hash collision resolutions with numbers as the keys
        self.collision_menu = {1: "Linear Probing", 2: "Quadratic Probing", 3: "Double Hashing", 4: "Chaining", 5: "Rehashing"}
        self.hash_functions = {1: self.hash_function_1, 2: self.hash_function_2, 3: self.hash_function_3}
        self.menu_history = []
        self.collision_choice = 0

    #add a method to display the main menu
    def display_main_menu(self):
        print("\nMenu options are as follows:")
        for key, value in self.main_menu.items():
            print(f"{key}: {value}")

    #add a method to display the collision resolution menu
    def display_collision_menu(self):
        for key, value in self.collision_menu.items():
            print(f"{key}: {value}")

    #add a method to handle the collision resolution menu
    def get_collision_resolution(self):
        print("\nChoose a collision resolution method:")
        self.display_collision_menu()
        choice = int(input("Enter your choice: "))
        if choice not in self.collision_menu:
            print("Invalid choice. Try again.")
            return self.get_collision_resolution()
        return choice

    def hash_function_1(self, key):
        print("Using hash function 1 - Modulo Division by size")
        return key % self.size

    def hash_function_2(self, key):
        print("Using hash function 2 - Mid Square Method")
        return (key // self.size) % self.size
    
    def hash_function_3(self, key):
        print("Using hash function 3 - Modulo Division by fraction of size and then add 1")
        if self.size < 5:
            return (key % (self.size // 3)) + 1
        else:
            return (key % (self.size // 5)) + 1
        
    #add a method to handle linear probing
    def linear_probing(self, index):
        while self.table[index] is not None:
            index = (index + 1) % self.size
        return index
    
    #add a method to handle quadratic probing
    def quadratic_probing(self, index):
        i = 1
        while self.table[index] is not None:
            index = (index + i**2) % self.size
            i += 1
        return index
    
    #add a method to handle double hashing
    def double_hashing(self, index, key):
        hash_function = self.hash_functions[2]
        hash2 = hash_function(key)
        i = 1
        while self.table[index] is not None:
            index = (index + i * hash2) % self.size
            i += 1
        return index
    
    #add a method to handle chaining
    def chaining(self, index, key):
        if self.table[index] is None:
            self.table[index] = [key]
        else:
            self.table[index].append(key)
    
    #add a method to handle rehashing
    def rehashing(self, index, key, hash_function):
        new_table_size = int(input("Enter the new size of the hash table: "))
        while new_table_size <= self.size:
            print("New size should be greater than the current size.")
            new_table_size = int(input("Enter the new size of the hash table: "))
        self.size = new_table_size
        temp_table = []
        for value in self.table:
            if value is not None:
                temp_table.extend(value)
        self.table = [None] * new_table_size
        for value in temp_table:
            collision = self.insert(value, hash_function)
            if not collision:
                print(f"Inserted {value} successfully.")
                temp_table.remove(value)
            else:
                print(f"Failed to insert {value}. Will be dealt with later.")
        i = 0
        for value in temp_table:
            if self.table[i] is None:
                self.table[i] = [value]
            i += 1
        print("Rehashing complete.")
        view_table = input("Do you want to view the new hash table (Y/N)? ")
        if view_table.lower() == 'y':
            self.display()
            
    #add a set size method to allow the user to change the size of the hash table
    def set_size(self, size):
        self.size = size
        self.table = [None] * size

    def search(self, key, hash_function):
        print("\nSearching for key in the hash table...")
        index = hash_function(key)
        found = False
        if key in self.table[index]:
            print(f"{key} found at index {index}.")
            found = True
        else:
            print(f"{key} not found. It may be at another index.")
            found = False
            for i, slot in enumerate(self.table):
                if slot is not None and key in slot:
                    print(f"{key} found at index {i}.")
                    found = True
                    break
            if not found:
                print(f"{key} not found in the hash table.")
            
    def insert(self, key, hash_function):
        index = hash_function(key)
        if index < self.size - 1 and self.table[index] is None:
            self.table[index] = [key]
            return False
        elif index >= self.size - 1:
            self.table.append(key)
            return False
        else:
            print("Collision detected! Resolving collision...")
            return True
    
    def get_index(self, key, hash_function):
        return hash_function(key)

    def handle_collision(self, index, key):
        print("\nHandling collision using your selected method...")
        if self.collision_choice == 1:
            index = self.linear_probing(index)
        elif self.collision_choice == 2:
            index = self.quadratic_probing(index)
        elif self.collision_choice == 3:
            index = self.double_hashing(index, key)
        elif self.collision_choice == 4:
            self.chaining(index, key)
        elif self.collision_choice == 5:
            self.rehashing(index, key)
        return index

    def display(self):
        for i, slot in enumerate(self.table):
            print(f"Index {i}: {slot}")

def main():
    size = int(input("Enter the size of the hash table: "))
    hash_table = HashTable(size)

    while True:
        print("\nChoose a hash function:")
        print("1. Hash function 1")
        print("2. Hash function 2")
        print("3. Hash function 3")
        choice = int(input("Enter your choice (1, 2 or 3): "))

        if choice == 1:
            hash_function = hash_table.hash_function_1
            break
        elif choice == 2:
            hash_function = hash_table.hash_function_2
            break
        elif choice == 3:
            hash_function = hash_table.hash_function_3
            break
        else:
            print("Invalid choice. Try again.")
            continue

    hash_table.collision_choice = hash_table.get_collision_resolution()
    print(f"You chose {hash_table.collision_menu[hash_table.collision_choice]} as the collision resolution method.")
    key = 0
    
    while key != -1:
        key = int(input("Enter the key to insert (-1 to stop): "))
        collision = hash_table.insert(key, hash_function)
        if collision:
            index = hash_table.get_index(key, hash_function)
            index = hash_table.handle_collision(index, key)
            if hash_table.collision_choice != 4 and hash_table.collision_choice != 5:
                hash_table.table[index] = [key]
        hash_table.display()

def handle_program():
    #display welcome messages, main menu and handle user input
    print("Welcome to the Akhtar Hasan Hash Table Simulator!")
    print("This program simulates a hash table with different collision resolution methods.")
    print("You can choose the size of the hash table and the hash function to use.")
    print("You can also insert keys into the hash table and search for keys.")
    print("The main menu will now be displayed, please choose an option.")
    hash_table = HashTable(1)
    hash_table.display_main_menu()
    hash_function = None
    choice = 0
    while choice != 6:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            #print(hash_table.menu_history)
            main()
        elif choice == 2:
            #print(hash_table.menu_history)
            size = int(input("Enter the size of the hash table: "))
            hash_table.set_size(size)
            while True:
                print("\nChoose a hash function:")
                print("1. Hash function 1")
                print("2. Hash function 2")
                print("3. Hash function 3")
                funct_choice = int(input("Enter your choice (1, 2 or 3): "))

                if funct_choice == 1:
                    hash_function = hash_table.hash_function_1
                    break
                elif funct_choice == 2:
                    hash_function = hash_table.hash_function_2
                    break
                elif funct_choice == 3:
                    hash_function = hash_table.hash_function_3
                    break
                else:
                    print("Invalid choice. Try again.")
                    continue

            hash_table.collision_choice = hash_table.get_collision_resolution()
        elif choice == 3:
            #print(hash_table.menu_history)
            if hash_table.main_menu[2] not in hash_table.menu_history:
                print("Please set up the hash table first.")
                continue
            values = int(input("How many vaulues do you want to insert? "))
            for i in range(values):
                key = int(input("Enter the key to insert: "))
                collision = hash_table.insert(key, hash_function)
                if collision:
                    index = hash_table.get_index(key, hash_function)
                    index = hash_table.handle_collision(index, key)
                    if hash_table.collision_choice != 4 and hash_table.collision_choice != 5:
                        hash_table.table[index] = [key]
        elif choice == 4:
            #print(hash_table.menu_history)
            if hash_table.main_menu[3] not in hash_table.menu_history:
                print("Please insert values into the hash table first.")
                if hash_table.main_menu[2] not in hash_table.menu_history:
                    print("Please set up the hash table first as well.")
                continue
            key = int(input("Enter the key to search for: "))
            hash_table.search(key, hash_function)
        elif choice == 5:
            #print(hash_table.menu_history)
            if hash_table.main_menu[2] not in hash_table.menu_history:
                print("Please set up the hash table first.")
                continue
            hash_table.display()
        elif choice == 6:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Try again.")
            continue
        hash_table.menu_history.append(hash_table.main_menu[choice])
        hash_table.display_main_menu()

if __name__ == "__main__":
    handle_program()