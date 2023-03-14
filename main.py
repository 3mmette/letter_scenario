from town import Town
from neighbourhood import Neighbourhood
from building import *
from person import *
from letterbox import Letterbox

if __name__ == '__main__':
    # Create town
    town = Town("Towny", "0001")
    # Create neighbourhoods
    neighbourhood_central = Neighbourhood("Towny Central")
    neighbourhood_north = Neighbourhood("Towny North")
    neighbourhood_east = Neighbourhood("Towny East")
    neighbourhood_south = Neighbourhood("Towny South")
    neighbourhood_west = Neighbourhood("Towny West")
    # Create houses
    house_one = House("1", "First Street", neighbourhood_north.neighbourhood_name, town)
    house_two = House("2", "First Street", neighbourhood_north.neighbourhood_name, town)
    house_three = House("1", "First Road", neighbourhood_east.neighbourhood_name, town)
    house_four = House("1", "First Way", neighbourhood_south.neighbourhood_name, town)
    house_five = House("1", "First Avenue", neighbourhood_west.neighbourhood_name, town)
    # Create post office
    post_office_central = PostOffice("1", "Central Boulevard", neighbourhood_central.neighbourhood_name, town)
    # Create letterboxes
    house_one_letterbox = Letterbox(house_one.address)
    house_two_letterbox = Letterbox(house_two.address)
    house_three_letterbox = Letterbox(house_three.address)
    house_four_letterbox = Letterbox(house_four.address)
    house_five_letterbox = Letterbox(house_five.address)
    # Create people
    person_alice = AliceBobDuo("Alice")
    person_bob = AliceBobDuo("Bob")
    person_charli = PostOfficer("Charli")
    person_sam = LetterThief("Sam")
    # People move into houses
    person_alice.update_address(house_one)
    person_bob.update_address(house_two)
    person_charli.update_address(house_three)
    person_sam.update_address(house_four)

    # Scenario
    print(f"Bobs address: {person_bob.address}")
    print("A sad day as Bob moves to a different neighbourhood")
    person_bob.update_address(house_five)
    print(f"Bobs address: {person_bob.address}")

    print("\nAlice wants to send a letter to Bob. Knowing someone has been reading letters, she encrypts the message.")
    person_alice.write_encrypted_letter("Bob", person_bob.address, "Hey Bob, I hope your new house is great, I can't "
                                                                   "wait to visit!")
    print(f"Alice's letters: {person_alice.letters_written}")

    print("\nAlice seals the letter")
    person_alice.seal_letter()
    print(f"Alice's letter to Bob seal status: {person_alice.letters_written[0].seal}")

    print("\nAlice deposits the letter at the post office, as Bob's house is too far away now")
    person_alice.deposit_letters(post_office_central)
    print(f"Alice's letters: {person_alice.letters_written}")
    print(f"Mail centre letters: {post_office_central.mail_centre_letters}")

    print("\nCharli begins their rounds, picking up the mail from the post office")
    person_charli.retrieve_letters_for_delivery(post_office_central)
    print(f"Mail centre letters: {post_office_central.mail_centre_letters}")
    print(f"Charli's letters for delivery: {person_charli.letters_to_deliver}")

    print("\nCharli gets the address from the letters and places them in their respective letterboxes")
    person_charli.deliver_letters()
    print(f"Charli's letters for delivery: {person_charli.letters_to_deliver}")
    print(f"Bob's letterbox letters: {house_five_letterbox.letters}")
    print(f"Bob's letterbox flag: {house_five_letterbox.letter_notification_flag}")

    print("\nWhile Bob isn't home, a letter thief takes the letters to read")
    person_sam.steal_letters(house_five_letterbox)
    print(f"Bob's letterbox letters: {house_five_letterbox.letters}")
    print(f"Bob's letterbox flag: {house_five_letterbox.letter_notification_flag}")
    print(f"Sam's stolen letters: {person_sam.letters_stolen}")

    print("\nThey open the letter")
    person_sam.open_sealed_letters()
    print(f"Letter seal status: {person_sam.letters_stolen[0].seal}")

    print("\nThey read the message")
    person_sam.read_letters()

    print("\nThe letter thief returns the letters")
    person_sam.return_letters(house_five_letterbox)
    print(f"Sam's stolen letters: {person_sam.letters_stolen}")
    print(f"Bob's letterbox letters: {house_five_letterbox.letters}")
    print(f"Bob's letterbox flag: {house_five_letterbox.letter_notification_flag}")

    print("\nBob comes home and collects his letter")
    person_bob.retrieve_letters()
    print(f"Bob's letterbox letters: {house_five_letterbox.letters}")
    print(f"Bobs letters: {person_bob.letters_received}")

    print("\nBob breaks the seal on the letter")
    person_bob.open_sealed_letters()

    print("\nBob reads the encrypted message")
    person_bob.read_encrypted_letter()

