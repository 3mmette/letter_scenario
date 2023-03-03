from letter import Letter


class Person:
    # Initialization
    def __init__(self, first_name, lives_at_address):
        self.first_name = first_name
        self.lives_at_address = lives_at_address
        self.letters = list()

    # Creates a new letter object and places it in the persons list of letters
    def write_letter(self, letter_id, to_whom, to_address, message):
        new_letter = Letter(letter_id, self.first_name, to_whom, to_address, message, False)
        self.letters.append(new_letter)

    # Changes to seal status of a selected letter in the list, by the letters id
    def seal_letter(self, find_letter_id):
        for letter in self.letters:
            if letter.letter_id == find_letter_id:
                letter.create_seal()

    # Places a letter, identified by its id, into a specified letterbox
    def deposit_letter(self, find_letter_id, letterbox):
        for letter in self.letters:
            if letter.letter_id == find_letter_id:
                letterbox.letter_deposited(letter)
                self.letters.remove(letter)

    # Takes all the letter in a letterbox and places them in a persons letter list
    def retrieve_letters(self, letterbox):
        self.letters = letterbox.letters_retrieved()

    # Breaks the seal on a selected letter, by its id
    def open_letter(self, find_letter_id):
        for letter in self.letters:
            if letter.letter_id == find_letter_id:
                letter.break_seal()

    # If the seal has been broken, reads the message contained in the letter, identified by its id
    def read_letter(self, find_letter_id):
        for letter in self.letters:
            if letter.letter_id == find_letter_id:
                if letter.seal is True:
                    print("The letter is still sealed")
                elif letter.seal is False:
                    print(f"Message: {letter.message}")
                else:
                    print("An error occurred")

    # Updates the address of a person
    def update_address(self, new_address):
        self.lives_at_address = new_address
