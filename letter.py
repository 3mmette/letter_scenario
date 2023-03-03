class Letter:
    def __init__(self, letter_id, from_whom, to_whom, to_address, message, seal=False):
        self.letter_id = letter_id
        self.from_whom = from_whom
        self.to_whom = to_whom
        self.to_address = to_address
        self.message = message
        self.seal = seal

    # Changes the seal status of a letter to True
    def create_seal(self):
        self.seal = True

    # Changes the seal status of a letter to False
    def break_seal(self):
        self.seal = False
