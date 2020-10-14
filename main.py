# Course: CS 30
# Period: 1
# Date created: 20/10/7
# Date last modified: 20/10/14
# Name: Brahm Gainda
# Description: RPG Continuous Game Play

Suspects = []
Clues = []
Persuasion_points = {}

# prompts
interrogate = "Who would you like to interrogate first?\n> "

clues_message = "Would you like to search for more (yes/no)?"

extraclue_found = "You found an extra clue 'Sams hair at the crime scene'\
= 5 p.p. against Sam"

extraclue2_found = "You found an extra clue 'Gun with Bills finger prints'\
= 2 p.p. against Bill"

message = "What would you like to do first?\
Check Suspects List, Check Clues, Check persuasion points"

# Intro Messages
print("enter 'quit' at any time to quit ")
print("\nYou're a famouse detective who has been kidnapped by a deadly gang.")
print("They tell you that a member of they're group has been \
murdered and they want you to solve the case\n")
print("They give you 24 hours to solve the case \
and a list of suspects and clue")
print("to convince the gang you solved the case \
you have to find 10 persuasion points against a suspect")
print("\nso find clues and interrogate suspects \
to get persuasion points against suspects \
and solve the case so you're life is spared")
print("\nWhat would you like to do first?")

# game info
suspects_list = ['Bill', 'Shaniqua', 'Steven', 'Sam']

clues = ['Bills shoe at crime scene = 2 p.p.', 'Bills DNA at crime scene\
= 2 p.p']

persuasion_points = {
                      'bill': 4,
                      'shaniqua': 0,
                      'steven': 0,
                      'sam': 0
                    }

hours_left = 24

# game functions


def game_input(message):
    choice = input(message)
    if choice.lower() == "quit":
        exit()
    return choice


def investigation(hours_left):
    while hours_left > 0:
        message = (f"""
Check Suspects List, Check Clues, Check Persuasion Points
(You have {hours_left} hours left)
> \
""")
        x = game_input(message)
        # Suspects path
        if x.lower() == "check suspects list":
            print('\nSuspects: ' + ', '.join(suspects_list))
            choice = game_input(interrogate)
            if choice.lower() in Suspects:
                print(f"You've already interrogated {choice}")
                continue
            if choice.lower() == "bill" or \
               choice.lower() == "shaniqua" or \
               choice.lower() == "steven" or \
               choice.lower() == "sam":
                    hours_left -= 2
                    Suspects.append(choice)
                    print(f"\nYou interrogated {choice}, they messed up \
and you have 2 persuasion points againt them")
                    persuasion_points[choice] += 2
                    print("you have " + str(hours_left) + " hours left")
                    break
            else:
                print("\nThat isn't a suspect")
                continue

                # clues path
        if x.lower() == "check clues":
            print("\nHere are the clues you have:")
            print(clues)
            print("\n")
            choice = game_input(clues_message)
            if choice.lower() in clues:
                print(f"You've already found {choice}")
                break
            if choice.lower() == "yes":
                    print("\n" + extraclue_found)
                    persuasion_points['sam'] += 4
                    hours_left -= 4
                    print("you have " + str(hours_left) + " hours left")
                    break
            if choice.lower() == "no":
                break
            else:
                print("That isn't a choice")
                continue

        # persuasion points path
        if x.lower() == "check persuasion points":
            print("\nHere are the persuasion points you have:")
            print(persuasion_points)
            print("\n")
            choice = game_input(clues_message)
            if choice.lower() == "yes":
                    print("\n" + extraclue2_found)
                    persuasion_points['bill'] += 2
                    hours_left -= 4
                    print("you have " + str(hours_left) + " hours left")
                    break
            else:
                print("That isn't a choice")
                continue

            # quit
            if x.lower() == "quit":
                hours_left = 0
                exit()

        else:
            print("\nYou did not pick one of the available options")
            print("try again")
            continue

investigation(hours_left)
