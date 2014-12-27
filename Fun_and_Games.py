import random

class Card(object):
# Card object, contains suit and type fields
	def __init__(self):
		self.suit = ''
		self.type = ''
		
	def getName(self):
		return self.type + ' of ' + self.suit
		
def genDeck(jokerNum):
# Generates a deck of cards w/a given number of Jokers
	deck = []
	suits = ['diamonds', 'hearts','spades', 'clubs']
	types = ['two', 'three', 'four',
                 'five', 'six', 'seven',
                 'eight', 'nine', 'ten', 'jack',
                 'queen', 'king', 'ace']
	for s in suits:
		for t in types:
			tempCard = Card()
			tempCard.suit = s
			tempCard.type = t
			deck.append(tempCard)
	
	for i in range(0, jokerNum):
		tempJoker = Card()
		tempJoker.suit = s
		tempJoker.type = t
		deck.append(tempCard)
	return deck

def draw(deck):
# Removes a card from the deck and returns name
        return deck.pop().getName()

def flipCoin():
# Randomly returns heads or tails (50/50 chance)
        return random.choice(['heads', 'tails'])
        
