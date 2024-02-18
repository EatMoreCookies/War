from card import Card 

class Player:
    def __init__(self, name: str):
        self.__hand: list = []
        self.name = name
    
    def get_num_cards(self):
        return len(self.__hand)

    def add_card(self, card: Card):
        self.__hand.append(card)

    def add_cards(self, cards: list):
        self.__hand.extend(cards)
    
    def lay_card(self):
        item = self.__hand.pop(0)
        return item

    def get_hand(self):
        values = [str(card) for card in self.__hand]
        return ', '.join(values)
    
    def get_multiple_cards(self, number: int):
        num_cards_to_take = min(len(self.__hand) - 1, number) # minus 1 since player must always have at least one card to play
        ret = self.__hand[:num_cards_to_take]
        self.__hand[:num_cards_to_take] = []

        return ret

    def has_won(self):
        return len(self.__hand) == 52
        