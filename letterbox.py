class Letterbox:
    # A list of all the letterboxes created
    letterboxes = list()

    def __init__(self, address, letter_notification_flag=False):
        self.address = address
        self.letter_notification_flag = letter_notification_flag
        self.letters = list()

        Letterbox.letterboxes.append(self)

    # Takes a letter and places it in the letterbox list, sets flag to True
    def letter_deposited(self, letter):
        self.letters.append(letter)
        self.letter_notification_flag = True

    # Returns all letter so a person object can take them, removes all letter objects from the letterbox, flag to False
    def letters_retrieved(self):
        self.letter_notification_flag = False
        all_letters = self.letters
        self.letters = list()
        return all_letters




