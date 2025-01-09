# Deck Class 
import random 
from Card import * 

class Deck ():
        SUIT_TUPLE = ('Diamonds', 'Clubs', 'Hearts', "Spades")
        # This dict maps each card ranl tp a value for a standard deck
        STANDARD_DICT = {'Ace':1, '2':2, '3': 3, '4':4, '5':5, '6':6, '7': 7, '8':8, '9':9, '10':10 , 'Jack':11, 'Queen': 12, 'King':13}

        def _init_(self, window, rankValueDict=STANDARD_DICT): 
            # rankValueDict defaults to STANDARD_DICT, but you can call it with a different dict, e.g., a special Dict for Blackjack
            self.startingDeckList = []
            self.playingDeckList = [] 
            for suit in Deck.SUIT_TUPLE: 
                for rank, value in rankValueDict.items(): 
                    oCard = Card(window, rank, suit, value)
                    self.startingDeckList.append(oCard)

            self.shuffle()
        
        def shuffle(self):
            #Copy the starting deck and save it in the playing deck list
            self.playingDeckList = self.startingDeckList.copy()
            for oCard in self.playingDeckList(): 
                oCard.conceal()
            random.shuffle(self.playingDeckList)
        
        def getCard(self): 
            if len(self.playingDeckList) == 0: 
                    raise IndexError('No More Cards')
                # Pop one card off the deck and return it 
        def returnCardToDeck(self,oCard): 
            # Put a card back into the deck
            self.deckList.insert(0 , oCard)
        
