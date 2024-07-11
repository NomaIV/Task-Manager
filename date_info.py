from datetime import date

"""task_due_date_str = input("Please enter due date of the task (date-month-year): ")


# Parse the input string into a datetime object
task_due_date = datetime.strptime(task_due_date_str, "%d-%B-%Y")

# Format the datetime object as "18 December 2023"
formatted_due_date = task_due_date.strftime("%d %B %Y")

print("Formatted due date:", formatted_due_date)

"""

task_due_date = input ("Please enter due date of the task (date- month- year) ")

# current date
current_date = date.today()
print(current_date)

current_date = current_date.strftime("%d %B %Y")
print(current_date)