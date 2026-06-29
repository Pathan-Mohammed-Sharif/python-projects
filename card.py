import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

values = {
    2: 2, 3: 3, 4: 4, 5: 5, 6: 6,
    7: 7, 8: 8, 9: 9, 10: 10,
    "J": 11, "Q": 12, "K": 13, "A": 14
}

while True:
    deck = cards * 4
    random.shuffle(deck)

    player = [deck.pop() for _ in range(3)]
    computer = [deck.pop() for _ in range(3)]

    input("Press Enter to draw 3 cards...")

    print("\nYour Cards:", player)
    print("Computer Cards:", computer)

    player_score = sum(values[c] for c in player)
    computer_score = sum(values[c] for c in computer)

    print("\nYour Score:", player_score)
    print("Computer Score:", computer_score)

    if player_score > computer_score:
        print("🎉 You Win!")
    elif computer_score > player_score:
        print("💻 Computer Wins!")
    else:
        print("🤝 Draw!")

    choice = input("\nPlay again? (y/n): ")
    if choice.lower() != 'y':
        print("Game Over!")
        break
