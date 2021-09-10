"""IF, ELIF, ELSE"""

# 1. Enter your name, then find the sum of the ASCII values of the letters in your name. If that number is larger than
# 500, print "I've got a great name!", and "I've got a fancy name!" otherwise.
# Ներմուծեք ձեր անունը և գտեք անվան տառերի ASCII արժեքների գումարը։ Եթե թիվը մեծ է 500-ից, տպել "I've got a great
# name!", իսկ հակառակ դեպքում՝ "I've got a fancy name!"։

fullname = str(input('Enter Full Name: '))
fullname = fullname.replace(' ', '')

fullnamne_ascii_value = 0
for i in fullname:
    i_value = ord(i)
    fullnamne_ascii_value += i_value


if fullnamne_ascii_value > 500:
    print("I've got a great name!")
else:
    print("I've got a fancy name!")


# 2. Ask the user for a movie title. If the title starts with a capital letter, print "Great title!", otherwise print
# "Titles start with capital letters...". If the input starts with a special character [!, @, #, $, %, ^, &], print "I
# doubt that this is a title.".
# Պահանջել ներմուծել ֆիլմի վերնագիր։ Եթե վերնագիրը սկսվում է մեծատառով, տպել "Great title!", հակառակ դեպքում տպել
# "Titles start with capital letters..."։ Եթե ներմուծվածը սկսվում է [!, @, #, $, %, ^, &] նշաններով, տպել "I doubt that
# this is a title."․

film_name = input("Enter Film Name: ")
symbol_list = list(r"!, @, #, $, %, ^, &")
if (film_name[0].upper() == film_name[0]) and (film_name[0].isalpha()) :
    print('Great title!')
elif film_name[0] in symbol_list :
    print('I doubt that this is a title.')
else :
    print('Titles start with capital letters...')


# 3. Ask the user to input his/her age. If the user is older than 18, than tell them they're eligible to vote. If they
# are younger than 18, tell them how many years do they have to wait.
# Հարցրեք օգտատիրոջ տարիքը։ Եթե նա 18 տարեկանից մեծ է, նրան տեղյակ պահեք, որ կարող է քվեարկել։ Հակառակ դեպքում ասեք, թե
# քանի տարուց նա կկարողանա դա անել։

age = int(input('Enter Your Age: '))
if age >= 18 :
    print('Դուք իրավունք ունեք քվեարկելու')
else :
    print('Դուք կարող եք քվեարկել ', 18 - age, 'տարի հետո')

# 4. Write a program that will tell us whether a given year is a leap year or not.
# Գրել ծրագիր, որը կտեղեկացնի, թե տրված տարին նահանջ է, թե ոչ։

year = int(input('Enter Year: '))

if year % 4 == 0:
    if not bool(year % 100):
        print(year, 'նահանջ տարի է')
    else:
        if bool(year % 400):
            print(year, 'նահանջ տարի է')
        else:
            print(year, 'սովորական տարի է')
else:
    print(year, 'սովորական տարի է')

# 5. Using 'random' module, generate a random number between -1000 and 1000. If the number is positive, print positive.
# If it's negative, print negative along with the absolute value of the number.
# Օգտագործելով random գրադարանը, գեներացնել [-1000,1000]-ը տիրույթում պատահական թիվ։ Եթե թիվը դրական է, տպել positive.
# Հակառակ դեպքում տպել negative և այդ թվի բացարձակ արժեքը։

import random

numb_1 = random.randrange(-1000, 1000)
print(numb_1)
if numb_1 <= 0:
    print('negative', abs(numb_1))
else:
    print('positive')
