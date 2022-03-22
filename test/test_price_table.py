from mtg.price_table import PriceTable
from mtg.deck import Deck
import unittest
from pathlib import Path


class TestPriceTable(unittest.TestCase):

    def test_find_price(self):
        price_table = PriceTable("../mtga_decks/价位表.txt")

        for deck_path in Path("../mtga_decks/chinese_format").glob("*"):
            deck = Deck(deck_path)
            print(f"display info from deck {deck_path}")
            print("card not found in price table:")
            for card in deck.main_deck:
                price_table.set_price(card)
            for card in deck.sideboard:
                price_table.set_price(card)

            print("card single price of deck is:")
            for card in deck.main_deck + deck.sideboard:
                print(f"{card} {card.price}")

            print(f"deck price of {deck_path} is {deck.load_price(price_table)}")


if __name__ == '__main__':
    unittest.main()
