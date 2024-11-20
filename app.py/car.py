car_started = False

command = ""
while command != 'quit':
    command = input('>').lower()
    if command == 'start':
        if car_started:
            print('The car is already started.')
        else:
            print('The car has started.')
            car_started = True
    elif command == 'stop':
        if not car_started:
            print('The car is already stopped.')
        else:
            print('The car has stopped.')
            car_started = False
    elif command == 'help':
        print("""
start: to start the car
stop: to stop the car
quit: to exit the program
        """)
    elif command == 'quit':
        print("Program terminated")
        break
    else:
        print("Invalid command. Type 'help' for a list of commands.")

