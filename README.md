# ✅ Daily Task Organizer

A simple, interactive command-line tool built with Python to help you organize and review your daily tasks. At the end of the day, run the script to get a clear summary of what you've accomplished.

## Features
-   Starts with a predefined list of daily tasks.
-   Interactively asks for the completion status of each task (`yes`/`no`).
-   Validates user input to prevent errors.
-   Sorts tasks into "Completed" and "Incomplete" lists.
-   Provides a clean, final summary of your day's productivity.

## How to Run
1.  Ensure you have Python 3 installed.
2.  Clone or download this repository to your computer.
3.  Open your terminal or command prompt and navigate to the project directory.
4.  Run the script with the following command:
    ```bash
    python task_organizer.py
    ```

## Demo
Here is what a session with the Daily Task Organizer looks like:

```
--- Let's review your daily tasks! ---
Please answer with 'yes' or 'no'.

Did you complete the task: 'Finish the weekly Python project'? yes
👍 Great job!
-------------------------
Did you complete the task: 'Go for a 30-minute walk'? no
😊 No problem, there's always tomorrow!
-------------------------
Did you complete the task: 'Read 10 pages of a book'? yes
👍 Great job!
-------------------------

--- Here is your daily summary ---

✅ Completed Tasks:
- Finish the weekly Python project
- Read 10 pages of a book

❌ Incomplete Tasks:
- Go for a 30-minute walk
```
