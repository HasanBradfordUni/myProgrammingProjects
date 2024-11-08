#HighScores class

class HighScores(object):
    #the contructor method for the class
    def __init__(self):
        #set up the scores array and names dictionary
        self.__scores = []
        self.__nameDict = {}

    #the method to get the scores and names from the file
    def get_scores(self, fileName):
        for line in fileName: #sets up a FOR loop which cycles through the file
            line = line.strip().split(",") #removes the '\n' and splits the line by the comma
            self.__scores.append(line[1]) #appends the score to the scores array
            self.__nameDict[line[0]] = float(line[1]) #creates a key-value pair for the name and score in the names dictionary
        return self.__scores #returns the scores array to the 'Main' program

    #merge sort method to sort the scores
    def sort_scores(self, scores):
        if len(scores) > 1: #if the length of the array is more than 1...
            #calculates the midpoint of the array  
            m = len(scores)/2 
            m = round(m, 0)
            m = int(m)
            #sets up 2 arrays the opposite halves of the array passed in 
            scores1 = scores[0:m]
            scores2 = scores[m:]

            #calls itself on each half array
            self.sort_scores(scores1)
            self.sort_scores(scores2)

            #sets initial values to 0
            i = j = k = 0

            #WHILE i and j are less than the lengths of the half arrays 
            while i < len(scores1) and j < len(scores2):
              if scores1[i] <= scores2[j]: #if the current item in array 1 is smaller than the on in array 2...
                  scores[k] = scores1[i] #stores the current item of the final array as the item in scores1 that is in position i
                  i += 1 #increments i by one to move to next item in array 1
              else: #otherwise...
                  scores[k] = scores2[j] #stores the current item of the final array as the item in scores2 that is in position j
                  j += 1 #increments j by one to move to next item in array 2
              k += 1 #increments k by one to move to next item in final array

            #WHILE i is less than the length of the first half array  
            while i < len(scores1):
              scores[k] = scores1[i] #stores the current item of the final array as the item in scores1 that is in position i
              i += 1 #increments i by one to move to next item in array 1
              k += 1 #increments k by one to move to next item in final array

            #WHILE j is less than the length of the second half array
            while j < len(scores2):
              scores[k] = scores2[j] #stores the current item of the final array as the item in scores2 that is in position j
              j += 1 #increments j by one to move to next item in array 2
              k += 1 #increments k by one to move to next item in final array

        return scores #return the sorted scores array to the 'Main' program

    #the method to sort the names dictionary 
    def sortNames(self):
        sorted_names = sorted(self.__nameDict.items(), key=lambda x:x[1]) #the keyword method to sort a dictionary
        return sorted_names #returns the sorted dictionary (as array of tuples) to 'Main' program

    #the method to check if the score is bigger than the smallest high score
    def check_score(self, score):
        last = len(self.__scores) - 1 #calculates the last index
        names = [*self.__nameDict] #stores the keys list of the names dictionary as names
        lastName = names[last] #gets the lastName using the last index
        if float(self.__scores[last]) < score: #uses an IF statement to see if score is larger than 'scores[last]'
            self.__scores.remove(self.__scores[last]) #removes the last score from 'scores'
            del self.__nameDict[lastName] #deletes the last keys-value pair in the names dictionary
            return True #returns True to the 'Main' program
        else: #otherwise...
            return False #returns False to the 'Main' program

    #the method to add a score/name to the array/dictionary
    def add_score(self, name, score):
        self.__scores.append(score) #append the score to the 'scores' array
        self.__nameDict[name] = score #creates a new key-value pair in the dictionary
        return self.__scores #returns the scores array to the 'Main' program

    #the method to write the new high scores to a file
    def saveScore(self, fileName, sortedNames):
        for item in sortedNames: #goes through the 'sortedNames' array
            name = item[0] #gets the name as item[0]
            score = item[1] #gets the score as item[1]
            text = name+","+str(score)+"\n" #creates the text which will be written to the file
            fileName.write(text) #writes the text to the file

    def get_score(self):
        return self.__scores, self.__nameDict
