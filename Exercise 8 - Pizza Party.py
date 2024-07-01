import math

print("Enter 'slice' or 'pizza'")
input_valid = False
while not input_valid:
  try:
    var = input("Would you like to use the slices calculator or pizzas calculator? ")
    var = var.lower()
    if var == 'slice' or var == 'pizza':
      input_valid = True
    else:
      print("Enter 'slice' or 'pizza'")
  except ValueError:
    print("Enter 'slice' or 'pizza'")
if var == 'slice':
  valid_input = False
  while not valid_input: 
    try:
      people_num = input("How many people? ")
      pizza_num = input("How many pizzas do you have? ")
      if people_num.isdigit() and pizza_num.isdigit():
        people_num = int(people_num)
        pizza_num= int(pizza_num)
        if people_num > 0 and pizza_num > 0:
          valid_input = True
      else:
        print("Enter a positive numeric value. ")
    except ValueError:
      print("Enter a positive numeric value. ")

  slices = pizza_num * 8
  pieces = slices // people_num
  remainder = slices % people_num

  print(f"{people_num} people with {pizza_num} pizzas")
  if pieces > 1:
    print(f"Each person gets {pieces} pieces of pizza\n\
  There are {remainder} leftover pieces.")
  else:
    print(f"Each person gets {pieces} piece of pizza\n\
  There are {remainder} leftover pieces.")

elif var == 'pizza':
  v_input = False
  while not v_input:
    try:
      num_people = input("Enter the number of people. ")
      num_slices = input("Enter the number of pieces each person wants. ")
      if num_people.isdigit() and num_slices.isdigit():
        num_people = int(num_people)
        num_slices = int(num_slices)
        if num_people > 0 and num_slices > 0:
          v_input = True
      else:
        print("Enter a positive numeric value.")
    except ValueError:
      print("Enter a positive numeric value.")

  one_pizza = 8
  total_slices = num_people * num_slices
  pizza_needed = math.ceil(total_slices / one_pizza)
  print(pizza_needed)