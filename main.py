#TODO 1: Present User with options & Request User Input
print("Welcome to Task Tracker 1.0")

trackerIsRunning = True

while trackerIsRunning:
    user_selection = int(input("Please select an option:\n1. List Tasks\n2. Add Task\n3. Update Task\n4. Delete Task\n5. Exit\n"))

    if user_selection == 1:
        print("List Tasks")
    elif user_selection == 2:
        print("Add Task")
    elif user_selection == 3:
        print("Update Task")
    elif user_selection == 4:
        print("Delete Task")
    elif user_selection == 5:
        print("Exiting Tracker")
        trackerIsRunning = False
    else:
        print("Invalid Option")

#TODO 2: Handle User Selection

#TODO 3: List all tasks, done, not done, in progress

#TODO 4: Add Tasks to Tracker

#TODO 5: Update Tasks Progress

#TODO 6: Delete Task from Tracker

#TODO 7 Store tasks in json file
