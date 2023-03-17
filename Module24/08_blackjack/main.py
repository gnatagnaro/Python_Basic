import random

NUM_CARDS = [str(n) for n in range(2, 11)]
PICT_CARDS = ['Валет', 'Дама', 'Король', 'Туз']
MAX_SUM = 21


class Deck:
    def __init__(self):
        self.card_list = []

    def __add__(self, right):
        tmp_deck = Deck()
        if isinstance(right, Deck):
            tmp_deck.card_list = [card for card in self.card_list]
            tmp_deck.card_list += [card for card in right.card_list]
        if isinstance(right, Card):
            tmp_deck.append(right)
        return tmp_deck

    def append(self, card):
        self.card_list.append(card)

    def get_cost(self):
        sum_cost = 0
        aces = 0
        for card in self.card_list:
            if card.name != PICT_CARDS[-1]:
                sum_cost += card.get_cost()
            else:
                sum_cost += 1
                aces += 1

        for _ in range(aces):
            if sum_cost + 10 <= MAX_SUM:
                sum_cost += 10
            else:
                break

        return sum_cost

    def __len__(self):
        return len(self.card_list)

    def is_over(self):
        return self.get_cost() > MAX_SUM


class Card:
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit

    def info(self):
        print(f"{self.name} {self.suit} ({self.get_cost()})")

    def __add__(self, right):
        tmp_deck = Deck()
        if isinstance(right, Card):
            tmp_deck.append(self)
            tmp_deck.append(right)
        return tmp_deck

    def get_cost(self):
        cost = 0
        if self.name in NUM_CARDS:
            cost = int(self.name)
        elif self.name in PICT_CARDS[:-1]:
            cost = 10
        elif self.name == PICT_CARDS[-1]:
            cost = 11
        return cost


def generate_full_deck():
    deck = Deck()
    for suit in ['бубей', 'пик', 'червей', 'треф']:
        for nominal in NUM_CARDS + PICT_CARDS:
            card = Card(nominal, suit)
            deck.append(card)

    random.shuffle(deck.card_list)

    return deck


class Dealer:
    def __init__(self):
        self.deck = None
        self.dealer_cards = None
        self.new_game()

    def new_game(self):
        self.deck = generate_full_deck()
        self.dealer_cards = Deck()
        for _ in range(2):
            self.dealer_cards = self.dealer_cards + self.get_card()

    def get_card(self):
        card = self.deck.card_list.pop()
        return card

    def end_game(self):
        while self.dealer_cards.get_cost() < 17:
            self.dealer_cards = self.dealer_cards + self.get_card()


def next_turn(player_deck, dealer):
    print(f'На данный момент сумма равна {player_deck.get_cost()}')
    response = int(input('Сдать карту или хватит ? (1 - сдать, 0 - хватит)'))
    if response == 0:
        return False

    card = dealer.get_card()
    player_deck.append(card)
    print('Вы получили: ')
    card.info()

    return not player_deck.is_over()


def main():
    dealer = Dealer()
    player_deck = Deck()
    stop = 0
    while not stop:
        stop = int(input("Сыграем еще ? (1 - да, 0 - нет)"))

        for _ in range(2):
            card = dealer.get_card()
            player_deck = player_deck + card

        if player_deck.get_cost() == MAX_SUM:
            print('Блэк-Джек. Вы выиграли!')
            print(player_deck.card_list)
            continue

        user_play = True
        is_over = False
        while user_play:
            user_play = next_turn(player_deck, dealer)
            is_over = player_deck.is_over()

        if is_over:
            print('Вы проиграли !')
        else:
            dealer.end_game()

            print('Расклад у диллера - ', str(dealer.dealer_cards.get_cost()))
            for card in dealer.dealer_cards.card_list:
                card.info()

            print('Расклад у вас - ', str(player_deck.get_cost()))
            for card in player_deck.card_list:
                card.info()

            if dealer.dealer_cards.get_cost() > player_deck.get_cost():
                print('Вы проиграли')
            elif dealer.dealer_cards.get_cost() < player_deck.get_cost():
                print('Вы выиграли')
            else:
                print('Ничья')


main()
