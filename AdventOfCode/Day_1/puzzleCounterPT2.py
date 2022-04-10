data = open("input.txt", "r")
printData = data.read()
x = printData.split()
counter = 0
length = len(x)
lengthEnd = length - 3
for i in range(0, lengthEnd):
  a = int(x[i]) 
  b = int(x[i+3])
  if b > a:
    counter = counter + 1
print(counter)
# answer is 1797
