"""LOOPS"""

# 1. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a nested loop.
# Օգտագործելով ցիկլեր, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։
matrix = []
temp = []
n = 0
for i in range(1, 10):

    temp.append(i**2)
    n += 1
    if n == 3:
        matrix.append(temp)
        temp = []
        n = 0
print(matrix)



# 2. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a list comprehension.
# Օգտագործելով comprehension, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։

a = [[i ** 2 for i in range(j - 2, j + 1)] for j in range(1, 10) if not j % 3]
print(a)

# 4. Count the number of 'b's in the given string. DO NOT use the count() method.
# Հաշվել տրված սթրինգում 'b'-երի քանակը։ Չօգտագործել count() մեթոդը։
nonsense = 'Blinking blindly, brainy Bob brings beautiful beer bottles beneath blue butterflies billowing brilliantly.'
b_count = 0
for char in nonsense:
    if char == 'b':
        b_count += 1
print(b_count)


# 5. Write a program that will print the factorial of n.
# Գրել ծրագիր, որը կտպի n թվի ֆակտորիալը։

number_1 = int(input('Enter Number: '))
value_f = 1
for i in range(1, number_1 + 1):
    value_f *= i
print(value_f)

