valid_input = False
while not valid_input: 
  try: 
    length = input("What is the length of the room in feet? ")
    width = input("What is the width of the room in feet? ")
    if length.isdigit() and width.isdigit():
      length = int(length)
      width = int(width)
      if length > 0 and width > 0:
        valid_input = True
    else:
      print("Enter a positive numeric value. ")
  except ValueError:
    print("Enter a postive numeric value")

constant = 0.09290304
area_feet = length * width
area_metres = area_feet * constant
area_metres = round(area_metres, 3)
print(f"You entered dimensions of {length} feet by {width} feet. ")
print(f"The area is\n\
{area_feet} square feet\n\
{area_metres} square metres")