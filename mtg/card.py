class Card:

    def __init__(self, **kwargs):
        self._name = kwargs["name"]

        if "price" in kwargs:
            self._price = kwargs["price"]
        else:
            self._price = None

    def __repr__(self):
        return self._name

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price
