# Weekly Project 01: Daily Task Organizer

# 1. At the start of the day, you create a checklist of tasks.
# Here is our predefined list of tasks for the day.
daily_tasks = [
    "Finish the weekly Python project",
    "Go for a 30-minute walk",
    "Read 10 pages of a book",
    "Plan tomorrow's schedule",
    "Water the plants"
]

# We create two empty lists to store the sorted tasks.
completed_tasks = []
incomplete_tasks = []

print("--- Let's review your daily tasks! ---")
print("Please answer with 'yes' or 'no'.\n")

# 2. At the end of the day, review which tasks you could finish.
# We use a 'for' loop to go through each task in the main list.
for task in daily_tasks:
    # A 'while' loop is used to ensure the user provides a valid answer.
    while True:
        # Ask for user input for each task.
        # .lower() makes the input lowercase, and .strip() removes extra spaces.
        status = input(f"Did you complete the task: '{task}'? ").lower().strip()

        # An 'if-elif-else' control structure checks the user's answer.
        if status == "yes":
            # If the task is finished, add it to the 'completed_tasks' list.
            completed_tasks.append(task)
            print("👍 Great job!")
            break  # Exit the 'while' loop to move to the next task.
        elif status == "no":
            # If the task is not finished, add it to the 'incomplete_tasks' list.
            incomplete_tasks.append(task)
            print("😊 No problem, there's always tomorrow!")
            break  # Exit the 'while' loop.
        else:
            # If the input is invalid, this message is shown.
            print("Invalid input. Please enter 'yes' or 'no'.")
    print("-" * 25) # Adds a separator for better readability

# 3. By the end of the day, you'll have a clear overview.
print("\n--- Here is your daily summary ---")

# Display the list of completed tasks.
print("\n✅ Completed Tasks:")
if completed_tasks:
    for item in completed_tasks:
        print(f"- {item}")
else:
    print("You have no completed tasks for today.")

# Display the list of incomplete tasks.
print("\n❌ Incomplete Tasks:")
if incomplete_tasks:
    for item in incomplete_tasks:
        print(f"- {item}")
else:
    print("🎉 Congratulations! You have completed all your tasks today!")