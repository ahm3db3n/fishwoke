import random

def fishing_game():
    fish_types = {
        "bass": 30,
        "trout": 20,
        "shark": 500,
        "old_cd_disc": 0,
        "alex_fish": 30,
        "rainbow_fish": 20,
        "rainbow_super_trout": 90,
        "hammershark": 40,
        "imperfect_salmon": 150,
        "Daniel_fish": 1000
        
    }

    inventory = []
    print("Welcome to Fishwoke! You are stranded in the middle of the ocean with nothing else but a rod and your will to fish. Good luck, skibidi fishing!")
    score = 0

    while True:
        input("Press Enter to cast your mighty rod!")
        catch = random.choice(list(fish_types.keys()))
        points = fish_types[catch]
        score += points
        print(f"You have caught a {catch} with that mighty rod of yours. Your total score is {score}.")

        if catch == "old_cd_disc":
            print("Oh no! You have caught a CD disc. Better luck next time!")
        elif catch == "imperfect_salmon":
            print("Wow! You've encountered the Imperfect Salmon, a rare and challenging catch!")
            engage_boss = input("Do you want to engage in a battle with the Imperfect Salmon? (yes/y or no/n): ").lower()
            if engage_boss in ["y", "yes"]:
                boss_score = 0
                print("The battle begins! Defeat the Imperfect Salmon by reaching 200 points.")
                while boss_score < 200:
                    boss_choice = random.choice(list(fish_types.keys()))
                    if boss_choice == "imperfect_salmon":
                        print("The Imperfect Salmon is resisting your attacks!")
                    else:
                        boss_points = fish_types[boss_choice]
                        boss_score += boss_points
                        print(f"The Imperfect Salmon attacks with a {boss_choice}! Your total score against the boss is {boss_score}.")
                
                print("Congratulations! You defeated the Imperfect Salmon!")
            else:
                print("You chose to avoid the battle with the Imperfect Salmon.")

        inventory.append(catch) 
        continue_game = input("Would you like to cast that rod again? (yes/y or no/n): ").lower()

        if continue_game in ["y", "yes"]:
            print("Yay! You chose to fish some more. Let's do it!")
        else:
            print("Your inventory contains:", inventory)
            delete_choice = input("Would you like to delete any items from your inventory? (yes/y or no/n): ").lower()
            if delete_choice in ["y", "yes"]:
                while True:
                    print("Inventory:", inventory)
                    delete_item = input("Enter the name of the item you want to delete: ")
                    if delete_item in inventory:
                        inventory.remove(delete_item)
                        print(f"{delete_item} has been removed from your inventory.")
                        break
                    else:
                        print("Item not found in inventory.")
            print(f"I hope you have a great day! Your final score is {score}.")
            break

fishing_game()
