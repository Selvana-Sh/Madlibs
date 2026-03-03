print("--------Welcome to MAD LIBS--------")


def get_number(prompt):
    # making sure user enters an int
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def story_1():
    num1 = get_number("number: ")
    time = input("mesure of  time: ")
    transport = input("which mode of transportation : ")
    adj1 = input("give us the first adjective: ")
    adj2 = input("give us an adjective: ")
    noun1 = input("give us the first noun: ")
    color = input("which color would you prefer: ")
    body_part1 = input("name a body part: ")
    verb = input("which verb would you prefer?: ")
    num2 = get_number("give us anumber: ")
    noun2 = input("a noun please?: ")
    noun3 = input("give us another noun: ")
    body_part2 = input("name the last body part: ")
    noun4 = input("give us one last noun: ")
    adj3 = input("give us an adjective: ")
    silly_word = input("give us a silly Word: ")

    return (
        f"It was about {num1} {time} ago when I arrived at "
        f"the hospital in a {transport}.\n"
        f"The hospital is a/an {adj1} place, there are a lot "
        f"of {adj2} {noun1} here.\n"
        f"There are nurses here who have {color} {body_part1}.\n"
        f"If someone wants to come into my room I told them "
        f"that they have to {verb} first.\n"
        f"I've decorated my room with {num2} {noun2}.\n"
        f"Today I talked to a doctor and they were wearing "
        f"a {noun3} on their {body_part2}.\n"
        f"I heard that all doctors {verb} {noun4} every day "
        f"for breakfast.\n"
        f"The most {adj3} thing about being in the hospital "
        f"is the {silly_word} {noun1}."
    )


def story_2():
    proper_noun = input("Give us a proper noun: ")
    noun1 = input("Give us the first noun: ")
    adj_feeling1 = input(
        "Give us the first adjective which describes a feeling: "
    )
    verb1 = input("Give us the first verb: ")
    animal = input("Give us a name of an animal: ")
    adj_feeling2 = input(
        "Give us the second adjective which describes a feeling: "
    )
    verb2 = input("Give us the second verb: ")
    color = input("Give us a color: ")
    verb_ing = input("Give us a verb ending with -ing: ")
    adverb = input("Give us an adverb: ")
    number = get_number("Give us a number: ")
    time = input("Give us a time: ")
    silly_word = input("Give us a silly word: ")
    noun2 = input("Give us the second noun: ")

    return (
        f"This weekend I'm going camping with {proper_noun}.\n"
        f"I packed my lantern, sleeping bag, and {noun1}.\n"
        f"I am so {adj_feeling1} to {verb1} in a tent.\n"
        f"I am {adj_feeling2}.\n"
        f"We might see a(n) {animal}.\n"
        f"While we're camping, we are going to hike, fish, "
        f"and {verb2}.\n"
        f"I have heard that the {color} lake is great for "
        f"{verb_ing}.\n"
        f"Then we will {adverb} hike through the forest "
        f"for {number} {time}.\n"
        f"If I see a {color} {animal} while hiking, I am "
        f"going to bring it home as a pet!\n"
        f"At night we will tell {number} {silly_word} "
        f"stories and roast {noun2} around the campfire!!"
    )


def story_3():
    proper_noun = input("Give us a proper noun: ")
    adj1 = input("give us the first adjective: ")
    color = input("Give us a color: ")
    animal = input("Give us a name of an animal: ")
    place = input("Name a place: ")
    adj2 = input("give us an adjective: ")
    magical1 = input(
        "Give us a name for the first magical place: "
    )
    adj3 = input("give us an adjective: ")
    magical2 = input(
        "Give us a name for the second magical place: "
    )
    room = input("Name a room in a House: ")
    noun1 = input("Give us the first noun: ")
    noun2 = input("Give us the second noun: ")
    noun_pl1 = input("Give us the first noun (in plural): ")
    adj4 = input("Give us an adjective: ")
    noun_pl2 = input("Give us the second noun (in plural): ")
    number = get_number("Give us a number: ")
    time = input("Give us a time: ")
    verb_ing = input("Give us a verb ending with -ing: ")
    adj5 = input("Give us an adjective: ")
    noun3 = input("Give us the last noun: ")

    return (
        f"Dear {proper_noun}, I am writing to you from "
        f"a {adj1} castle in an enchanted forest.\n"
        f"I found myself here after riding a {color} "
        f"{animal} in {place}.\n"
        f"There are {adj2} {magical1} and {adj3} "
        f"{magical2} here!\n"
        f"In the {room} there is a pool full of {noun1}.\n"
        f"I fall asleep on a {noun2} of {noun_pl1} and "
        f"dream of {adj4} {noun_pl2}.\n"
        f"It feels like {number} {time}.\n"
        f"The only way to get here is {verb_ing} on a "
        f"{adj5} {noun3}!!"
    )


def start_game():
    stories = {
        "1": story_1,
        "2": story_2,
        "3": story_3,
    }

    while True:
        print("\nChoose a story template:")
        print("1 - Hospital Story")
        print("2 - Camping Story")
        print("3 - Castle Story")

        choice = input("Enter 1, 2 or 3: ")

        if choice not in stories:
            print("Invalid choice. Please try again.")
            continue

        print("\nYour story is done!\n")
        story_text = stories[choice]()
        print(story_text)

        # play again?
        while True:
            again = input("\nDo you want to play again? (y/n): ").lower()
            if again in ["y", "n"]:
                break
            print("Please enter 'y' or 'n'.")

        if again == "n":
            print("\nThank you for playing our game!")
            break


start_game()