'''This is the section where you will import libraries'''
from datetime import date, datetime # from Programiz 'how to get current date and time in python?

# Open and read file tasks.txt and write instruction.

file = open ("tasks.txt", "r")
lines = file.read ()
file.close()

# Login Section
# Read usernames and passwords from user.txt file
user_data = {}
with open("user.txt", "r") as file:
    for line in file:
        line = line.strip()
        line = line.split(",")
        if len(line) == 2:
            user_data[line[0]] = line[1]

# Use a while loop to validate username and password
login_attempts = 3
while login_attempts > 0:
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")

    # Validate the username and password
    if entered_username in user_data and user_data[entered_username] == entered_password:
        print("Login successful!")

        break
    else:
        print("Invalid username or password. Please try again.")
        login_attempts -= 1

# If the loop completes without breaking, print a message
else:
    print("Login attempts exceeded. Account locked.")

while True:
    # Present the menu to the user and 
    # Make sure that the user input is converted to lower case.
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
sd - statistics display                 
e - exit
: ''').lower()

    if menu == 'r':

        # Check if username is "admin"
        if entered_username == "admin":

            # Request input for new username
            new_username = input("Please enter username ")

            # Request input for new password
            new_password = input ("Please enter password ")

            # password confirmation
            password_confirmation = input("Please confirm password ") 

            #Checking new password and confirmed password
            if new_password == password_confirmation:

            # Passwords match, add them to user.txt
                with open ("user.txt", "a") as file:
                    file.write(f"{new_username},{new_password}\n")
                    print("register user")

            else:
                print("Password confirmation incorrect. Please try again ")

        else: 
            print("Only 'admin' can register users. ")


    elif menu == 'a':
        # Request user task details

        username_task = input ("Please enter username of the person whom the task is assigned to: ")
        task_title = input(" Please enter title of the task: ")
        task_description = input("Please enter description of the task: ")
        task_due_date = input ("Please enter due date of the task: (date- month- year)") # date month is a number
        converted_time = datetime.strptime(task_due_date, "%d %m %Y")

        # Current date
        current_date = date.today() 
        current_date = current_date.strftime("%d %B %Y")
        print(current_date)

        #Open and write to tasks.txt
        with open ("tasks.txt", "a") as file:
            file.write(f"{username_task}, {task_title}, {task_description}, {task_due_date}, {current_date}, No\n")
        print("add task")

        
    elif menu == 'va':
        # Open and read file tasks.txt
        with open ("tasks.txt", "r") as file:

            # Read line in file
            for line in file:

                #Split line where comma and space is
                task_information = line.strip()
                task_information = line.split (", ")

                # Print results in the format shown in the Output 2 in the PDF
                print(f"Task assigned to: {task_information [0]}")
                print(f"Title: {task_information [1]}")
                print(f"Description: {task_information [2]}")
                print(f"Due Date: {task_information [3]}")
                print(f"Date Assigned: {task_information [4]}")
                print(f"Completed: {task_information [5]}\n")
              

    elif menu == 'vm':

        # Username of user logged in
        user_logged_in = entered_username
        # Open and read file tasks.txt
        with open ("tasks.txt", "r") as file:
            for line in file:
                task_info = line.strip ()
                task_info = line.split (", ")

                # Check if username matches user logged in 
                if task_info [0] == user_logged_in:
                    print(f"Task assigned to: {task_info [0]}")
                    print(f"Title: {task_info [1]}")
                    print(f"Description: {task_info [2]}")
                    print(f"Due Date: {task_info [3]}")
                    print(f"Status: {task_info [4]}")
                    print("...........................................")

    # Only for when username is 'admin'               
    elif menu == 'sd':
        if entered_username == "admin":

            # Statistics display, need to open user.txt file and count total lines
            with open ("user.txt", "r") as file:
                total_num_users = 0
                for line in file:
                    total_num_users += 1
                
            # Statistics display, need to open tasks.txt file and count total lines
            with open ("tasks.txt", "r") as file: 
                total_num_tasks = 0
                for line in file:
                    total_num_tasks += 1

            print("Total number of users:", total_num_users)
            print("Total number of tasks:", total_num_tasks)

        else:
            print("Only 'admin' can view statistics display ")

                    
    elif menu == 'e':
        print('Goodbye!!!')
        exit()  # Breaks the while loop as the program exits.

    else:
        print("You have made entered an invalid input. Please try again")
