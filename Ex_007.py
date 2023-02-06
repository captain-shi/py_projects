#Exercise question available on codingbat.com/prob

#not_string
def not_string(str):
    
  if str.startswith('not'):
      
    return str

  else:
      
    return 'not ' + str

T = not_string('not clear')

print(T)

F = not_string('clear')

print(F)