#Tool to search for leetcode solutions 
solutionMapping = {2784: "isGood",
           2444: "countSubarrays",
           992: "subarraysWithKDistinct",
           101: "isSymmetric"}

solutionsFile = open("leetcodeSolutions.py")
solutionsBank = solutionsFile.readlines()

solutionNum = int(input("Enter the number of the problem you want to find the solution of: "))
solution = ""
solutionFound = False
nextSolutionName = ""

if solutionNum in solutionMapping.keys():
    solutionName = "def "+solutionMapping[solutionNum]
    for line in solutionsBank:
        if solutionName in line:
            solutionFound = True
        if solutionFound:
            if "self." in line:
                index1 = line.index(".")
                index2 = line.index("(")
                functionName = "def "+line[index1+1:index2]
                if functionName not in solution:
                    nextSolutionName = functionName
            if "return" not in line or "def" not in next(iter(solutionsBank)):
                solution += line
            else:
                solution += line
                solutionFound = False
                if nextSolutionName != "":
                    solution += "\n"
                    solutionName = nextSolutionName
                else:
                    break
    print("\nThe solution is as follows:\n")
    print(solution)
else:
    print("\nThe solution could not be found")


