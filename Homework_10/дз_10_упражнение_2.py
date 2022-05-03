from abc import abstractmethod

class Clothes:
    @abstractmethod
    def __init__(self, size, height, num_coat, num_suit):
        self.size = size
        self.height = height
        self.num_coat = num_coat
        self.num_suit = num_suit

    @property
    def fabric_consumption_for_coat(self):
        return str((self.size / 6.5 + 0.5) * self.num_coat)

    @property
    def fabric_consumption_for_suit(self):
        return str((2 * self.height + 0.3) * self.num_suit)

    @abstractmethod
    def all_fabric_consumption(self):
        return (self.size / 6.5 + 0.5) * self.num_coat + (2 * self.height + 0.3) * self.num_suit

class Coat(Clothes):
    def __init__(self, size, num_coat):
        self.size = size
        self.num_coat = num_coat

class Suit(Clothes):
    def __init__(self, height, num_suit):
        self.height = height
        self.num_suit = num_suit


coat = Coat(13, 2)
print(coat.fabric_consumption_for_coat)
suit = Suit(5, 10)
print(suit.fabric_consumption_for_suit)
clothes = Clothes(13, 5, 2, 10)
print(clothes.all_fabric_consumption())