class Letterbox:
    def __init__(self, house_address, letter_notification_flag=False):
        self.house_address = house_address
        self.letter_notification_flag = letter_notification_flag
        self.letters = list()

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




