from mtg.card import Card


class PriceTable:

    def __init__(self, price_table_path):
        self._info = {}
        with open(price_table_path, "r") as fp:
            for price_info_line in fp.readlines():
                card_name, price = price_info_line.strip().split(" ")
                self._info[card_name] = float(price)

    def set_price(self, card):
        if card.name in self._info:
            card.price = self._info[card.name]
