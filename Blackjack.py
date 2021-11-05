import random


class Card:
    suits = ('♠', '♣', '♥', '⬥')
    ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace')

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f'| {self.suit} of {self.rank} |'

    def value(self):
        pass

class FaceCard(Card):

    ranks = ['Jack', 'Queen', 'King']

    def __init__(self, suit, rank):
        super().__init__(suit, rank)

    def value(self):
        if self.rank in ranks:
            return (10,10)


class AceCard(Card):
    ranks = ['Ace']
    def __init__(self, suit, rank):
        super().__init__(suit, rank)

    def value(self):
        if self.rank in ranks:
            return (1,11)


class NumCard(Card):
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    def __init__(self, suit, rank):
        super().__init__(suit, rank)

    def value(self):

        return self.ranks[self.rank]


# creating Deck, shuffle function and single dealing#

class Deck:

    def __init__(self):
        self.deck = []
        self.create_deck()

    def create_deck(self):

        d1 = []
        for suit in FaceCard.suits:
            for rank in FaceCard.ranks:
                d1.append(Card(suit, rank))
        d2 = []
        for suit in NumCard.suits:
            for rank in NumCard.ranks:
                d2.append(NumCard(suit, rank))
        d3 = []
        for suit in AceCard.suits:
            for rank in AceCard.ranks:
                d2.append(AceCard(suit, rank))

        self.deck = d1 + d2 + d3
        return self.deck

    def shuffle(self):
       random.shuffle(self.deck)
       return self.deck

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Player(object):

    def __init__(self, name):
        self.name = name
        self.hard = 0
        self.soft = 0
        self.hand = 0
        self.win = 0

    def __repr__(self):
        return f'{self.name} {self.hand}'

class Game(object):

    max_players = 8

    def __init__(self, deck):
        self.deck = deck
        self.number_of_players = 0
        self.dealer = 0
        self.users = []
        self.player_cards = []
        self.dealer_cards = []
        self.player_score = 0
    def add_player(self):
        while self.number_of_players < self.max_players:
            ans = input('Do you want to add a player ?')
            if ans == 'y':
                player = Player(input('Please enter the name of player'))
                self.number_of_players += 1
                self.users.append(player.name)
                print(f'{player.name} is added!')
                if self.number_of_players == self.max_players:
                    print('You reached maximum players')
                    break
                return self.add_player()
            elif ans == 'n':
                print('-----------------------')
                break
            else:
                print("Please enter 'y' or 'n'")
                return self.add_player()

    def initial_deal(self):
        print('Start a game')
        # Initial dealing for player and dealer
        while len(player_cards) != 2:

            # Randomly dealing a card
            for player in self.users:
                player_card = random.choice(self.deck)
                self.player_cards.append(player_card)
                self.deck.remove(player_card)

        while len(dealer_cards) != 2:
            dealer_card = random.choice(deck)
            self.dealer_cards.append(dealer_card)
            self.deck.remove(dealer_card)
            if len(dealer_cards) == 2:
                print('The cards dealer has are X ', dealer_cards[1])

    def check_hand(self, hand):
        self.hand = hand
