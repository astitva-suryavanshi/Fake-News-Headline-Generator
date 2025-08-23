import random

subjects = ["Sharukh Khan", "Virat Kohli", "Nirmala Sitaraman", "A Mumbai Cat", "A group of Monkeys"]

actions = ["launches", "cancels", "dance", "eats", "declare war"]

things = ["at RedFort", "in Mumbai local train", "a plate of Samosa", "inside parliament", "at Ganga Ghats","during IPL match"]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    thing = random.choice(things)

    headline = f"BREAKING NEWS : {subject} {action} {thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another Headlines?(yes/no)").strip()
    if user_input == "no":
        break

    print("Thanks for using")