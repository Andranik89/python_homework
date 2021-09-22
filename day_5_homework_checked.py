import random
"""DATA STRUCTURES"""

# 1. Write a program to multiply all the items in a list.
# Գրել ծրագիր, որը կբազմապատկի լիստի բոլոր թվերը։
#
numb_1 = int(input('Enter number: '))
lst = [2, 3, 5, 7, 'test']
count_1 = 0
for i in lst:
    if type(i) == int or type(i) == float:  # Տիպը ստուգելուց աշխատեք օգտագործել isinstance ֆունկցիան
        lst[count_1] = lst[count_1] * numb_1
    count_1 += 1
print(lst)

### &&
list_value = 1
for i in lst:
    if type(i) == int or type(i) == float:
        list_value *= i
print(list_value)

# 2. Write a program to count the number of strings where the string length is 2 or more and the first and last
# character are same from a given list of strings.
# Գրել ծրագիր, որը կհաշվի լիստում եղած 2 կամ ավել երկարություն ունեցող լիստերի քանակը, որոնց առաջին և վերջին տառերը
# նույնն են։

# Պահանջը սխալ եք հասկացել։ Պետք է սթրինգերի լիստ լինի, օրինակ՝ ['string', 'other string', 'some other string', 'sting']
lst_2 = [['a', 'c', 'd', 'a'], 5, [5, 4, 6, 5], ['d', 'k', 'd'], ['t'], ['a', 'p'], ['a', 'a']]

lst_count = 0

for i in lst_2:
    if type(i) != list or len(i) < 2 or i[0] != i[-1] or type(i[0]) != str:
        continue
    lst_count += 1
    print(i[0], i[-1], lst_count)

# 3. Write a program that will remove duplicates from a list. DO NOT use set() method directly on the list.
# Գրել ծրագիր, որը կջնջի դուպլիկատները լիստից։ ՉՕԳՏԱԳՈՐԾԵԼ set() մեթոդը։

lst_3 = [2, 3, 4, 5, 2, 3, 4, 5, 7, 9, 5, 11]
temp_lst = lst_3.copy()
new_lst_3 = []
for i in range(len(lst_3)):
    temp_lst.pop(0)
    if lst_3[i] not in temp_lst:
        new_lst_3.append(lst_3[i])

print(new_lst_3)

# 4. Create a list from 5 user inputs.
# Ստեղծել լիստ 5 ներմուծված թվերից
new_list_input = []
for i in range(5):
    new_list_input.append(int(input(f"Enter the list element - {i + 1} : ")))
print(new_list_input)


# 5. Write a program to print the given list after removing the 2nd, 4th and 5th elements.
# Գրել ծրագիր, որը կջնջի տրված լիստի 2-րդ, 4-րդ և 5-րդ էլեմենտները։

lst_5 = ['Rock', 'Pop', 'Metal', 'Hip-Hop', 'Rap']

for i in [2, 4 - 1, 5 - 2]:
    lst_5.pop(int(i-1))  # Այստեղ int()-ի իմաստը չկա, i-ն արդեն թվային լիստի միջից է

print(lst_5)



# 6. Given a list of ints, print True if the array contains a 2 next to a 2 somewhere.
# Գրել ծրագիր, որը կտպի True, եթե տրված լիստում ինչ-որ տեղ 2 թվին 2 է հաջորդում։

lst_6 = [1, 2, 3, 4, 7, 9, 6, 2, 3, 2, 2]
n = 0
for ls_6 in lst_6:  # ls_6-ը ինչի՞ համար է։ Ոչ մի տեղ չի օգտագործվում
    if lst_6[n] == 2 and n < len(lst_6) - 1 and lst_6[n + 1] == 2:
        print('True')
    n += 1

# 7. Given a list of ints, print True if every element is a 1 or a 4, and False otherwise.
# Գրել ծրագիր, որը կտպի True, եթե լիստի բոլոր էլեմենտները 1 կամ 4 են։ Հակառակ դեպքում տպել False:
lst_7 = [1, 4, 1, 4, 1, 4, 5]
list_status = "True"
for elem in lst_7:
    if elem != 1 and elem != 4:
        list_status = 'False'

print(list_status)

# 8. Ask for user input and add that input as a key into the dictionary. If the key exists, warn the user about it and
# do nothing. Assign some arbitrary value to it.
# Պահանջել ներմուծել բանալի և ավելացնել այդ բանալին dictionary-ի։ Եթե այն արդեն գոյություն ունի, տպել, որ բանալին արդեն
# կա և ոչինչ չանել։ Որպես արժեք տեղադրել պատահական օբյեկտ

# Այստեղ պահանջ չկա, որպեսզի key-երը նույն տիպի լինեն։
dict_8 = {i: i**2 for i in set(range(5))}
type_d = type(list(dict_8.keys())[0])
input_key = type_d(input('Enter key: '))

if input_key in list(dict_8.keys()):
    print("բանալին արդեն կա")
else:
    dict_8[input_key] = random.random()

print(dict_8)

# 9. Loop through the values of a dictionary and add them to a new list.
# Ցիկլի միջոցով ավելացնել dictionary—ի արժեքները նոր լիստի մեջ։
dict_9 = {i: i ** 2 for i in list(range(5))}
list_9 = []
for j in dict_9:  # Կարող ենք նաև գրել for j in dict_9.values():
    list_9.append(dict_9[j])
print(list_9)

# 10. Write a script to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are square of keys.
# Գրել ծրագիր, որը կստեղծի և կտպի dictionary, որի բանալիները [1,15] թվերն են, իսկ արժեքները դրանց քառակուսիները։

dict_10 = {i: i**2 for i in {1, 15}}  # 1-15 բոլոր թվերը պետք է լինեն
print(dict_10)
