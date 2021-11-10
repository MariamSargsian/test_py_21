import itertools
import random
from abc import ABC, abstractmethod


class CardABC(ABC):
    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def value(self):
        pass
    
class DeckABC(ABC):
    @abstractmethod
    def create_deck(self):
        pass

    @abstractmethod
    def shuffle(self):
        pass

class Card(CardABC):
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
            return 10


class AceCard(Card):
    ranks = ['Ace']
    def __init__(self, suit, rank):
        super().__init__(suit, rank)

    def value(self):
        if self.rank in ranks:
            return 11


class NumCard(Card):
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    def __init__(self, suit, rank):
        super().__init__(suit, rank)

    def value(self):

        return self.ranks[self.rank]


# creating Deck, shuffle function and single dealing#

class Deck(DeckABC):

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
            choice = input('Do you want to add a player ?')
            if choice == 'y':
                player = Player(input('Please enter the name of player'))
                self.number_of_players += 1
                self.users.append(player.name)
                print(f'{player.name} is added!')
                if self.number_of_players == self.max_players:
                    print('You reached maximum players')
                    break
                return self.add_player()
            elif choice == 'n':
                print('-----------------------')
                break
            else:
                print("Please enter 'y' or 'n'")
                return self.add_player()

    def initial_deal(self):
        print('Start a game')
        # Initial dealing for player and dealer
        while len(self.player_cards) != 2:

            # Randomly dealing a card
            for player in self.users:
                player_card = random.choice(self.deck)
                self.player_cards.append(player_card.pop())


        while len(self.dealer_cards) != 2:
            dealer_card = random.choice(self.deck)
            self.dealer_cards.append(dealer_card.pop())

            if len(self.dealer_cards) == 2:
                dealer_cards[1] = '| <card hidden> |'

    def check_hand(self, hand):

       v_sum = 0
       aces = 0
       for i in range(len(hand)):
            v_sum += hand[i].value()

            if hand[i].rank == 'Ace':
                aces += 1
            while v_sum > 21 and aces > 0:
                v_sum -= 10
                aces -= 1
       return v_sum

    def ask_user(self, user: Player):
        for player in self.users:
            self.player_score = self.check_hand(hand)
            while self.player_score < 21:
                choice = input('Do you want another card: (y/n)')
                if choice == 'y':
                    player_card = random.choice(self.deck)
                    player_cards.append(player_card.pop())
                    self.player_score += player_card.value()

                else:
                    return self.player_score

            if self.player_score == 21:
                print("BLACKJACK!!!you win")


            if self.player_score > 21:
                print("you bust")

    def ask_dealer(self):
        dealer_score = self.check_hand(self.dealer_cards)
        while dealer_score < 17:
            dealer_card = random.choice(self.deck)
            self.dealer_cards.append(dealer_card.pop())

            dealer_score += dealer_card.value()

            if dealer_score > 21:
                print("Dealer bust!!! You win!!!")

            if dealer_score == 21:
                print("Dealer has a BLACKJACK!!! You bust")

            if dealer_score == self.player_score:
                print("TIE GAME!!!")

            elif player_score > dealer_score:
                print("You win!!!")

            else:
                print("DEALER WINS!!!")

    def start_again(self):

            choice = input("Do you want to start again? (y/n) ")

            if (choice == 'y' or choice == 'n'):
                return choice
            else:
                print("Please enter 'y' or 'n'")
                return Game.start_again()

def main():
    def looping():
        deck = Deck()
        game = Game(deck)
        for user in game.users:
            game.ask_user(user=user)
        game.ask_dealer()
        if game.start_again():
            looping()
    looping()
    print("Thanks. Bye!")


if __name__ == "__main__":
    main()

