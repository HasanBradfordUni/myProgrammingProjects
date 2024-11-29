#Goals challenge outcome calculator
import pyperclip

def findHistory(currentGoals):
	#This function will search for a file called challengeHistory.txt and return the summary statistics
	try:
		file = open("challengeHistory.txt", 'r')
		#Read the file and split the contents into a list
		contents = file.read().split("\n")
		#Close the file
		file.close()
		#Create a list to store the contents of the file
		attempts = 1
		historicalTotals = []
		historicalAccuracies = []
		#Iterate through the contents of the file
		for line in contents:
			if line:
				#Split the line into a list
				line = line.split(",")
				goals = int(line[0][7:])
				if goals == currentGoals:
					attempts += 1
					total = int(line[1][15:])
					bestTotal = int(line[2][13:])
					accuracy = float(total / bestTotal * 100)
					#Append the line to the history list
					historicalTotals.append(total)
					historicalAccuracies.append(accuracy)
		#Return the history list
		return attempts, historicalTotals, historicalAccuracies
	except FileNotFoundError:
		#If the file is not found return default values
		return 1, [], []
		
def writeHistory(goalsChoice, currentOutcome, bestOutcome):
	try:
		file = open("challengeHistory.txt", 'a')
		string = f'Goals: {goalsChoice}, Actual Score: {currentOutcome}, Best Score: {bestOutcome}\n'
		file.write(string)
		file.close()
		print("History saved successfully!")
	except FileNotFoundError:
		print("Cannot save history!")

class Clipboard():
        def __init__(self):
                self.clipboardSummary = ""

        def addToClipboard(self, text):
                self.clipboardSummary += text

        def copyClipboard(self):
                pyperclip.copy(self.clipboardSummary)

combos = {200000: [10,10,10,10,10,25,25,25,25,25,35,35,35,35,50], 
		  100000: [8,8,8,9,9,9,10,10,10,10,10,10,10,11,11,11,11,11,11,11,12,12], 
		  10000: [1,1,1,2,2,2,3,3,4,5], 
		  20000: [2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5], 
		  9000: [1,1,1,2,2,2,3,3,4,4], 
		  7000: [1,1,1,2,2,2,2,3,3,4], 
		  500000: [20,20,20,20,20,35,35,35,35,35,50,50,50,50,100,100],
		  90000: [7,7,7,7,7,8,8,8,8,8,9,9,9,9,9,10,10,10,10,10,10,10,11,11,11],
		  80000: [6,6,6,6,6,6,7,7,7,7,7,8,8,8,8,8,9,9,9,9,10],
		  70000: [5,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,8,8,9,9],
		  30000: [],
		  60000: [],
		  40000: []}
combosDisplay = {1: "Career", 2: "Double", 3: "Triple", 4: "Quad", 5:"xFive", 6:"xSix", 7:"xSeven", 8:"xEight", 9:"xNine", 10:"xTen", 11:"xEleven", 12:"xTwelve", 13:"xThirteen", 15:"xFifteen", 20:"xTwenty", 25: "xTwentyFive", 30:"xThirty", 35: "xThirtyFive", 40: "xFourty", 50:"xFifty", 100: "xHundred"}
clipboard = Clipboard()

print("""Choose a goals target for the challenge, possible targets are below:
	1. 7000 goals
	2. 9000 goals
	3. 10,000 goals
	4. 20,000 goals
	5. 70,000 goals
	6. 80,000 goals
	7. 90,000 goals
	8. 100,000 goals
	9. 200,000 goals
	10. 500,000 goals
Type the number of your choice, e.g. for 10,000 goals choose 3""")
choiceInput = input()

match choiceInput:
	case "1":
		choice = 7000
		print("You chose 7000 goals!")
	case "2":
		choice = 9000
		print("You chose 9000 goals!")
	case "3":
		choice = 10000
		print("You chose 10,000 goals!")
	case "4":
		choice = 20000
		print("You chose 20,000 goals!")
	case "5":
		choice = 70000
		print("You chose 70,000 goals!")
	case "6":
		choice = 80000
		print("You chose 80,000 goals!")
	case "7":
		choice = 90000
		print("You chose 90,000 goals!")
	case "8":
		choice = 100000
		print("You chose 100,000 goals!")
	case "9":
		choice = 200000
		print("You chose 200,000 goals!")
	case "10":
		choice = 500000
		print("You chose 500,000 goals!")
	case _:
		choice = 0
		print("That is not a valid option, choose again!")

