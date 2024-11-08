from HighScores_class import HighScores
from random import randint

score = randint(500, 1050)
high_scores = HighScores()
fileIn = open('high_scores.txt', 'r')

scores = high_scores.get_scores(fileIn)
fileIn.close()

intScores = []

print("Your score is:",score)
name = input("Enter your name to save this score: ")

if high_scores.check_score(score):
    scores = high_scores.add_score(name, score)
    for item in scores:
        intScores.append(int(item))
    print(high_scores.sort_scores(intScores))
    sortedNames = high_scores.sortNames()
    sortedNames = sortedNames[::-1]
    fileOut = open('high_scores.txt', 'w')
    high_scores.saveScore(fileOut, sortedNames)
    fileOut.close()
else:
    print("Score is not high enough!")
