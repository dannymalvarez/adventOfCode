data = open("input.txt", "r")
printData = data.read()
x = printData.split()
forward = 0
depth = 0
length = len(x)
for i in range (0, length):
  if x[i] == "forward":
    forward += int(x[i+1])
  elif x[i] == "down":
    depth += int(x[i+1])
  elif x[i] == "up":
    depth -= int(x[i+1])
answer = forward * depth
print(answer)