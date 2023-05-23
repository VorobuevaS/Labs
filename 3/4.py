import random
o = 0
while o < 3:
  a = random.randrange(1, 10)
  b = random.randrange(1, 10)
  e = a + b
  print(a,"+",b,"=")
  print(e)
  u = int(input(" "))
  if e == u:
      print("Ответ верный")
  else:
      print("Ответ неверный")
      o = o + 1
