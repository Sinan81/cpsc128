class Deck(CardCollection):
    # Override ancestor's constructor, i.e. replace the default.
    def __init__(self):
        self.cards = []
        for cardnum in range(52):
            self.add( Card(cardnum) )
 
    # Alias the inherited method "size" as "cards_left",
    # because we usually ask how many cards are left in a
    # deck rather than asking about its size.
    def cards_left(self):
        return self.size()
 
    # Another alias. When using a deck of cards we talk about "dealing"
    # cards not "removing" them from the deck.
    def deal(self):
        return self.remove()

    # Add a new method, shuffle, that does not exist in ancestor class.
    def shuffle(self):
        ncards = len(self.cards)
        for swaps in range(ncards):
            swaps = ncards -1 - swaps
            posn1 = random.randint(0, swaps)
            self.cards[posn1], self.cards[swaps] = self.cards[swaps], self.cards[posn1]