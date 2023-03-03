class House:
    def __init__(self, street_number, street_name):
        self.street_number = street_number
        self.street_name = street_name

    # Uses the neighbourhood, town and postcode to create a full address
    def create_address(self, neighbourhood, town, postcode):
        house_address = f"{self.street_number} {self.street_name}, {neighbourhood}, {town} {postcode}"
        return house_address
