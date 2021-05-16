# Welcome Message
print("Welcome to Remaining age calculator\n")
# Get the current user age 
current_age = int(input("Enter your current age(in Years):\n"))
# Do some math and calculation
remaining_age = 90 - current_age
remaining_month = remaining_age * 12
remaining_weeks = remaining_age * 52
remaining_days = remaining_age * 365
# Print the result
print(f'You have {remaining_days:,} days, {remaining_weeks:,} weeks, {remaining_month:,} months and {remaining_age} years')