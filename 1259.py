# Considering the input of non-negative integer values​​, sort these numbers ​​
# according to the following criteria: First the even in ascending order 
# followed by the odd in descending order.

# Input
# The first line of input contains a positive integer number N (1 < N <= 105). 
# This is the number of following input lines. The next N lines contain, 
# each one, a integer non-negative number.

# Output
# Print all numbers according to the explanation presented above. Each number
# must be printed in one line as shown below.

n = int(input())
num = list()
even = list()
odd = list()
for i in range(n):
  num.append(int(input()))
# print(num)
for j in range(n):
  if (num[j] % 2) == 0:
    even.append(num[j])
  else:
    odd.append(num[j])

even = sorted(even, reverse=False)
odd = sorted(odd, reverse=True)

for i in range(len(even)):
  print(even[i])

for i in range(len(odd)):
  print(odd[i])
