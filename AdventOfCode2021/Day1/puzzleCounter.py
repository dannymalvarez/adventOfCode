data = open("input.txt", "r")
printData = data.read()
x = printData.split()
counter = 0
length = len(x)
lengthEnd = length - 1
for i in range(0, lengthEnd):
  a = int(x[i])
  b = int(x[i+1])
  if b > a:
      counter = counter + 1
print(counter)
# Answer is 1766
#This is a cleaner version of the solution and done in python which was my preferred language.
