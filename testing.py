# Mad Libs Python Program

# Define the three templates
template_1 = (
    "It was about {num_1} {time_1} ago when I arrived at the hospital in a {transport}. "
    "The hospital is a/an {adj_1} place, there are a lot of {adj_2} {noun_1} here. "
    "There are nurses here who have {color_1} {body_1}. If someone wants to come into "
    "my room I told them that they have to {verb_1} first. I’ve decorated my room with "
    "{num_2} {noun_2}. Today I talked to a doctor and they were wearing a {noun_3} on "
    "their {body_2}. I heard that all doctors {verb_2} {noun_4} every day for breakfast. "
    "The most {adj_3} thing about being in the hospital is the {silly_1} {noun_5}!"
)

template_2 = (
    "This weekend I am going camping with {person_1}. I packed my lantern, sleeping bag, and {noun_1}. "
    "I am so {feel_1} to {verb_1} in a tent. I am {feel_2} we might see a(n) {animal_1}, "
    "I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb_2}. "
    "I have heard that the {color_1} lake is great for {verb_ing_1}. Then we will {adverb_1} hike "
    "through the forest for {num_1} {time_1}. If I see a {color_2} {animal_2} while hiking, "
    "I am going to bring it home as a pet! At night we will tell {num_2} {silly_1} stories "
    "and roast {noun_2} around the campfire!!"
)

template_3 = (
    "Dear {person_1}, I am writing to you from a {adj_1} castle in an enchanted forest. "
    "I found myself here one day after going for a ride on a {color_1} {animal_1} in {place_1}. "
    "There are {adj_2} {creature_1} and {adj_3} {creature_2} here! In the {room_1} there is a pool full of {noun_1}. "
    "I fall asleep each night on a {noun_2} of {noun_3} and dream of {adj_4} {noun_4}. "
    "It feels as though I have lived here for {num_1} {time_1}. I hope one day you can visit, "
    "although the only way to get here now is {verb_ing_1} on a {adj_5} {noun_5}!!"
)

# 1. Allow the user to pick one of the templates
print("Choose a Mad Libs template:")
print("1. Hospital Adventure")
print("2. Camping Trip")
print("3. Enchanted Castle")

choice = input("Type the number of your template (1, 2, or 3): ")

# 2. Ask the user to input words based on the chosen template
if choice == "1":
    print("\n--- Fill in the blanks for Template 1 ---")
    data = {
        "num_1": input("Type number: "),
        "time_1": input("Type measure of time: "),
        "transport": input("Type mode of transportation: "),
        "adj_1": input("Type adjective: "),
        "adj_2": input("Type adjective 2: "),
        "noun_1": input("Type noun: "),
        "color_1": input("Type color: "),
        "body_1": input("Type part of the body: "),
        "verb_1": input("Type verb: "),
        "num_2": input("Type number 2: "),
        "noun_2": input("Type noun 2: "),
        "noun_3": input("Type noun 3: "),
        "body_2": input("Type part of the body 2: "),
        "verb_2": input("Type verb 2: "),
        "noun_4": input("Type noun 4: "),
        "adj_3": input("Type adjective 3: "),
        "silly_1": input("Type silly word: "),
        "noun_5": input("Type noun 5: "),
    }
    story = template_1.format(**data)

elif choice == "2":
    print("\n--- Fill in the blanks for Template 2 ---")
    data = {
        "person_1": input("Type proper noun (person's name): "),
        "noun_1": input("Type noun: "),
        "feel_1": input("Type adjective (feeling): "),
        "verb_1": input("Type verb: "),
        "feel_2": input("Type adjective (feeling) 2: "),
        "animal_1": input("Type animal: "),
        "verb_2": input("Type verb 2: "),
        "color_1": input("Type color: "),
        "verb_ing_1": input("Type verb (ending in ing): "),
        "adverb_1": input("Type adverb (ending in ly): "),
        "num_1": input("Type number: "),
        "time_1": input("Type measure of time: "),
        "color_2": input("Type color 2: "),
        "animal_2": input("Type animal 2: "),
        "num_2": input("Type number 2: "),
        "silly_1": input("Type silly word: "),
        "noun_2": input("Type noun 2: "),
    }
    story = template_2.format(**data)

elif choice == "3":
    print("\n--- Fill in the blanks for Template 3 ---")
    data = {
        "person_1": input("Type proper noun (person's name): "),
        "adj_1": input("Type adjective: "),
        "color_1": input("Type color: "),
        "animal_1": input("Type animal: "),
        "place_1": input("Type place: "),
        "adj_2": input("Type adjective 2: "),
        "creature_1": input("Type magical creature (plural): "),
        "adj_3": input("Type adjective 3: "),
        "creature_2": input("Type magical creature (plural) 2: "),
        "room_1": input("Type room in a house: "),
        "noun_1": input("Type noun: "),
        "noun_2": input("Type noun 2: "),
        "noun_3": input("Type noun (plural) 3: "),
        "adj_4": input("Type adjective 4: "),
        "noun_4": input("Type noun (plural) 4: "),
        "num_1": input("Type number: "),
        "time_1": input("Type measure of time: "),
        "verb_ing_1": input("Type verb (ending in ing): "),
        "adj_5": input("Type adjective 5: "),
        "noun_5": input("Type noun 5: "),
    }
    story = template_3.format(**data)

else:
    story = "Invalid choice! Please restart the program and pick 1, 2, or 3."

# 3. Generate the story afterwards and show it to the user
print("\n" + "=" * 40)
print("HERE IS YOUR STORY:")
print("=" * 40)
print(story)
print("=" * 40)