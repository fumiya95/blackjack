
import random

CARD_VALUES = {
    'A': 1,
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
    total = 0
    ace_count = 0
    for card in cards:
        rank = card[:-1]
        if rank == 'A':
            ace_count += 1
            total += 1
        else:
            total += CARD_VALUES[rank]
    while ace_count > 0:
        if total + 10 <= 21:
            total += 10
        ace_count -= 1
    return total

def main():
    deck = create_deck()
    player_cards = [deck.pop(), deck.pop()]
    dealer_cards = [deck.pop(), deck.pop()]

    # プレイヤーターン
    while True:
        print(f"あなたのカード: {player_cards} (合計: {calculate_score(player_cards)})")
        action = input("Hit する場合は H、Stand する場合は S を入力してください: ").strip().upper()

        if action == 'H':
            player_cards.append(deck.pop())
            if calculate_score(player_cards) > 21:
                print("あなたはバーストしました！")
                break
        elif action == 'S':
            print("あなたはスタンドしました。")
            break
        else:
            print("入力が不正です。H か S を入力してください。")

    # 後ほどディーラーターンを追加する
    print("ディーラーのカード:", dealer_cards)

if __name__ == "__main__":
    main()