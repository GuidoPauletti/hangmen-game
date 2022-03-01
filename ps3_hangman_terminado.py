# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    i = 0
    for letter in secretWord:
        
        result = letter in lettersGuessed
        if result == True :
            i = i + 1
    if i >= len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    show = ''
    for letter in secretWord:
        
        result = letter in lettersGuessed
        if result == True :
            show = show + letter
        else :
            show = show + '_ '
    return show


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabet_copy = alphabet[:]
    for char in alphabet:
        if char in lettersGuessed :
            alphabet_copy.remove(char)
    cadena = ''.join(alphabet_copy)
    return cadena

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    guesses_left = 8
    print ('Welcome to the game Hangman!') 
    print ('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print ('------------')
    while guesses_left > 0:
        if isWordGuessed(secretWord, lettersGuessed):
            print ('Congratulations, you won!')
            guesses_left = 0
        else:
            print ('You have ' + str(guesses_left) + ' guesses left')
            print ('Available letters: ' + getAvailableLetters(lettersGuessed))
            guess = input('Please guess a letter:' '')
            guessInLowerCase = guess.lower()
            
            if guessInLowerCase in lettersGuessed :
                print ("Oops! You've already guessed that letter:" + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
            elif guessInLowerCase in secretWord :
                lettersGuessed += guessInLowerCase
                print ('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
                
                
            else :
                lettersGuessed += guessInLowerCase
                print ('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
                guesses_left -= 1
                
    if isWordGuessed(secretWord, lettersGuessed) == False:
        print ('Sorry, you ran out of guesses. The word was ' + secretWord)
    
   





hangman(chooseWord(wordlist))

    
        


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
