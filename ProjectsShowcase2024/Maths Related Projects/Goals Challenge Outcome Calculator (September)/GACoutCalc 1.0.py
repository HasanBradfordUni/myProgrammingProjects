#Goals challenge outcome calculator
import pyperclip

def findHistory(currentGoals):
	#This function will search for a file called challengeHistory.txt and return the summary statistics
	try:
		file = open("newChallengeHistory.txt", 'r')
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
		file = open("newChallengeHistory.txt", 'a')
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

combos = {15000: [1,1,1,2,2,2,3,3,4,5],}
combosDisplay = {1: "Career", 2: "Double", 3: "Triple", 4: "Quad", 5:"xFive", 6:"xSix", 7:"xSeven", 8:"xEight", 9:"xNine", 10:"xTen", 11:"xEleven", 12:"xTwelve", 13:"xThirteen", 15:"xFifteen", 20:"xTwenty", 25: "xTwentyFive", 30:"xThirty", 35: "xThirtyFive", 40: "xFourty", 50:"xFifty", 100: "xHundred"}
clipboard = Clipboard()

print("""Choose a goals & assists target for the challenge, possible targets are below:
	1. 15,000 Goals & Assists
Type the number of your choice, e.g. for 15,000 g/a choose 1""")
choiceInput = input()

choice = 0

while choice == 0:
	match choiceInput:
		case "1":
			choice = 15000
			print("You chose 15000 goals & assist!")
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
	chosenGoals = int(input("Enter the number of g/a he has with the multiplier: "))
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
print("\nThe best possible result for the amount of goals & assists for each combo are:\n")
clipboard.addToClipboard("The best possible result for the amount of goals & assists for each combo are:\n")
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
print("\nThe worst possible result for the amount of goals & assists for each combo are:\n")
clipboard.addToClipboard("\nThe worst possible result for the amount of goals & assists for each combo are:\n")
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
outcomeString = "\nYour total goals & assists for the challenge were "+str(normalOutcome)+" goals & assists, the best possible outcome was "+str(bestOutcome)+" goals & assists and the worst possible outcome was "+str(worstOutcome)+" goals & assists."
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
averageString = f"\nYour final score of {normalOutcome} goals & assists ranks {attemptRank} out of {attempts} attempts, {keyword} the average score of {averageScore}."
print(averageString)
clipboard.addToClipboard(averageString)
clipboard.addToClipboard("\n")
accuraciesString = f"The best outcome would be {difference} goals & assists higher meaning you scored {accuracy}% (average {averageAccuracy}%) accuracy."
print(accuraciesString)
clipboard.addToClipboard(accuraciesString)
clipboard.addToClipboard("\n")
if normalOutcome > choice:
        resultString = "Congratulations, you have achieved your target of "+str(choice)+" g/a!"
else:
        resultString = "Unfortunately you did not achieve your target of "+str(choice)+" g/a." 
print(resultString)
clipboard.addToClipboard(resultString)
clipboard.addToClipboard("\n")
print()
writeHistory(choice, normalOutcome, bestOutcome)
print("Summary will now be copied to clipboard...")
clipboard.copyClipboard()
