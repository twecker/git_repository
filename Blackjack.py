

class Player(object):
	def __init__(self, hand = [], bankroll = 10000):
		self.hand = hand
		self.bankroll = bankroll

	def hit(self, hands):
		pass

class Hand(object):
	def __init__(self, cards):
		self.cards = cards



class Card(object):
	def __init__(self, suit, rank, value = 0):
		self.suit = suit
		self.rank = rank
		if not self.rank.isalpha():
			self.value = int(self.rank)
		elif self.rank == "Ace":
			self.value = 11
		else:
			self.value = 10
	def __str__(self):
		return '%s %s' % (self.rank, self.suit)
	def __repr__(self):
		return self.__str__()


class Dealer(object):
	def __init__(self, hand = []):
		self.hand = hand
import random


class Deck(object):
	pips = ['2','3','4','5','6','7','8','9','10', 'Jack','Queen','King','Ace']
	suits = ['♠', '♦', '♥', '♣']
	def __init__(self, cards = []):
		self.cards = cards
	def __str__(self):
		for m in self:
			return m
	def add_cards(self):
		pips = ['2','3','4','5','6','7','8','9','10', 'Jack','Queen','King','Ace']
		suits = ['♠', '♦', '♥', '♣']
		for i in suits:
			for x in pips:
				self.cards.append(Card(suit = i, rank = x))
	def shuffle(self):
		random.shuffle(self.cards)


class Shoe(object):
	def __init__(self, decks = 1):
		self.decks = decks


def value(hand):
	total = 0
	for i in hand:
		total += i.value
	return total

def deal(person, deck, times):
	for i in range(times):
		x = deck.pop()
		person.hand.append(x)

def game(w, player):
	bet = int(raw_input("Place your bet "))
	if bet == player.bankroll:
		print "Go big or go home, eh?"
		print " "

	player_bust = False
	dealer_bust = False
	
	dealer = Dealer()
	dealer.hand = []
	player.hand = []
	deal(player, w.cards, 2)
	deal(dealer, w.cards, 2)

	if value(player.hand) == 21:
		print player.hand
		print "Blackjack!"
		player.bankroll += (2 * bet)
		player.hand = []
		dealer.hand = []
		return


	print "the dealer shows the %s " % (dealer.hand[0])
	keep_playing = True
	print "your hand is %s" % (player.hand)
	print "with a value of %s" % (value(player.hand))


	while keep_playing:
		m = raw_input("Action ")
		if m == "hit" or m == "Hit":
			deal(player, w.cards, 1)
		elif m == 'double down' or m =='double':
			deal(player, w.cards, 1)
			bet = bet * 2
			keep_playing = False
		else:
			keep_playing = False
		if value(player.hand) > 21:
			for i in player.hand:
				if i.rank == "Ace":
					i.value == 1
		print "your hand is %s" % (player.hand)
		if value(player.hand) > 21:
			for i in player.hand:
				if i.rank == "Ace":
					i.value == 1
		print "with a value of %s" % (value(player.hand))
		if value(player.hand) > 21:
			player_bust = True
			keep_playing = False



	while value(dealer.hand) < 17:
		deal(dealer, w.cards, 1)
		for card in dealer.hand:
			if card.rank == 'Ace':
				if value(dealer.hand) > 21:
					card.value = 1
				else:
					card.value = 11
		if value(dealer.hand) > 17:
			dealer_playing = False

		


			
	print " "
	print " "
	print "The dealer holds a hand of %s" % (dealer.hand)
	print "with a value of %s" % (value(dealer.hand))
	print " "
	print "you hold a hand of %s" % (player.hand)
	print "with a value of %s" % (value(player.hand))
	print " "
	
	if player_bust == True:
		print "Tough Luck, You've Busted"
		print "You Loose $%s" % (bet)
		player.bankroll -= bet
		player.hand = []
		dealer.hand = []
		return
		
	if value(dealer.hand) > 21:
		print "The House Busts, Here's Your Money"
		print "You Gain $%s" % (bet)
		player.bankroll += bet
		player.hand = []
		dealer.hand = []
		return
		
	if value(player.hand) > value(dealer.hand):
		print "Well played" 
		print "You Gain $%s" % (bet)
		player.bankroll += bet
	if value(player.hand) == value(dealer.hand):
		print "Let's call this one a draw"
		print "Your Bet of $%s is Returned to You" % (bet)
	if value(player.hand) < value(dealer.hand):
		print "Looks like you've lost this one"
		print "You Loose $%s" % (bet)
		player.bankroll -= bet
	player.hand = []
	dealer.hand = []




def play_a_round():
	w = Deck()
	w.add_cards()
	w.shuffle()
	player = Player()
	while player.bankroll > 0:
		l = raw_input("You currently hold $%s, would you like to play? " % (player.bankroll))
		print ' '
		if l == 'yes' or l == 'Yes':
			game(w, player)
		elif l == "No" or l =="no":
			print "You've ended with $%s" % (player.bankroll)
			return
		else:
			break
	print "you've run out of money"




play_a_round()





