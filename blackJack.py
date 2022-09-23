import random
from art import blackJackLogo


def deal_card():
    """The deal_card function deals with generating new random card from the list everytime it's called"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    randCard = random.choice(cards)
    return randCard


def calculate_Score(cards):
    """The calculate_Score function is responsible for calculating the all the cards in a list by checking
    whether a user or computer has blackJack or not. This function is also responsible for replacing Ace
    when its needed!"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def cardsCompare(userCards, ComputerCards):
    """The cardsCompare function compares both user cards and computer cards and print a final result!"""
    if calculate_Score(userCards) == calculate_Score(ComputerCards):
        print(f"You have {userCards}, and Score: {calculate_Score(userCards)}")
        print(f"Computer has {computer_cards}, and Score: {calculate_Score(computer_cards)}")
        print("────────────────────────────────────────────────────────────────────────")
        print("                               Its a draw")
        print("────────────────────────────────────────────────────────────────────────")

    elif calculate_Score(userCards) == 0:

        print(f"Computer has {computer_cards}, and Score: {calculate_Score(computer_cards)}")
        print("────────────────────────────────────────────────────────────────────────")
        print("                     User has BlackJack - User Wins!")
        print("────────────────────────────────────────────────────────────────────────")

    elif calculate_Score(ComputerCards) == 0:
        print(f"You have {userCards}, and Score: {calculate_Score(userCards)}")
        print(f"Computer has {computer_cards}, and Score: {calculate_Score(computer_cards)}")
        print("────────────────────────────────────────────────────────────────────────")
        print("                 Computer has BlackJack - Computer Wins!")
        print("────────────────────────────────────────────────────────────────────────")
    elif calculate_Score(userCards) > 21:
        print(f"You have {userCards}, and Score: {calculate_Score(userCards)}")
        print(f"Computer has {computer_cards}, and Score: {calculate_Score(computer_cards)}")
        print("────────────────────────────────────────────────────────────────────────")
        print("                      User Busted! - Computer Wins!")
        print("────────────────────────────────────────────────────────────────────────")
    elif calculate_Score(ComputerCards) > 21:
        print(f"You have {userCards}, and Score: {calculate_Score(userCards)}")
        print(f"Computer has {computer_cards}, and Score: {calculate_Score(computer_cards)}")
        print("────────────────────────────────────────────────────────────────────────")
        print("                      User Wins! - Computer Busted!")
        print("────────────────────────────────────────────────────────────────────────")
    elif calculate_Score(userCards) > calculate_Score(ComputerCards):
        print(f"You have {userCards}, and Score: {calculate_Score(userCards)}")
        print(f"Computer has {computer_cards}, and Score: {calculate_Score(computer_cards)}")
        print("────────────────────────────────────────────────────────────────────────")
        print("                   User Has Maximum Score - User Wins!")
        print("────────────────────────────────────────────────────────────────────────")

    elif calculate_Score(ComputerCards) > calculate_Score(userCards):
        print(f"You have {userCards}, and Score: {calculate_Score(userCards)}")
        print(f"Computer has {computer_cards}, and Score: {calculate_Score(computer_cards)}")
        print("────────────────────────────────────────────────────────────────────────")
        print("                Computer Has Maximum Score - Computer Wins!")
        print("────────────────────────────────────────────────────────────────────────")


youPlay = True

while youPlay:
    choice = input("Do you want to play black jack ( y/n ) : ")
    if choice == "y" or "Y":
        print(blackJackLogo)
        user_cards = []
        computer_cards = []
        is_game_over = False

        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        while not is_game_over:
            userScore = calculate_Score(user_cards)
            computerScore = calculate_Score(computer_cards)

            print(f"Your cards: {user_cards}, Current score: {userScore}")
            print(f"Computer's first card: {computer_cards[0]}")
            if userScore == 0 or computerScore == 0 or userScore > 21:
                is_game_over = True
            else:
                userDeals = input("Type 'y' to get another card, Type n to pass: ")
                if userDeals == "y":
                    user_cards.append(deal_card())
                    calculate_Score(user_cards)
                else:
                    is_game_over = True
        shouldPlay = True

        while shouldPlay:
            if sum(computer_cards) < 17:
                computer_cards.append(deal_card())
            else:
                shouldPlay = False

        cardsCompare(user_cards, computer_cards)
    else:
        youPlay = False
