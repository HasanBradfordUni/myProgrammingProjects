import os
# Count the number of files of a certain type in a directory
# The directory is the root directory of the program
# The file type is the file extension

def count_files(rootDir, fileType):
    count = 0
    for root, dirs, files in os.walk(rootDir):
        for file in files:
            #print(file)
            if file.endswith(fileType):
                count += 1
    return count

def main():
    fileType = input("Please enter the file type you would like to count: ")
    rootDir = input("Please enter the root directory of the program (. for this directory): ")
    print(f"The number of {fileType} files in the directory is: {count_files(rootDir, fileType)}")

if __name__ == "__main__":
    main()


