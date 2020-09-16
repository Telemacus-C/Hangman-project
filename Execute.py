Fullhangman = '          __________________________________\n            |                           |\n           _|_                          |\n          |   |                         |\n          \ | /                        /|\n            |                         / |\n            |                        /  |\n          /   \                     /   |\n                                   /    |\n                                  /     |\n                                 /      |\n                                /       |\n                               /        |\n----------------------------- / ------- | ---'


import random


print('easy')
print('medium')
print('hard')
print('very hard')
userinput = input("select a difficulty from those provided: ")

if userinput == 'easy':
    wordList = open('easy.txt','r')
    print(wordList)
elif userinput == 'medium':
    wordList = open('medium.txt', 'r')
    print(wordList)
elif userinput == 'hard':
    wordList = open('hard.txt', 'r')
    print(wordList)
elif userinput == 'very hard':
    wordList = open('veryHard.txt', 'r')
    print(wordList)
else:
    print('incorrect input')

wordCount = 0
words =[]
for word in wordList:
    #print(word, wordCount)
    words.append(word)
    wordCount += 1

print(words)

randomNumber = (random.randint(0, wordCount - 1))

chosenWord = (words[randomNumber].strip()).lower()
print(randomNumber, chosenWord)

blankWord = ''
for i in chosenWord:
    blankWord = str(blankWord) + '_'
print(blankWord)

failedGuesses = ""
attemptsLeft = 6
while attemptsLeft != 0:
    if blankWord.find("_") == -1:
        print("You won! :)")
        break
    guess = input("enter your letter guess: ")
    if chosenWord.find(guess) == -1:
        attemptsLeft = attemptsLeft - 1
        print('Failed guess, attemps left : ' + str(attemptsLeft))
        failedGuesses = failedGuesses + guess
        print('failed guess list: ' + str(failedGuesses))
    if not chosenWord.find(guess) == -1:
        startI = 0
        endI = len(chosenWord) - 1
        while not chosenWord.find(guess, startI) == -1:
            foundI = chosenWord.find(guess, startI)
            # print(dashes[0:foundI -1])
            blankWord = blankWord[0:foundI] + guess + blankWord[foundI + 1:]
            startI = foundI + 1
        if len(chosenWord[startI:]) == 0:
            startI = startI - 1
        print(blankWord)
print('You lost. :(')
print(Fullhangman)
