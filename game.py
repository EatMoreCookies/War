from card import Card
from player import Player
import random
import time

class Game:
    def __init__(self, player1: str, player2: str, slow: bool = True, sleep_time: float = 1):
        self.__deck: list = []
        self.__suits: list = ["♥", "♠", "♣", "♦"]
        self.__player1 = player1
        self.__player2 = player2
        self.__slow = slow
        self.__sleep_time = sleep_time
        self.create_deck()
    
    def get_random_card_from_deck(self):
        # Get the current timestamp
        current_timestamp = int(time.time())

        # Use the current timestamp as the seed
        random.seed(current_timestamp)

        return random.randint(0, len(self.__deck) - 1)
    
    def create_deck(self):
        for s in self.__suits:
            for i in range(0, 13):
                self.__deck.append(Card(i, s))

    def play(self):
        player_1 = Player(self.__player1)
        player_2 = Player(self.__player2)

        while len(self.__deck) > 0:
            player_1.add_card(self.__deck.pop(self.get_random_card_from_deck()))
            player_2.add_card(self.__deck.pop(self.get_random_card_from_deck()))

        print(f'{player_1.name} has a hand of {player_1.get_hand()}')
        
        if self.__slow:
            time.sleep(self.__sleep_time)

        print(f'{player_2.name} has a hand of {player_2.get_hand()}')

        if self.__slow:
            time.sleep(self.__sleep_time)

        war = True
        pile: list = []

        while war:
            p1_card = player_1.lay_card()
            p2_card = player_2.lay_card()

            pile.append(p1_card)
            pile.append(p2_card)

            print(f'{player_1.name} laid {p1_card}')

            if self.__slow:
                time.sleep(1)

            print(f'{player_2.name} laid {p2_card}')

            if self.__slow:
                time.sleep(self.__sleep_time)

            if p1_card.value != p2_card.value:
                if p1_card.value > p2_card.value:
                    player_1.add_cards(pile)
                    print(f'{player_1.name} has taken the trick. {player_1.name} now has {player_1.get_num_cards()} cards and {player_2.name} has {player_2.get_num_cards()} cards.')
                    pile = []

                elif p2_card.value > p1_card.value:
                    player_2.add_cards(pile)
                    print(f'{player_2.name} has taken the trick. {player_2.name} now has {player_2.get_num_cards()} cards and {player_1.name} has {player_1.get_num_cards()} cards.')
                    pile = []
                
                if self.__slow:
                    time.sleep(self.__sleep_time)
            
            else:
                print("WAR!")
                pile.extend(player_1.get_multiple_cards(p1_card.value))
                pile.extend(player_2.get_multiple_cards(p2_card.value))


            if player_1.has_won() or player_2.has_won():
                war = False

                if player_1.has_won():
                    print(player_1.name + " has won!")
                else:
                    print(player_2.name + " has won!")










