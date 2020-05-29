
import random

#WELCOMING MESSAGE + HOW TO PLAY

money = 100
print('WELCOME TO CASINO MAYHEM\n')
print("The rules are pretty simple:\n In this game there are 4 mini casino games for you to handle.\n You will start off with a set balance of €100.\n You will place appropriate bets for each mini casino game in conjuction to how much money you have available to you.")
print('\n If you place a bet that is out of your balance range you will automatically lose.\n If you place a bet that is less than 1 euro you lose aswell.\n At the end we will now compare your balance to see if you won the game overall.')
print('\n If your balance is more than €150 at the end then well done you win.\n If your balance is less than 150 euro then you lose.\n')
print('\nGoodluck to you!\n')
name = input("Please Enter your Username: \n")
print("\nHello {} hope everything is well with you!\n".format(name))
print("\nYou will start off with a balance of €{}\n".format(money))

#Write CASINO MAYHEM FUNCTION HERE!
def flipping_coin(guess, bet):
    if bet > money:
        print("You dont have enough money to place a bet that high\n you have €{} left".format(money))
        return 0

    if bet < 1:
        print("You cant bet less than a dollar")
        return 0

    print("You have €{} and you placed a bet on {}".format(money, guess))
    coinflip = random.randint(1, 2)

    if coinflip == 1:
        coinflip = 'heads'

    if coinflip == 2:
        coinflip = 'tails'

    if coinflip == guess:
        new_money = money + bet
        print("Winner: {}!".format(guess,))
        return bet
    else:
        new_money = money - bet
        print("You lost! your coin flip resulted in {}".format(guess,))
        return -bet

def chohan(guess, bet):
    dice1 = random.randint(1,7)
    dice2 = random.randint(1,7)
    total = dice1 + dice2

    if bet > money:
        print("You dont have enough money to place a bet that high\n you have €{} left".format(money))
        return 0

    if bet < 1:
        print("You cant bet less than a dollar")
        return 0

    if total % 2 == 0 and guess == 'even':
        new_money = money + bet
        print("You lucky man! you are right it's Even! Your Cash Total: €{}".format(new_money))
        return bet

    elif total % 2 == 1 and guess == 'odd':
        new_money = money + bet
        print("You lucky man! you are right it's Odd! Your Cash Total: €{}".format(new_money))
        return bet

    elif total % 2 == 0 and guess != 'even':
        new_money = money - bet
        print("You lost since you said {}, your balance is €{}".format(guess, new_money))
        return -bet

    elif total % 2 == 1 and guess != 'odd':
        new_money = money - bet
        print("You lost since you said {}, your balance is €{}".format(guess, new_money))
        return -bet

def cards(bet):
    deck_of_cards = [1,2,3,4,5,6,7,8,9,'jack','queen','king']
    deck_of_cards *= 4
    player1 = random.choice(deck_of_cards)
    computer = random.choice(deck_of_cards)
    print('Hi {} your card is {}'.format(name, player1))
    print('The computer picked {}'.format(computer))

    if bet > money:
        print("You dont have enough money to place a bet that high")
        return 0

    if bet < 1:
        print("You can't bet less than a dollar")
        return 0

    if player1 == 'jack':
        player1 = 10

    elif player1 == 'queen':
        player1 = 11

    elif player1 == 'king':
        player1 = 12

    if computer == 'jack':
        computer = 10

    elif computer == 'queen':
        computer = 11

    elif player1 == 'king':
        computer = 12

    if player1 > computer:
        new_money = money + bet
        print('You won €{}'.format(bet))
        return bet

    elif player1 < computer:
        new_money = money - bet
        print('You lost €{}'.format(str(bet)))
        return -bet

    elif player1 == computer:
        print("It's a tie")
        return 0

    else:
        return 0

def roulette(bet):
    zero = [0]
    red = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
    black = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
    computer = random.randint(0,37)
    player1 = input('Please pick red or black\n')

    if bet > money:
        print("You dont have enough money to place a bet that high\n you have €{} left".format(money))
        return 0

    if bet < 1:
        print("You cant bet less than a dollar!")
        return 0

    if player1 == 'red' and computer in black:
        print('You lose! your guess was in red and the computer picked {}, which is in black!!'.format(computer))
        new_money = money - bet
        return -bet

    elif player1 == 'black' and computer in red:
        print('You lose! your guess was in black and the computer picked {}, which is in red!!'.format(computer))
        new_money = money - bet
        return -bet

    elif player1 == 'red' and computer in zero:
        print('You lose! your guess was in red and the computer picked {}, which is an automatic loss!!'.format(computer))
        new_money = money - bet
        return -bet

    elif player1 == 'black' and computer in zero:
        print('You lose! your guess was in black and the computer picked {}, which is an automatic loss!!'.format(computer))
        new_money = money - bet
        return -bet

    elif player1 == 'red' and computer in red:
        print('You lucky chap you win! your guess was in red and the computer picked {}, which is red!!'.format(computer))
        new_money = money + bet
        return bet

    elif player1 == 'black' and computer in black:
        print('You lucky chap you win! your guess was in black and the computer picked {}, which is in black!!'.format(computer))
        new_money = money + bet
        return bet

#Calling my CASINO MAYHEM functions here
print('Welcome to Coin flip!\n')
print("Rules:\n you will be asked to guess heads or tails.\n You will then place your bet!")
money += flipping_coin(input('Please guess heads or tails?\n'), int(input('Please place an appropriate bet thats within your range. \n')))
print('Balance: {}\n'.format(money))


print('Welcome to Chohan!\n')
print("Rules:\n There will be two virtual dice that will be rolled, Whatever the outcome of the 2 dices are, it will then be added together to form a total\n You are now told to guess if the total of the two dices is odd or even\n You will then place your bet!")
money += chohan(input('Please guess odd or even?\n'), int(input('Please place an appropriate bet thats within your range. \n')))
print('Balance: {}\n'.format(money))


print('Welcome to Highest Card \n')
print("Rules:\n This game is totally simulated by the computer,\n In this game you will be assigned to a computer that is playing with another computer.\n There will be a list of poker cards and the both computer will pick cards from the list at random.\n The computer with the highest playing card in value wins!")
money += cards(int(input('Please place an appropriate bet thats within your range. \n')))
print('Balance: {}\n'.format(money))


print('Welcome to Roulette \n')
print("Rules:\n Roulette is a game which consists of a big wheel and a ball.\n The big wheel will have a certain amount of numbers that will be red and another amount that will be black.\n You will be asked to pick red or black. If the ball stops and your assigned colour that you picked, you win!, If not you lose!\n You automatically lose the amount you bet if your ball stops at zero!")
money += roulette(int(input('Please place an appropriate bet thats within your range. \n')))
print('Balance: {}\n'.format(money))


#TO SEE IF YOU WIN CASINO MAYHEM OVERALL
if money >= 150:
    print('Congratulations on completing CASINO MAYHEM and coming out victories!\n I hope to see you next time {}'.format(name))
else:
    print('Well done for completing CASINO MAYHEM but your balance is less than €150 since its {}.\n Better luck next time {}!'.format(money, name))
