import math

print("The calculator supports rectangular shaped rooms, circular rooms, and L shaped rooms. ")
choice_valid = False
while not choice_valid:
  try:
    choice = input("Choose 'rectangle', 'circle', or 'L': ")
    if choice.lower() == 'rectangle' or 'circle' or 'l':
      choice_valid = True
    else:
      print("Choose 'rectangle', 'circle', or 'L'. ")
  except ValueError:
    print("Choose 'rectangle', 'circle', or 'L'. ")

if choice == 'rectangle':
  valid_input = False
  while not valid_input:
    try:
      length = input("Enter the length: ")
      width = input("Enter the width? ")
      if length.isdigit() and width.isdigit():
        length = int(length)
        width = int(width)
        if length > 0 and width > 0:
          valid_input = True
      else:
        print("Enter a positive numeric value. ")
    except ValueError:
      print("Enter a positive numeric value. ")

  area = length * width
  one_gallon = 350
  req_gallon = math.ceil(area / one_gallon)

  if req_gallon == 1:
    print(f"You will need to purchase {req_gallon} gallon of paint to cover {area} square feet. ")
  else:
    print(f"You will need to purchase {req_gallon} gallons of paint to cover {area} square feet. ")

elif choice == 'circle':
  circle_input = False
  while not circle_input:
    try:
      radius = input("Enter the radius: ")
      if radius.isdigit():
        radius = int(radius)
        if radius > 0:
          circle_input = True
      else:
        print("Enter a positive numeric value. ")
    except ValueError:
      print("Enter a positive numeric value. ")
  
  one_gallon = 350
  radius_square = radius ** 2
  area_circle = math.ceil(math.pi * radius_square)
  circle_req_gallon = math.ceil(area_circle / one_gallon)
  if circle_req_gallon == 1:
    print(f"You will need to purchase {circle_req_gallon} gallon of paint to cover {area_circle} square feet. ")
  else:
    print(f"You will need to purchase {circle_req_galrclon} gallons of paint to cover {area_circle} square feet. ")

elif choice == 'l':
  l_input = False
  while not l_input:
    try:
      left_side = input("Enter the side length of the left side of the L shaped room: ")
      top_side = input("Enter the side length of the top side of the L shaped room: ")
      middle_right_side = input("Enter the side length of the middle right side of the L shaped room: ")
      middle_top_side = input("Enter the side length of the middle horizontal side of the L shaped room: ")
      if left_side.isdigit() and top_side.isdigit() and middle_right_side.isdigit() \
      and middle_top_side.isdigit():
        left_side = int(left_side)
        top_side = int(top_side)
        middle_right_side = int(middle_right_side)
        middle_top_side = int(middle_top_side)
        if left_side > 0 and top_side > 0 and middle_right_side > 0 and middle_top_side > 0:
          l_input = True
      else:
        print("Enter positive numeric values. ")
    except ValueError:
      print("Enter positive numeric values. ")

  area_larger = left_side * top_side 
  area_smaller = middle_right_side * middle_top_side
  whole_area = area_larger + area_smaller 
  one_gallon = 350
  req_gallon_l = math.ceil(whole_area / one_gallon)
  if req_gallon_l == 1:
    print(f"You will need to purchase {req_gallon_l} gallon of paint to cover {whole_area} square feet. ")
  else:
    print(f"You will need to purchase {req_gallon_l} gallons of paint to cover {whole_area} square feet. ")