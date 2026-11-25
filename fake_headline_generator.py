
# 1 - Import the random module
import random

# 2 - Create subjects
subjects = [
    "Shah Rukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi",
]

action = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plate of samosas",
    "inside Parliament",
    "during IPL Match",
    "at India Gate",
]

# 3 - Start the headline generation loop
while True:
    selected_subjects = random.choice(subjects)
    selected_action = random.choice(action)
    selected_places_or_things = random.choice(places_or_things)

    # 4 - Generate the headline
    headline = f"BREAKING NEWS: {selected_subjects} {selected_action} {selected_places_or_things}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()

    if user_input == "no":
        break

# Print goodbye message
print("\nThanks for using the headline generator. Have a fun day!")
