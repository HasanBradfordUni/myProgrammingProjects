from translation import translation_main
from Error_checker import error_checker_main, check_syntax

def clean_file(file):
    for num in range(0, len(file)):
        if num == 25:
            file[num] = ""
        elif num == 33:
            file[num] = ""
    return file

def clean_file2(file):
    for num in range(0, len(file)):
        if 5 <= num <= 8:
            file[num] = ""
    return file

if __name__ == '__main__':
    parsing_error = False
    translation_main()
    errors = check_syntax('translated_code.py')
    more_errors = True
    while more_errors:
        for error in errors:
            error = error.split("\n")
            for line in error:
                splitLine = line.split(":")
                if len(splitLine) > 3 and (splitLine[3] == " E0602" or splitLine[3] == " E0601"):
                    more_errors = True
                    parsing_error = error_checker_main()
                if parsing_error:
                    with open("translated_code.py", "r") as file:
                        newFile = clean_file(file.readlines())
                    with open("translated_code.py", "w") as file:
                        for thisLine in newFile:
                            file.write(thisLine)
                    parsing_error = False
                else:
                    more_errors = False
    with open("translated_code.py", "r") as file:
        newFile = clean_file2(file.readlines())
    with open("translated_code.py", "w") as file:
        for thisLine in newFile:
            file.write(thisLine)
