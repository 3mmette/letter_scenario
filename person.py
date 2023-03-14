from letter import Letter
from letterbox import Letterbox
from building import *


# A generic person class needing just their first name.
class Person:
    def __init__(self, first_name):
        self.first_name = first_name
        self.address = None
        self.letters_written = list()
        self.letters_received = list()

    # Once a person is created, they can move into a house using the update address function.
    def update_address(self, house):
        # If it is the first time moving into a house.
        if self.address is None:
            self.address = house.address
            house.occupants.append(self)
        # Removes them from their old address and adds them to their new address.
        else:
            for house in House.houses:
                if self.address == house.address:
                    house.occupants.remove(self)
            self.address = house.address
            house.occupants.append(self)

    # Creates a new letter object and places it in the persons list of letters
    def write_letter(self, to_whom, to_address, message):
        new_letter = Letter(self.first_name, to_whom, to_address, message)
        self.letters_written.append(new_letter)

    # Places a letter into the mail centre at the post office and removes from persons letter list
    def deposit_letters(self, post_office):
        for letter in self.letters_written:
            post_office.mail_centre_letters.append(letter)
            self.letters_written.remove(letter)

    # Takes all the letter in a letterbox and places them in a persons letter list if they are the letterbox owner
    def retrieve_letters(self):
        for letterbox in Letterbox.letterboxes:
            if self.address == letterbox.address:
                for letter in letterbox.letters:
                    self.letters_received.append(letter)
                    letterbox.letters.remove(letter)

    # Breaks the seal on all letters in a persons received letters.
    def open_sealed_letters(self):
        for letter in self.letters_received:
            if letter.seal:
                letter.break_seal()
            if letter.seal_broken_before:
                print("Seal has been broken, this letter has been opened")

    # If the seal has been broken, reads the messages contained in persons received letters.
    def read_letters(self):
        count = 0
        for letter in self.letters_received:
            count += 1
            if letter.seal:
                print(f"Letter {count} is still sealed")
            elif not letter.seal:
                print(f"Letter {count} Message: {letter.message}")
            else:
                print("An error occurred")


# Subclass for Alice and Bob, allowing them to seal letters to each other, as well as encrypt and decrypt them.
class AliceBobDuo(Person):
    def __init__(self, first_name):
        super().__init__(first_name)

    # If a letter is written by Alice or Bob, and is addressed to Alice or Bob, they seal it
    def seal_letter(self):
        for letter in self.letters_written:
            if letter.to_whom == "Bob" or letter.to_whom == "Alice":
                letter.create_seal()

    # Write a letter in a secret code
    def write_encrypted_letter(self, to_whom, to_address, message):
        encrypted_message = ""
        for individual_letter in message:
            encrypted_message += f"{ord(individual_letter)} "
        new_letter = Letter(self.first_name, to_whom, to_address, encrypted_message)
        self.letters_written.append(new_letter)

    # Read a letter written in a secret code
    def read_encrypted_letter(self):
        count = 0
        for letter in self.letters_received:
            count += 1
            if letter.seal:
                print(f"Letter {count} is still sealed")
            elif not letter.seal:
                encrypted_message = letter.message.split()
                unencrypted_message = ""
                for coded_number in encrypted_message:
                    unencrypted_message += chr(int(coded_number))
                print(f"Letter {count} Message: {unencrypted_message}")
            else:
                print("An error occurred")


# Subclass for the person stealing letters. Allows them to steal and replace letters, and open and read letters stolen.
class LetterThief(Person):
    def __init__(self, first_name):
        super().__init__(first_name)
        self.letters_stolen = list()

    # Allows the thief to take letters from any given letterbox.
    def steal_letters(self, letterbox):
        self.letters_stolen = letterbox.letters_retrieved()

    # Override. Allows the thief to open sealed letters in their letters stolen list.
    def open_sealed_letters(self):
        for letter in self.letters_received:
            if letter.seal:
                letter.break_seal()
            else:
                if letter.seal_broken_before:
                    print("Seal has been broken, this letter has been opened")
        for letter in self.letters_stolen:
            if letter.seal:
                letter.break_seal()
            else:
                if letter.seal_broken_before:
                    print("Seal has been broken, this letter has been opened")

    # Override Allows the thief read all letters, both theirs and stolen.
    def read_letters(self):
        count = 0
        print(f"{self.first_name}s letters")
        for letter in self.letters_received:
            count += 1

            if letter.seal:
                print(f"Letter {count} is still sealed")
            elif not letter.seal:
                print(f"Letter {count} Message: {letter.message}")
            else:
                print("An error occurred")
        print("Stolen letters")
        count = 0
        for letter in self.letters_stolen:
            count += 1
            if letter.seal:
                print(f"Letter {count} is still sealed")
            elif not letter.seal:
                print(f"Letter {count} Message: {letter.message}")
            else:
                print("An error occurred")

    # Allows the thief to return letters to any letterbox they are addressed to.
    def return_letters(self, letterbox):
        for letter in self.letters_stolen:
            if letter.to_address == letterbox.address:
                letterbox.letter_deposited(letter)
                self.letters_stolen.remove(letter)


class PostOfficer(Person):
    def __init__(self, first_name):
        super().__init__(first_name)
        self.letters_to_deliver = list()

    # Collects all the letters from the mail centre, ready for delivery.
    def retrieve_letters_for_delivery(self, post_office):
        self.letters_to_deliver = post_office.mail_centre_letters
        post_office.mail_centre_letters = list()

    # Delivers all letters to their respective addresses.
    def deliver_letters(self):
        for letter in self.letters_to_deliver:
            for letterbox in Letterbox.letterboxes:
                if letter.to_address == letterbox.address:
                    letterbox.letter_deposited(letter)
                    self.letters_to_deliver.remove(letter)
