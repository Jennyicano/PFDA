# Quiz program that reads a file and prints out the lines that match the regex

import re

regex = "^$"

filename = "./quiz.txt"

with open(filename) as quizFile:
    for line in quizFile:
        searchResult = re.search(regex, line)
        if (searchResult):
            matchingLine = line
              # I set the end to blank because each line will already have a \n
            print (matchingLine, end="")
            
  
# Results  
# Input regex: hello = Output: hello
# Input regex: Hello = Output: Hello, Hello World, Hello mary
# Input regex: ^Hello = Output: Hello, Hello World
# Input regex: ^Hell*o = Output: Hello, Hello World, Hello John, Helllllllllllo Anamaniacs
# Input regex: ^Hell+o = Output: Hello, Hello World, Helllllllllllo Anamaniacs
# Input regex: ^Hell?o = Output: Hello, Hello World, Hello John
# Input regex: ^hello [A-Z] = Output: none 
# Input regex: ^Hello [A-Z] = Output: Hello World 
# Input regex: "=" = Output: var = 123  
# Input regex: "#" = Output: change this #this will change
# Input regex: "[" = Output: error 
# Input regex: "^$" = Output: none
