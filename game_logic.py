import random
from decouple import config

class CasinoGame:
    def __init__(self):
        self.player_money = int(config('MY_MONEY',default = 1000))
        self.winning_slots = list(range(1, 11))

    def play_round(self, bet_amount, chosen_slot):
        winning_slot = random.choice(self.winning_slots)
        if chosen_slot == winning_slot:
            self.player_money += bet_amount
            return f"Congratulations! You won ${bet_amount * 2}!"
        else:
            self.player_money -= bet_amount
            return "Sorry, you lost."

    def is_game_over(self):
        return self.player_money <= 0

    def get_player_money(self):
        return self.player_money
