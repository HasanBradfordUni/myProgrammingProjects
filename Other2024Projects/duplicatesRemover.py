"""Scan through the lines of text in a file and remove any duplicate lines"""
def removeDuplicates(filename):
    oldText = ""
    print("Original text: ")
    file = open(filename, 'r')
    for line in file:
        print(line)
        oldText += line
    newText = ""
    print("Text after removing duplicates: ")
    for text in oldText.splitlines(True):
        if text not in newText:
            print(text)
            newText += text
    file = open(filename, 'w')
    file.write(newText)
    file.close()

#now call the above function after taking user input
filename = input("Enter the name of the file (with extension): ")
removeDuplicates(filename)