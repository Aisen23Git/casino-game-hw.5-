from game_logic import CasinoGame

def main():
    game = CasinoGame()

    while not game.is_game_over():
        print(f"Your current balance: ${game.get_player_money()}")
        bet_amount = int(input("Place your bet: "))
        chosen_slot = int(input("Choose a slot to bet on (1-10): "))
        print(game.play_round(bet_amount, chosen_slot))

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Game over.")
    if game.get_player_money() > int(config('MY_MONEY')):
        print("You're in profit!")
    else:
        print("You're in loss.")

if __name__ == "__main__":
    main()
