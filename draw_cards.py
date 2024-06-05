# Import random package
import random
import sys

# Create deck of cards
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
values = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
cards = []
shuffled_cards = []

## Function that creates standard deck of cards
def populate_deck():
    cards.clear()
    i = 0
    j = 0
    while i < 4:
        while j < 13:
            card = [values[j], suits[i]]
            cards.append(card)
            j += 1
        i += 1
        j = 0
## Shuffles cards
def shuffle_deck():
    populate_deck()
    random.shuffle(cards)

# Picks a card if user types 'Y', exits if 'N'.
def draw_card():
    choice = input('Draw a card? (Y/N): ')
    if choice == 'y' or choice == 'Y':
        draw = cards.pop()
    elif choice == 'n' or choice == 'N':
        print('Ok, bye.')
        sys.exit()
    return draw

# Returns a boolean for if two cards equal each other.
def card_check(card1, card2):
    check = False
    if card1 == card2:
        check = True
    return check

def main():
    draws = 0
    game_over = False

    shuffle_deck()
    secret_card = cards[random.randint(0, 51)]
    print('I\'m thinking of a card...')

    while game_over == False:
        card = draw_card()
        if card_check(card, secret_card) == False:
            print('You drew the ' + card[0] + ' of ' + card[1] + '. That\'s not it, try again!')
            draws += 1
        elif card_check(card, secret_card) == True:
            print('You drew the ' + card[0] + ' of ' + card[1] + '. You got it!')
            draws += 1
            game_over = True
    
    if game_over == True:
        print('You drew ' + str(draws) + ' times.')
        again = input('Play again? (Y/N): ')
        if again == 'y' or again == 'Y':
            main()
        elif again == 'n' or again == 'N':
            print('Ok, bye.')
            sys.exit()

main()

    


