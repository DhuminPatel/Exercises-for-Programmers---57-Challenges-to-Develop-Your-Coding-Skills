quote = input('What is the quote? ')
said = input('Who said it? ')
#My own addition (not needed)
if quote[-1] != '.':
  quote = quote + '.'
else: 
  pass
print(f'{said} says, "{quote}"')