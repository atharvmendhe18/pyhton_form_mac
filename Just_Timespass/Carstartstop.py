command = input('>')
command = command.lower()
start = False
while True:
    command = input(">")
    if command == "help":
        print("Start - to start teh car")
        print('Stop - stop the car')
        print('Quit - to quit the game')
    elif command == "start":
        if start:
            print("Car is already started genious!!!")
        else:
            print("Car started..")
            start = True
    elif command == "stop":
        if not start:
            print("Car is already stopped dumbass!!!")
        else:
            print("Car stopped...")
            start = False
    elif command == "quit":
        print("Thank you for playing")
        break
    else:
        print('I dont understand...')