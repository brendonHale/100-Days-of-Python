import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    card = random.choice(cards)
    return card

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0

    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(11)

    return sum(hand)

def compare(player, dealer):
    if player == dealer:
        return "Draw"
    elif dealer == 0:
        return "Lose, Dealer hit BlackJack"
    elif player == 0:
        return "Win, you hit BlackJack"
    elif player > 21:
        return "Lose, you Busted"
    elif dealer > 21:
        return "Win, Dealer Busted"
    elif player > dealer:
        return "Win"
    else:
        return "Lose"

def play_game():
    print(art.logo)
    player_hand = []
    dealer_hand = []
    player_score = -1
    dealer_score = -1
    game_over = False

    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            deal = input("Type 'y' to deal another card, type 'n' to pass: ")

            if deal == "y":
                player_hand.append(deal_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    print(f"Your hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's hand: {dealer_hand}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))

while input("Do you want to play a game of BlackJack? (y/n): ") == "y":
    print("\n" * 20)
    play_game()







