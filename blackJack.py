import random


def deal_card():

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    randCard = random.choice(cards)
    return randCard


def calculate_Score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def cardsCompare(userCards, ComputerCards):
    if calculate_Score(userCards) == calculate_Score(ComputerCards):
        print(f"You have {userCards}, and Score: {calculate_Score(userCards)} - Its a draw")
        print(f"Computer has {computer_cards}, and Score: {calculate_Score(computer_cards)}")
    elif calculate_Score(userCards) == 0:
        print(
            f"Computer has {computer_cards}, and Score: {calculate_Score(computer_cards)} - User has BlackJack - User "
            f"Wins!")
    elif calculate_Score(ComputerCards) == 0:
        print(f"You have {userCards}, and Score: {calculate_Score(userCards)}")
        print(
            f"Computer has {computer_cards}, and Score: {calculate_Score(computer_cards)} - Computer has BlackJack - "
            f"Computer Wins!")
    elif calculate_Score(userCards) > 21:
        print(f"You have {userCards}, and Score: {calculate_Score(userCards)} - User Busted!")
        print(f"Computer has {computer_cards}, and Score: {calculate_Score(computer_cards)} - Computer Wins!")
    elif calculate_Score(ComputerCards) > 21:
        print(f"You have {userCards}, and Score: {calculate_Score(userCards)} - User Wins!")
        print(f"Computer has {computer_cards}, and Score: {calculate_Score(computer_cards)} - Computer Busted!")
    elif calculate_Score(userCards) > calculate_Score(ComputerCards):
        print(f"You have {userCards}, and Score: {calculate_Score(userCards)} - User Wins!")
        print(f"Computer has {computer_cards}, and Score: {calculate_Score(computer_cards)}")

    elif calculate_Score(ComputerCards) > calculate_Score(userCards):
        print(f"You have {userCards}, and Score: {calculate_Score(userCards)}")
        print(f"Computer has {computer_cards}, and Score: {calculate_Score(computer_cards)} - Computer Wins!")


youPlay = True

while youPlay:
    choice = input("Do you want to play black jack(Y/N) : ")
    if choice == "y" or "Y":
        user_cards = []
        computer_cards = []
        is_game_over = False

        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        while not is_game_over:
            userScore = calculate_Score(user_cards)
            computerScore = calculate_Score(computer_cards)

            print(f"Your Cards: {user_cards}, current score: {userScore}")
            print(f"Computer's First card: {computer_cards[0]}")
            if userScore == 0 or computerScore == 0 or userScore > 21:
                is_game_over = True
            else:
                userDeals = input("Type y to get another card, type n to pass: ")
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
