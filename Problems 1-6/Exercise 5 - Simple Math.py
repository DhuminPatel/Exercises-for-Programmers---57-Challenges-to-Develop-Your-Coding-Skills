valid_input = False
while not valid_input:
  try:
    var = input("What is the first number? ")
    var2 = input("What is the second number? ")
    if var.isdigit() and var2.isdigit():
      var = int(var)
      var2 = int(var2) 
      if var > 0 and var2 > 0:
        valid_input = True
    else:
      print("Enter a positive numeric value. ")
  except ValueError:
    print("Enter a valid integer. ")

addition = var + var2
subtraction = var - var2
multiplication = var * var2
division = var / var2 

print(f'{var} + {var2} = {addition}\n\
{var} - {var2} = {subtraction}\n\
{var} 2* {var2} = {multiplication}\n\
{var} / {var2} = {division}')