command = " "
started = False
stopped = False

while command != "quit":
    command = input("> ").lower()

    if command == "start":
        if started:
            print("Already started")
        else:
            started = True
            print("Started")
    elif command == "stop":
        if stopped:
            print("Already stopped")
        else:
            stopped = True
            print("Stopped")
    elif command == "help":
        print(""""
        start - start the car
        stop - stop the car
        quit - quit
        """)
    elif command == "quit":
        break
    else:
        print("Invalid command")