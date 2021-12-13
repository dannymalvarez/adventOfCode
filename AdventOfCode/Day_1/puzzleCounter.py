data = []
inputs = open('input.txt','r')
datum = inputs.read()
counter = 0 
datumb = datum.split('\n')
data.append(datumb)
data = data.pop()

data.remove('')
   
for i in range(0, len(data)):
  data[i] = int(data[i])

counter = 0
for i in range(0, len(data)):
  a = data[i]
  b = data[i+1]
  if b > a:
    counter += 1
    print(counter)
# Answer is 1766, also I get a fun error once it finishes running
#Traceback (most recent call last):
#  File "/Users/danielalvarez/Desktop/Fun_Projects/AdventOfCode/Day_1/puzzleCounter.py", line 17, in <module>
#    b = data[i+1]
#IndexError: list index out of range
