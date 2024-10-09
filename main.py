print("Welcome to Task Tracker 1.0\n")

trackerIsRunning = True

tasks = ["Finish Task Tracker App", "Task 2"]

while trackerIsRunning:
    user_selection = int(input("Please select an option:\n1. List Tasks\n2. Add Task\n3. Update Task\n4. Delete Task\n5. Exit\n"))

    if user_selection == 1:
        if len(tasks) < 1:
            print("You currently have 0 tasks.\n")
        else:
            for task in tasks:
                print(task)
    elif user_selection == 2:
        print("Add Task\n")
    elif user_selection == 3:
        print("Update Task\n")
    elif user_selection == 4:
        print("Delete Task\n")
    elif user_selection == 5:
        print("Exiting Tracker\n")
        trackerIsRunning = False
    else:
        print("Invalid Option\n")

#TODO 2: Handle User Selection

#TODO 3: List all tasks, done, not done, in progress

#TODO 4: Add Tasks to Tracker

#TODO 5: Update Tasks Progress

#TODO 6: Delete Task from Tracker

#TODO 7 Store tasks in json file