choiceCombos = combos[choice]

print("The following combos are associated with this target:\n")
totalGoals = []
playerGoalsMapping = {}
for combo in choiceCombos:
	print("The multiplier is:",str(combo))
	chosenPlayer = input("Enter the player chosen with this multiplier: ")
	chosenGoals = int(input("Enter the number of goals he has with the multiplier: "))
	goals = int(chosenGoals // combo)
	playerGoalsMapping[goals] = chosenPlayer
	totalGoals.append(goals)

normalOutcome = 0
bestOutcome = 0
worstOutcome = 0
for num in range(len(totalGoals)):
	normalOutcome += totalGoals[num]*choiceCombos[num]
#Order the total goals in ascending order
totalGoals.sort()
print("\nThe best possible result for the amount of goals for each combo are:\n")
clipboard.addToClipboard("The best possible result for the amount of goals for each combo are:\n")
clipboard.addToClipboard("\n")

for num in range(len(totalGoals)):
        comboString = str(combosDisplay[choiceCombos[num]])+": "+"Player: "+str(playerGoalsMapping[totalGoals[num]])+", Goals: "+str(totalGoals[num]*choiceCombos[num])
        print(comboString)
        clipboard.addToClipboard(comboString)
        clipboard.addToClipboard("\n")
        bestOutcome += totalGoals[num]*choiceCombos[num]
print("Best Total:",bestOutcome)
clipboard.addToClipboard("Best Total: "+str(bestOutcome))
clipboard.addToClipboard("\n")

#Order the total goals in descending order
totalGoals.sort(reverse=True)
print("\nThe worst possible result for the amount of goals for each combo are:\n")
clipboard.addToClipboard("\nThe worst possible result for the amount of goals for each combo are:\n")
clipboard.addToClipboard("\n")
for num in range(len(totalGoals)):
	comboString = str(combosDisplay[choiceCombos[num]])+": "+"Player: "+str(playerGoalsMapping[totalGoals[num]])+", Goals: "+str(totalGoals[num]*choiceCombos[num])
	print(comboString)
	clipboard.addToClipboard(comboString)
	clipboard.addToClipboard("\n")
	worstOutcome += totalGoals[num]*choiceCombos[num]
print("Worst total:",worstOutcome)
clipboard.addToClipboard("Worst Total: "+str(worstOutcome))
clipboard.addToClipboard("\n")

#Output the results, best, worst and normal in one string
outcomeString = "\nYour total goals for the challenge were "+str(normalOutcome)+" goals, the best possible outcome was "+str(bestOutcome)+" goals and the worst possible outcome was "+str(worstOutcome)+" goals."
print(outcomeString)
clipboard.addToClipboard(outcomeString)
clipboard.addToClipboard("\n")
difference = bestOutcome - normalOutcome
accuracy = round(normalOutcome / bestOutcome * 100, 2)
attempts, historicalTotals, historicalAccuracies = findHistory(choice)
historicalTotals.sort()
historicalTotal = normalOutcome
attemptRank = attempts
totalAccuracies = accuracy
for num in range(len(historicalTotals)):
	if normalOutcome > historicalTotals[num]:
		attemptRank = len(historicalTotals) - num
	totalAccuracies += historicalAccuracies[num]
	historicalTotal += historicalTotals[num]
averageAccuracy = round(totalAccuracies / attempts, 1)
averageScore = round(historicalTotal / attempts, 1)
if normalOutcome > averageScore:
	keyword = "above"
else:
	keyword = "below"
averageString = f"\nYour final score of {normalOutcome} goals ranks {attemptRank} out of {attempts} attempts, {keyword} the average score of {averageScore}."
print(averageString)
clipboard.addToClipboard(averageString)
clipboard.addToClipboard("\n")
accuraciesString = f"The best outcome would be {difference} goals higher meaning you scored {accuracy}% (average {averageAccuracy}%) accuracy."
print(accuraciesString)
clipboard.addToClipboard(accuraciesString)
clipboard.addToClipboard("\n")
if normalOutcome > choice:
        resultString = "Congratulations, you have achieved your target of "+str(choice)+" goals!"
else:
        resultString = "Unfortunately you did not achieve your target of "+str(choice)+" goals." 
print(resultString)
clipboard.addToClipboard(resultString)
clipboard.addToClipboard("\n")
print()
writeHistory(choice, normalOutcome, bestOutcome)
print("Summary will now be copied to clipboard...")
clipboard.copyClipboard()
