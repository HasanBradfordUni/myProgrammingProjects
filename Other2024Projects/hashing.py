# Online Python - IDE, Editor, Compiler, Interpreter\
number = int(input('Enter your next number: '))

hashFunct1 = number % 11
print(f'Primary hash function result is: {hashFunct1}')

collision = input('Is there a collision (Y/N): ')
hashFunct2 = (number % 3) + 1

i = 1
newHashFunct = hashFunct1

while collision.lower() == 'y':
    newHashFunct = (hashFunct1 + i*hashFunct2) % 11
    hashFunct2 = (number % 3) + 1
    
    print(f'Result of rehashing is {newHashFunct}')
    collision = input('Is there a collision (Y/N): ')
    
    i += 1

print(f'Number should go in {newHashFunct}')
