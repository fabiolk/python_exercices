# Read 3 double numbers (A, B and C) representing the sides of a triangle and arrange them in decreasing order, so that the side A is the biggest of the three sides. Next, determine the type of triangle that they can make, based on the following cases always writing an appropriate message:
# if A ≥ B + C, write the message: NAO FORMA TRIANGULO
# if A2 = B2 + C2, write the message: TRIANGULO RETANGULO
# if A2 > B2 + C2, write the message: TRIANGULO OBTUSANGULO
# if A2 < B2 + C2, write the message: TRIANGULO ACUTANGULO
# if the three sides are the same size, write the message: TRIANGULO EQUILATERO
# if only two sides are the same and the third one is different, write the message: TRIANGULO ISOSCELES
# Input
# The input contains three double numbers, A (0 < A) , B (0 < B) and C (0 < C).

# Output
# Print all the classifications of the triangle presented in the input.




inpt = input().split(' ')

inpt_1 = float(inpt[0])
inpt_2 = float(inpt[1])
inpt_3 = float(inpt[2])

aux = (inpt_1, inpt_2, inpt_3)

x = sorted(aux, reverse = True)

A = x[0]
B = x[1]
C = x[2]

# print(A,B,C)
if A >= (B + C):
    # print(A, (B + C))
    print('NAO FORMA TRIANGULO')
else:
    if A**2 == (B**2 + C**2):
        # print(A**2, (B**2 + C**2))
        print('TRIANGULO RETANGULO')
    if A**2 > (B**2 + C**2):
        # print(A**2, (B**2 + C**2))
        print('TRIANGULO OBTUSANGULO')
    if A**2 < (B**2 + C**2):
        # print(A**2, (B**2 + C**2))
        print('TRIANGULO ACUTANGULO')
    if (A == B) and (A == C):
        # print((A == B), (A == C))
        print('TRIANGULO EQUILATERO')
    if (A == B) and (A != C):
        # print((A == B), (A != C))
        print('TRIANGULO ISOSCELES')
    if (A == C) and (A != B):
        # print((A == C), (A != B))
        print('TRIANGULO ISOSCELES')
    if (B == C) and (B != A):
        # print((B == C), (B != A))
        print('TRIANGULO ISOSCELES')

