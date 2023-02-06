
#Exercise question available on codingbat.com/prob
# sleep_in
def sleep_in(weekday, vacation):
  if not weekday or vacation:
      return True
  else:
      return False

x = sleep_in(True,False)

print(x)

z = sleep_in(False,True)

print(z)