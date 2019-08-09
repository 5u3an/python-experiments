a=0
b=0
while True:
  r = input("enter the direction step: ")
  if not r:
    break
  dir, steps = r.split(' ')
  if dir == "left":
      a = a - int(steps)
  elif dir == "right":
      a = a + int(steps)
  elif dir == "up":
      b = b + int(steps)
  elif dir == "down":
      b = b - int(steps)
  else:
    pass
distance = (a**2 + b**2)**(1/2)
print("the output is: ",int(distance))
