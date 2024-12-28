import random

# カードの値を管理する辞書
CARD_VALUES = {
    'A': 1,  # Aは1として計算し、後から必要に応じて+10する
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10, 'K': 10
}

def create_deck():
    ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    suits = ['♠','♥','♦','♣']
    deck = [rank + suit for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def calculate_score(cards):
    """
    手札のスコアを計算して返す。
    A は 1 または 11 として、21 を超えない範囲で高い方を選ぶ。
    """
    total = 0
    ace_count = 0

    for card in cards:
        rank = card[:-1]  # 末尾のマークを除いた部分がランク
        if rank == 'A':
            ace_count += 1
            total += 1  # ひとまず1点として足す
        else:
            total += CARD_VALUES[rank]

    # A を 11 として扱えるかをチェック
    while ace_count > 0:
        if total + 10 <= 21:
            total += 10
        ace_count -= 1

    return total

def main():
    deck = create_deck()
    player_cards = [deck.pop(), deck.pop()]
    dealer_cards = [deck.pop(), deck.pop()]

    print("プレイヤーのカード:", player_cards)
    print("ディーラーのカード:", dealer_cards)

    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    print("プレイヤーのスコア:", player_score)
    print("ディーラーのスコア:", dealer_score)

if __name__ == "__main__":
    main()