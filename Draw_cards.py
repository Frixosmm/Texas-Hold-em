import random
class Card:
    def __init__ (self):
        self.value=random.randint(2,14)
        self.suit=random.randint(1,4)
        self.combo=(self.value,self.suit)

        
def Draw_cards(number):
    played_cards=[(0,0)]
    while len(played_cards) !=number+1:
        new_card=Card()
        
        if new_card.combo not in played_cards:  
            played_cards.append((new_card.value,new_card.suit))
    return played_cards[1:]
