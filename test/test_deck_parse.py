from mtg.deck import Deck

if __name__ == "__main__":
    deck = Deck.read_decK("mtga_decks/chinese_format/ESPER MIDRANGE")
    print(deck.main_deck)
    print(deck.sideboard)
