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

    # ディーラーターン
    player_score = calculate_score(player_cards)
    print(f"ディーラーのカード: {dealer_cards} (合計: {calculate_score(dealer_cards)})")

    if player_score <= 21:
        while calculate_score(dealer_cards) < 17:
            dealer_cards.append(deck.pop())

    dealer_score = calculate_score(dealer_cards)
    print(f"ディーラーのカード最終: {dealer_cards} (合計: {dealer_score})")

    # 勝敗判定
    if player_score > 21:
        print("あなたの負けです…")
    else:
        if dealer_score > 21:
            print("ディーラーがバースト！ あなたの勝ちです！")
        else:
            if player_score > dealer_score:
                print("あなたの勝ちです！")
            elif player_score < dealer_score:
                print("あなたの負けです…")
            else:
                print("引き分けです。")

if __name__ == "__main__":
    main()