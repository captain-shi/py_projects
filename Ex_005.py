#Exercise question available on codingbat.com/prob

#parrot_trouble
def parrot_trouble(talking, hour):
    
  if talking:
      
      if hour < 7 or hour > 20:
          
          return True
      
      else:
          
          return False
      
  else:
      
     return False

a = parrot_trouble(True, 5)

print(a)

b = parrot_trouble(True, 23)

print(b)

c = parrot_trouble(False, 5)

print(c)

d = parrot_trouble(True, 13)

print(d)