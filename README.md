# Task-Manager

This project is focused on working with files and string manipulation, along with the use of conditional logic and loops. The goal is to create a program to help a small business manage tasks assigned to each member of their team.

## Project Overview

In this Capstone Project, you will create a Python program that works with two text files, `user.txt` and `tasks.txt`, to manage tasks and users.

### Project Details
1. **File Setup:**
   - Copy the provided template program `task_template.py` and rename it to `task_manager.py`.
   - Review the contents of `tasks.txt` and `user.txt`.

2. **tasks.txt:**
   - Stores a list of all tasks with the following data on each line:
     - Username of the person assigned to the task.
     - Title of the task.
     - Description of the task.
     - Date the task was assigned.
     - Due date for the task.
     - Completion status (Yes/No).

3. **user.txt:**
   - Stores usernames and passwords in the following format:
     - `username, password`
       
4. **Program Functionalities:**
   - **Login:**
     - Prompt the user to enter a username and password.
     - Validate credentials against `user.txt`.
     - Display an error message for invalid credentials and prompt again.

   - **Register a User (r):**
     - Only available to the admin user.
     - Prompt for a new username and password, and confirm the password.
     - Write the new credentials to `user.txt` if the password is confirmed.

   - **Add a Task (a):**
     - Prompt for the username of the assignee, task title, description, and due date.
     - Write the new task to `tasks.txt` with the current date as the assignment date and "No" as the default completion status.

   - **View All Tasks (va):**
     - Display all tasks from `tasks.txt` in an easy-to-read format.

   - **View My Tasks (vm):**
     - Display only the tasks assigned to the current user in an easy-to-read format.

  ### Admin-Specific-Functions
  - **Admin-Specific Functionalities:**
  - Only the user with the username `admin` can register new users.
  - Admin users have an additional menu option to display statistics:
    - Total number of tasks.
    - Total number of users.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/NomaIV/Task-Manager.git
   cd L1T19
   ```

2. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

## Usage

1. Run the program:
   ```bash
   python3 task_manager.py
   ```

2. Follow the on-screen prompts to log in and select the desired functionality.

3. Menu Options:
   - `r`: Register  new user (admin only)
   - `a`: Add a new task
   - `va`: View all tasks
   - `vm`: View my tasks
   - `sd`: Display statistics (admin only)
   - `e`: Exit the program

## Technology Used

- Python

## Example Usage

Upon running `task_manager.py`, the program will display a menu allowing the user to choose between different actions such as adding tasks, viewing tasks, and managing users (admin only). Depending on the selection, the program will guide the user through entering the necessary information and display the relevant data.

## License

This project is licensed under the MIT License 



