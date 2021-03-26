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
    for x in range(len(word)):
        for letter in lettersGuessed:
            if letter == word[x]:
                finalString.append(letter)
            else:
                finalString.append("_")
    return finalString

#return true if player wants to play again and false if not
def Game():
    selectedWord = words[random.randint(0,len(words))]
    lettersInWord = getLetters(selectedWord)
    lettersGuessed = []
    incorrectGuesses = 0
    gameStatus = True

    while gameStatus:
        letterGuessed = ""
        print(HANGMANPICS[incorrectGuesses])
        print(displayWordStatus(selectedWord,letterGuessed))

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

        #check if game over
        if incorrectGuesses == 6:
            gameStatus = False
    
    #ask to play again
    response = input("Would you like to play again? (y/n) > ")
    if response == y:
        return True
    return False

Game()


