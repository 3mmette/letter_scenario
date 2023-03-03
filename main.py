from town import Town
from neighbourhood import Neighbourhood
from house import House
from person import Person
from letterbox import Letterbox

if __name__ == '__main__':
    # Create instances
    town = Town("Towny", "0001")
    neighbourhood = Neighbourhood("Towny North")

    house_one = House("1", "First Street")
    house_one_address = house_one.create_address(neighbourhood.neighbourhood_name, town.town_name, town.postcode)
    house_one_letterbox = Letterbox(house_one_address)
    person_alice = Person("Alice", house_one_address)

    house_two = House("2", "First Street")
    house_two_address = house_two.create_address(neighbourhood.neighbourhood_name, town.town_name, town.postcode)
    house_two_letterbox = Letterbox(house_two_address)
    person_bob = Person("Bob", house_two_address)

    # Letterbox Status
    print("Letterbox status")
    print(f"Alice's letterbox flag: {house_one_letterbox.letter_notification_flag}")
    print(f"Bob's letterbox flag: {house_two_letterbox.letter_notification_flag}")

    # Alice writes a letter
    print("\nAlice writes a letter")
    person_alice.write_letter(1, person_bob.first_name, person_bob.lives_at_address, "Hey Bob")
    print(f"Letters in Alice's Possession: {len(person_alice.letters)}")

    # Alice seals the letter
    print(f"\nSealed: {person_alice.letters[0].seal}")
    print("Alice seals the letter")
    person_alice.seal_letter(1)
    print(f"Sealed: {person_alice.letters[0].seal}")

    # Alice places it in Bobs mailbox
    print("\nAlice places it in Bobs letterbox")
    person_alice.deposit_letter(1, house_two_letterbox)
    print(f"Bob's letterbox flag: {house_two_letterbox.letter_notification_flag}")
    print(f"Letters in Alice's possession: {len(person_alice.letters)}")
    print(f"Letters in Bob's letterbox: {len(house_two_letterbox.letters)}")

    # Bob removes the letter from his letterbox
    print("\nBob removes the letter from his letterbox")
    person_bob.retrieve_letters(house_two_letterbox)
    print(f"Bob's letterbox flag: {house_two_letterbox.letter_notification_flag}")
    print(f"Letters in Bob's letterbox: {len(house_two_letterbox.letters)}")
    print(f"Letters in Bob's possession: {len(person_bob.letters)}")

    # Bob tried to read the letter without breaking the seal
    print("\nBob tried to read the letter without breaking the seal")
    person_bob.read_letter(1)

    # Bob opens the letter
    print("\nBob opens the letter")
    person_bob.open_letter(1)
    print(f"Sealed: {person_bob.letters[0].seal}")

    # Bob can now read the letter
    print("\nBob reads the letter")
    person_bob.read_letter(1)
