import time

def rollercoaster_track():
    track = [
        "   _______",
        "  /       \\",
        " /         \\",
        "|   Roller  |",
        "|   Coaster |",
        "|           |",
        " \\         /",
        "  \\_______/"
    ]
    for segment in track:
        print(segment)
        time.sleep(0.1)

def rollercoaster_simulation():
    print("Welcome to the Text-based Rollercoaster Simulation!")
    input("Press Enter to start the rollercoaster ride...")
    rollercoaster_track()
    print("You survived the rollercoaster! Thanks for riding!")

if __name__ == "__main__":
    rollercoaster_simulation()

