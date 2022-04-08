#Work in Progress on repl.it
data = open("input2.txt", "r")
printData = data.read()
x = printData.split()
counter = 0
length = len(x)
lengthEnd = length - 1
for i in range(0, lengthEnd):
  if x[i] and x[i+1] and x[i+2]:
    sum = int(x[i]) + int(x[i+1]) + int(x[i+2])
    print(sum)
  #a = int(x[i])
  #b = int(x[i+1])
  #sum = a + b + c
  #if b > a:
   #   counter = counter + 1
#print(counter)
