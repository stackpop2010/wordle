"""
Makes a wordle type game. I tried limmiting guesses to words in the dictionary to keep a user from guessing something like
'aeiou' or gibberish. However, was frequently getting error that a word that was in my dictionary was not.
"""

from wordbank import words
import random

secret_word = random.choice(words)

#print(secret_word)
my_guess = ["[ ]","[ ]","[ ]","[ ]","[ ]"]

print("Welcome the totally not Wordle clone.\n"
      "Guess a 5 letter word (no numbers or symbols). \n"
      "The word may end in an 'S' - but there are very few plural words.\n"
      "There are a limited number of proper nouns.\n"
      "If your guess has a * after it, you have guessed a letter in the word, but not in that spot.\n"
      "If your guess is lower case, it is not in the word.\n"
      "If your guess is upper case with no symbols, it is the correct letter for that spot!\n"
      "Have fun! :)")

def guesser(guess, n = None):
    if n == None:
        n = 1

    guess1=input("guess a 5 letter word: ")
    guess1 = guess1.upper()
    if len(guess1) != 5:
        guess1=input("Please choose a 5 letter word with only letters")
    #if len(guess1) not in words:
        #guess1=input("That word is not in our dictionary, please try again")

    if str(guess1) == secret_word:
        return "You Win!"
    elif str(guess1) != secret_word and n >5:
        return ("You Lose, the word was:", secret_word)

    for i in range(0, len(guess1)):
        if guess1[i] == secret_word[i]:
            my_guess[i] = guess1[i]
        if guess1[i] in secret_word and guess1[i] not in secret_word[i]:
            j = (guess1[i]) + "*"
            my_guess[i] = j
        if guess1[i] not in secret_word:
            k = (guess1[i]).lower()
            my_guess[i] = k
    print(my_guess)
    n += 1
    return guesser(my_guess, n)

print(guesser(my_guess))