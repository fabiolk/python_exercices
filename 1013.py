# Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior". Use the following formula:

# maior ab = (a+b+abs(a-b))/2

# Input
# The input file contains 3 integer values.

# Output
# Print the greatest of these three values followed by a space and the message “eh o maior”.

val = input().split(' ')

a = int(val[0])
b = int(val[1])
c = int(val[2])

greatest_ab = ((a + b) + abs(a - b))/2
greatest_bc = ((b + c) + abs(b - c))/2

teste = ((greatest_ab + greatest_bc) + abs(greatest_ab - greatest_bc))/2

# print('{0} eh o maior'.format(teste))
print(int(teste), 'eh o maior')