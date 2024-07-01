valid_input = False
while not valid_input: 
  var = input("What is the input string? ")
  if var != "": 
    var_length = len(var)
    print(f'{var} has {var_length} characters.')
  else: 
    print('Enter a string')

    