import random

def create_deck():
    ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    suits = ['♠','♥','♦','♣']
    deck = [rank + suit for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def main():
    deck = create_deck()

    # プレイヤーとディーラーそれぞれに2枚ずつ配る
    player_cards = [deck.pop(), deck.pop()]
    dealer_cards = [deck.pop(), deck.pop()]

    # 確認用表示
    print("プレイヤーのカード:", player_cards)
    print("ディーラーのカード:", dealer_cards)

if __name__ == "__main__":
    main()