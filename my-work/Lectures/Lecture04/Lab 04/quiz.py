import re

regex = "^Hello [A-Z]"
filename = "./datafiles/quiz.txt"

with open(filename) as quizFile:
    for line in quizFile:
        searchResult = re.search(regex, line)
        if (searchResult):
            matchingLine = line
            # I set the end to blank because each line will already have a \n
            print (matchingLine, end="")