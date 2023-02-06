#Exercise question available on codingbat.com/prob

#monkey_trouble
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
      return True
  elif not a_smile and not b_smile:  
          return True
  else:
      return False
  
a = monkey_trouble(True, False)

print(a)

b = monkey_trouble(True, True)

print(b)

c = monkey_trouble(False, False)

print(c)