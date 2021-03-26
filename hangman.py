import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
YOU LOST!''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

#returns an array of letters contained in a word
def getLetters(word):
    wordContains = []
    for letter in word:
        if letter in wordContains:
            continue
        wordContains.append(letter)
    return wordContains

#display correctly guessed letters and underscores
def displayWordStatus(word,lettersGuessed):
    finalString = ""
    #if guessed letters is empty then fill with _
    if len(lettersGuessed) == 0:
        for z in range(len(word)):
            finalString += "_ "
        return finalString
    
    for x in range(len(word)):
        for y in range(len(lettersGuessed)):
            if lettersGuessed[y] == word[x]:
                finalString += lettersGuessed[y] + " "
                break
            elif y == len(lettersGuessed)-1:
                finalString += "_ "

    return finalString

def checkWin(word,lettersGuessed,lettersInWord):
    result = False
    correctLetters = 0

    if len(lettersGuessed) == 0:
        return result
    
    for x in range(len(word)):
        for y in range(len(lettersGuessed)):
            if lettersGuessed[y] == word[x]:
                correctLetters += 1
                break
    
    if correctLetters == len(lettersInWord):
        result = True

    return result

#return true if player wants to play again and false if not
def Game():
    selectedWord = words[random.randint(0,len(words))]
    lettersInWord = getLetters(selectedWord)
    lettersGuessed = []
    incorrectGuesses = 0
    gameStatus = True

    while gameStatus:
        letterGuessed = ""
        print(selectedWord+HANGMANPICS[incorrectGuesses])
        print(displayWordStatus(selectedWord,lettersGuessed))
        print("Guessed Letters: " + str(lettersGuessed))

        letterGuessed = input("Enter a letter > ").lower()


        #check correct guess
        if letterGuessed in lettersInWord:
            lettersGuessed.append(letterGuessed)
            continue
        #check if letter has already been guessed
        elif letterGuessed in lettersGuessed:
            print("letter has already been guessed!")
            continue
        #if none of these then it was a wrong guess
        else:
            lettersGuessed.append(letterGuessed)
            incorrectGuesses += 1

        #check if game won
        won = checkWin(selectedWord,lettersGuessed,lettersInWord)
        if won == True:
            print("Congratulations you won! The word was " + selectedWord)
            gameStatus = False
        elif incorrectGuesses == 6:
            print("Sorry, you lost. The word was " + selectedWord)
            gameStatus = False
    
    #ask to play again
    response = input("Would you like to play again? (y/n) > ").lower()
    if response == "y":
        return True
    return False

Game()
