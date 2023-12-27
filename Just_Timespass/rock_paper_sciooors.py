# aim is to create rock, paper and scissors game without the help from the intrnet and only using what i have learned
import random

machine_points = 0
human_points = 0
chhoice_for_machines = ['rock', 'paper', 'scissor']
no_of_tries = 0

while no_of_tries < 5:

    machine_input = random.choice(chhoice_for_machines)
    human_input = input("choose between rock, paper and scissor ")

    if human_input == 'rock' and machine_input == "paper":
        machine_points += 1
        no_of_tries += 1
        print(human_input)
        print(f'Machine chooses {machine_input} ')
        print(f'Machine points = {machine_points} ')
        print(f'Human points = {human_points} ')
    elif human_input == "rock" and machine_input == "scissor":
        human_points += 1
        no_of_tries += 1
        print(f'Machine chooses {machine_input} ')
        print(f'Machine points = {machine_points} ')
        print(f'Human points = {human_points} ')
    elif human_input == "rock" and machine_input == "rock":
        no_of_tries += 1
        print(f'Machine chooses {machine_input} ')
        print(f'Machine points = {machine_points} ')
        print(f'Human points = {human_points} ')
    elif human_input == "paper" and machine_input == "scissor":
        machine_points += 1
        no_of_tries += 1
        print(f'Machine chooses {machine_input} ')
        print(f'Machine points = {machine_points} ')
        print(f'Human points = {human_points} ')
    elif human_input == "paper" and machine_input == "paper":
        no_of_tries += 1
        print(f'Machine chooses {machine_input} ')
        print(f'Machine points = {machine_points} ')
        print(f'Human points = {human_points} ')
    elif human_input == "paper" and machine_input == "rock":
        no_of_tries += 1
        human_points += 1
        print(f'Machine chooses {machine_input} ')
        print(f'Machine points = {machine_points} ')
        print(f'Human points = {human_points} ')
    elif human_input == "scissor" and machine_input == "rock":
        machine_points += 1
        no_of_tries += 1
        print(f'Machine chooses {machine_input} ')
        print(f'Machine points = {machine_points} ')
        print(f'Human points = {human_points} ')
    elif human_input == "scissor" and machine_input == "scissor":
        no_of_tries += 1
        print(f'Machine chooses {machine_input} ')
        print(f'Machine points = {machine_points} ')
        print(f'Human points = {human_points} ')
    elif human_input == "scissor" and machine_input == "paper":
        human_points += 1
        no_of_tries += 1
        print(f'Machine chooses {machine_input} ')
        print(f'Machine points = {machine_points} ')
        print(f'Human points = {human_points} ')
if human_points > machine_points:
    print("Human Won")
elif human_points == machine_points:
    print("Its a tie between human and machine")
else:
    print("Machine Won")
