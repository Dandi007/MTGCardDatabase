from typing import List, Union
from mtg.card import Card
from pathlib import Path
from mtg.price_table import PriceTable


class Deck:

    def __init__(self, mtga_deck_file: Union[Path, str]):
        with open(mtga_deck_file, "r") as fp:

            self._main_cards = []
            self._sideboard = []

            self._card_dict = {}

            fetch_main_cards = False

            for meta_line in fp.readlines():
                meta_info = meta_line.strip().split(" ")
                if len(meta_info) < 2:
                    # check parse mode
                    if meta_info[0] == "Deck":
                        fetch_main_cards = True
                    if meta_info[0] == "Sideboard":
                        fetch_main_cards = False
                else:
                    # parse card
                    card_number, card_name = meta_info
                    card_number = int(card_number)
                    self._card_dict[card_name] = card_number
                    cards = [Card(name=card_name) for _ in range(card_number)]
                    if fetch_main_cards:
                        self._main_cards.extend(cards)
                    else:
                        self._sideboard.extend(cards)

    @property
    def sideboard(self):
        return self._sideboard

    @property
    def main_deck(self):
        return self._main_cards

    def load_price(self, price_table: PriceTable):
        tot = 0
        for card in self.main_deck + self.sideboard:
            price_table.set_price(card)
            tot += card.price
        return tot
