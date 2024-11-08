import subprocess
import numpy

def check_syntax(filename):
    errors = []
    result = subprocess.run(['pylint', filename], stdout=subprocess.PIPE)
    errors.append(result.stdout.decode())
    return errors

def error_checker_main():
    parsing_error = False
    errors = check_syntax('translated_code.py')
    with open("translated_code.py", "r") as file:
        oldCode = file.readlines()
        print("Old Code:", oldCode)

    lineNumbers = numpy.array([])
    errorNum = 0
    variable_to_value = {"rate": "random.randint(1, 10)",
                         "error": "random.choice([True, False])",
                         "errorNumber": "random.choice([1, 3, 5])",
                         "employees": "file.readlines()",
                         "file": "open('employees.txt', 'r')",
                         "Employees": "[Employee(i*5, i) for i in range(1,11)]",
                         "count": "0"}
    notImported = True

    for error in errors:
        error = error.split("\n")
        for line in error:
            splitLine = line.split(":")
            if len(splitLine) > 3 and (splitLine[3] == " E0602" or splitLine[3] == " E0601"):
                lineNumber = int(splitLine[1]) - 1
                lineNumbers = numpy.append(lineNumbers, lineNumber)
                variableName = splitLine[4].split("'")[1]
                if variableName == "random":
                    if notImported:
                        oldCode.insert(0, 'import random \n')
                        notImported = False
                elif variableName == "Employee":
                    oldCode.insert(1,
                                   "class Employee:\n\tdef __init__(self, hours, rate):\n\t\tself.hours = "
                                   "hours\n\t\tself.rate = rate\n")
                else:
                    variableValue = variable_to_value[variableName]
                    if errorNum > 0:
                        lineNumbers += errorNum
                    lineNumber = lineNumbers[len(lineNumbers) - 1]
                    oldCode.insert(int(lineNumber), f'{variableName} = {variableValue}\n')
                    errorNum += 1
            elif len(splitLine) > 3 and splitLine[3] == " E0001":
                parsing_error = True
                print("Parsing Error")
                break

    print("New Code:", oldCode)
    file = open("translated_code.py", "w")
    for code in oldCode:
        file.write(code)
    file.close()
    return parsing_error

if __name__ == '__main__':
    error_checker_main()
