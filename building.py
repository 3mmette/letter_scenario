# A building class, which takes a street number and name, in addition to one of the neighbourhoods created and the town.
class Building:

    def __init__(self, street_number, street_name, neighbourhood, town):
        self.street_number = street_number
        self.street_name = street_name
        # Creates a full address for the building.
        self.address = f"{self.street_number} {self.street_name}, {neighbourhood}, {town.town_name} {town.postcode}"


# Subclass house, which has a list of the people living in the house and a list of all the houses created.
class House(Building):
    # List of all house instances created.
    houses = list()

    def __init__(self, street_number, street_name, neighbourhood, town):
        super().__init__(street_number, street_name, neighbourhood, town)
        self.occupants = list()


# Subclass post office, which has a mail centre for all the letters deposited for delivery.
class PostOffice(Building):
    def __init__(self, street_number, street_name, neighbourhood, town):
        super().__init__(street_number, street_name, neighbourhood, town)
        self.mail_centre_letters = list()
