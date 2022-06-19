from words import words
import random

def pick_word():
    word = random.choice(words)
    game(word)
    
def game(a_word):
    list_word = list(a_word)
    unders = list('_'*len(a_word))
    guessed_letters = []
    print(a_word)
    print("Welcome to hangman!")
    print("Your goal is to guess the word!")
    i = 0
    while i < 6:
        guessed = False
        if a_word == ''.join(unders):
            guessed = True
            print("You guessed it!")
            break
        letter = input("Guess a letter: ")
        if letter == a_word:
            print("You guessed it!")
            break
        elif letter not in guessed_letters and letter in list_word:        
            for pos, char in enumerate(list_word):
                if char == letter:
                    unders[pos] = letter
        elif letter.isspace():
            print("Invalid input.")
        elif letter not in list_word:
            i += 1
            print(f"Letter not in word, {6-i} tries remaining.")
        else:
            print('You already guessed this letter.')            
        guessed_letters.append(letter)
        print(''.join(unders))
    if not guessed and i==6:
        print(f"Word: {a_word}")

pick_word()
