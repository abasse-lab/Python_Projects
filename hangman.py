import random
import sys
#so now basically i am going to welcome them to hangman

#This will be my secret word list, gonna make it bigger
wordlist = ["christianpulisic", "kepaarrizabalaga", "callumhudsonodoi", "tammyabraham", "willian", "billygilmour", "ngolokante", "oliviergiroud", "masonmount", "jorghino", "tinoanjorin", "rubenloftuscheek", "reecejames", "armandobroja", "mateokovacic", "willycaballero", "rossbarkley", "cesarazpilicueta", "antoniorudiger", "fikayotomori", "michybatshuayi", "andreaschristensen", "kurtzouma"]
guess_word = []
secretword = random.choice(wordlist)
len_word = len(secretword)
alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwYyXxZz"
letter_storage = []

def beginning():
    print("Welcome to the amazing hangman game" + "\n" + 
    "I really hope you enjoy this game" + '\n' + 
    "How to play:" 
    "One player thinks of a word or phrase;" + '\n' + 
    "the others try to guess what it is one letter at a time." + '\n' + 
    "The player draws a number of dashes equivalent to the number of letters in the word." + '\n' + 
    "If a guessing player suggests a letter that occurs in the word," + '\n' + 
    "the other player fills in the blanks with that letter in the right places"+ '\n' +
    "Do you want to continue playing this game?\n")

    while True:
        name = input('Please enter your name\n')
        if name == '':
            print("enter a name please!")
        else:
            break
beginning()
#what we need now is if the word is equal to what we have on list we say congrats hun

def ask_player_to_play():
    print("Excellent!")
    while True:
        choice = input('Please enter yes or no if you would like to play!\n')
        if choice == 'yes' or choice == 'YES':
            break
        elif choice == 'NO' or choice == 'no':
            sys.exit('You are missing out, hope to see you again!!')
        else:
            print('Answer yes or no please\n')
            continue
ask_player_to_play()

def giving_secretword():
    for char in secretword:
        guess_word.append('-')
    print('the word has', len_word, 'characters')
    print(guess_word)
def guessing():
    guess_taken = 1
    while guess_taken < 10:
        guess = input("Pick a letter\n").lower()
        if not guess in alphabet:
            print("Enter a letter from a-z alphabet")
        elif guess in letter_storage:
            print("You have already guessed that letter!")
        else:
            letter_storage.append(guess)
            if guess in secretword:
                print(' You guessed correctly!')
                for x in range(0, len_word):
                    if secretword[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)
                if not '-' in guess_word:
                    print('You Won!')
                    print(guess_word)
                    break
            else:
                print('The letter is not in the word. Try Again!')
                guess_taken += 1
                if guess_taken == 10:
                    print('Sorry mate you lose')

giving_secretword()
guessing()
print('Game over!')
