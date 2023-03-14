class Letter:
    def __init__(self, from_whom, to_whom, to_address, message):
        self.from_whom = from_whom
        self.to_whom = to_whom
        self.to_address = to_address
        self.message = message
        self.seal = False
        self.seal_broken_before = False

    # Creates a seal on a letter, it can not be resealed
    def create_seal(self):
        if not self.seal_broken_before:
            self.seal = True
        else:
            print("Seal has previously been broken. You cannot reseal the letter")

    def break_seal(self):
        self.seal = False
        self.seal_broken_before = True
