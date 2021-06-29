import random

class Cards():
          def __init__(self):
                    self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

class Players():
	  def __init__(self,player1,player2):
		    self.player1 = player1
		    self.player2 = player2

	  def __str__(self):
		    return f"\nPlayer 1: {self.player1}\n Player 2: {self.player2}"

class Deck(Cards,Players):
          def __init__(self,player1,player2):
                    self.player1 = player1
                    self.player2 = player2
                    Cards.__init__(self)
                    Players.__init__(self,self.player1,self.player2)
                    self.deck = self.cards * 4
                    random.shuffle(self.deck)
                    self.half_of_deck = len(self.deck)//2
                    self.deck_p1 = self.deck[:self.half_of_deck]
                    self.deck_p2 = self.deck[self.half_of_deck:]
                    random.shuffle(self.deck_p1)
                    random.shuffle(self.deck_p2)
                    self.card1 = None
                    self.card2 = None
                    self.draw_list = []

          def draw_card(self):
                    if len(self.deck_p1) > 0 and len(self.deck_p2) > 0:   
                              self.card1 = self.deck_p1[len(self.deck_p1)-1]
                              self.card2 = self.deck_p2[len(self.deck_p2)-1]
                              Deck.display_cards(self,self.card1,self.card2)
                              Deck.check_win(self)
                    elif len(self.deck_p1) == 0:
                              print(f'\n\n\t\t\t{self.player2} WINS!!! with {len(self.deck_p2)} cards.')
                    elif len(self.deck_p2) == 0:
                              print(f'\n\n\t\t\t{self.player1} WINS!!! with {len(self.deck_p1)} cards.')
                    else:
                              pass

          def display_cards(self,c1,c2):
                    if len(self.deck_p1) > len(self.deck_p2):
                              print('\t',end='\t')
                              print('\t____________\t',end='\t\t')
                              print('\t____________\t')
                              print('\t',end='\t')
                              print('\t|\t   |\t',end='\t\t')
                              print('\t|\t   |\t')
                              print('__________',end='\t')
                              print('\t|\t   |\t',end='\t\t')
                              print('\t|\t   |\t')
                              print('__________',end='\t')
                              print(f'\t|    {c1}     |\t',end='\t\t')
                              print(f'\t|    {c2}     |\t')
                              print('__________',end='\t')
                              print('\t|\t   |\t',end='\t\t')
                              print('\t|\t   |\t',end='\t')
                              print('__________')
                              print('__________',end='\t')
                              print('\t|\t   |\t',end='\t\t')
                              print('\t|\t   |\t',end='\t')
                              print('__________')
                              print('__________',end='\t')
                              print('\t------------\t',end='\t\t')
                              print('\t------------\t',end='\t')
                              print('__________')
                    elif len(self.deck_p1) < len(self.deck_p2):
                              print('\t',end='\t')
                              print('\t____________\t',end='\t\t')
                              print('\t____________\t')
                              print('\t',end='\t')
                              print('\t|\t   |\t',end='\t\t')
                              print('\t|\t   |\t')
                              print('\t',end='\t')
                              print('\t|\t   |\t',end='\t\t')
                              print('\t|\t   |\t',end='\t')
                              print('__________')
                              print('\t',end='\t')
                              print(f'\t|    {c1}     |\t',end='\t\t')
                              print(f'\t|    {c2}     |\t',end='\t')
                              print('__________')
                              print('__________',end='\t')
                              print('\t|\t   |\t',end='\t\t')
                              print('\t|\t   |\t',end='\t')
                              print('__________')
                              print('__________',end='\t')
                              print('\t|\t   |\t',end='\t\t')
                              print('\t|\t   |\t',end='\t')
                              print('__________')
                              print('__________',end='\t')
                              print('\t------------\t',end='\t\t')
                              print('\t------------\t',end='\t')
                              print('__________')
                    else:
                              print('\t',end='\t')
                              print('\t____________\t',end='\t\t')
                              print('\t____________\t')
                              print('\t',end='\t')
                              print('\t|\t   |\t',end='\t\t')
                              print('\t|\t   |\t')
                              print('\t',end='\t')
                              print('\t|\t   |\t',end='\t\t')
                              print('\t|\t   |\t')
                              print('\t',end='\t')
                              print(f'\t|    {c1}     |\t',end='\t\t')
                              print(f'\t|    {c2}     |\t')
                              print('\t',end='\t')
                              print('\t|\t   |\t',end='\t\t')
                              print('\t|\t   |\t',end='\t')
                              print('\t')
                              print('__________',end='\t')
                              print('\t|\t   |\t',end='\t\t')
                              print('\t|\t   |\t',end='\t')
                              print('__________')
                              print('__________',end='\t')
                              print('\t------------\t',end='\t\t')
                              print('\t------------\t',end='\t')
                              print('__________')


          def check_win(self):
                    self.index1 = self.cards.index(self.card1)
                    self.index2 = self.cards.index(self.card2)
                    if self.index1 == self.index2:
                              if len(self.deck_p1) > 1 and len(self.deck_p2) > 1:
                                    print('\n\t\t\t\tDRAW MEANS WAR!!!')
                                    self.draw_list.extend([self.card1,self.card2])
                                    p1 = self.deck_p1.pop()
                                    p2 = self.deck_p2.pop()
                                    Deck.draw_card(self)

                    elif (self.index1 < self.index2):
                              if len(self.draw_list) > 0:
                                    self.draw_list.extend([self.card1,self.card2])
                                    self.deck_p2.extend(self.draw_list)
                                    p1 = self.deck_p1.pop()
                                    p2 = self.deck_p2.pop()
                                    print(f"\n{self.player2} "+'+',len(self.draw_list))
                                    self.draw_list = []
                                    
                              else:
                                    p = self.deck_p1.pop()
                                    wp = self.deck_p2.pop()
                                    self.deck_p2.reverse()
                                    self.deck_p2.extend([p,wp])
                                    self.deck_p2.reverse()
                                    print(f'\n{self.player2} +1')
                                    
                              Deck.draw_card(self)
                              
                    elif self.index1 > self.index2:
                              if len(self.draw_list) > 0:
                                    self.draw_list.extend([self.card1,self.card2])
                                    self.deck_p1.extend(self.draw_list)
                                    p1 = self.deck_p1.pop()
                                    p2 = self.deck_p2.pop()
                                    print(f"\n{self.player1} "+'+',len(self.draw_list))
                                    self.draw_list = []
                                    
                              else:
                                    p = self.deck_p2.pop()
                                    wp = self.deck_p1.pop()
                                    self.deck_p1.reverse()
                                    self.deck_p1.extend([p,wp])
                                    self.deck_p1.reverse()
                                    print(f'\n{self.player1} +1')
                                    
                              Deck.draw_card(self)

                    else:
                              pass


def game():
          p1 = input('Player 1 enter your name: ')
          p2 = input('Player 2 enter your name: ')
          pl = Players(p1,p2)
          cl = Cards()
          deck = Deck(p1,p2)
          print('Welcome\n',pl,'\nEnjoy the game "WAR!!"')
          deck.draw_card()
			  


q = ''
while q != 'N':
          game()
          q = input('\n\nDo you want to continue playing (Y/N): ')