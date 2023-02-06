#Exercise question available on codingbat.com/prob

#makes10
def makes10(a, b):
    
  if a == 10 or b == 10:
      
      return True
  
  elif a + b == 10:
      
       return True
   
  else:
      
    return False

x = makes10(1, 7)

print(x)

b = makes10(10, 5)

print(b)

n = makes10(6, 4)

print(n)
