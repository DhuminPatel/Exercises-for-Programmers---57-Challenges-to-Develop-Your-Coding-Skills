import datetime

valid_input = False
while not valid_input: 
  try:
    age = input('What is your current age? ')
    retire_age = input('At what age would you like to retire? ')
    if age.isdigit() and retire_age.isdigit():
      age = int(age)
      retire_age = int(retire_age)
      if age > 0 and retire_age > 0:
        valid_input = True
    else:
      print("Enter a positive numeric value. ")
  except ValueError: 
    print("Enter a valid positive integer. ")

current_year = datetime.datetime.now().year
years_until_retirement = retire_age - age
retirement_year = current_year + years_until_retirement

print(f"You have {years_until_retirement} left until you can retire.\n\
It's {current_year}, so you can retire in {retirement_year}.")
