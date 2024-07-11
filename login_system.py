# User input for username and password
# username = input("Please enter username: ")
# password = input("Please enter password: ")

# Open and write to the user.txt file     #Remove these lines
#with open("user.txt", "a") as file:
    #file.write(f"{username},{password}\n")

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
