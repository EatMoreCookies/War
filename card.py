class Card:
    def __init__(self, value: int, suite: str):
       self.value = value
       self.suite = suite
    
    def __str__(self):
        return str(self.value) + " of " + self.suite