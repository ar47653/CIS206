import re

test_1 = '''
ABCDEFabcdef123450
*&%@#!}{
'''

pattern = re.compile(r'[\w]')
matches = pattern.finditer(test_1)

print("1")
for match in matches:
    print(match)
print()


test_2_and_3 = '''
ab
abc
a
ab
abb
'''

pattern = re.compile(r'ab*')
matches = pattern.finditer(test_2_and_3)

print("2")
for match in matches:
    print(match)
print()

pattern = re.compile(r'ab+')
matches = pattern.finditer(test_2_and_3)

print("3")
for match in matches:
    print(match)
print()


test_4 = '''
aab_cbbbc
aab_Abbbc
Aaab_abbbc
'''

pattern = re.compile(r'[a-z]+_[a-z]+')
matches = pattern.finditer(test_4)

print("4")
for match in matches:
    print(match)
print()


test_5 = '''The quick brown fox jumps over the lazy dog.
 The quick brown fox jumps over the lazy dog.'''

pattern = re.compile(r'^[A-Za-z]+')
matches = pattern.finditer(test_5)

print("5")
for match in matches:
    print(match)
print()


test_6 = '''The quick brown fox jumps over the lazy dog.
Python Exercises.'''

pattern = re.compile(r'[\w]*z[\w]*')
matches = pattern.finditer(test_6)

print("6")
for match in matches:
    print(match)
print()

test_7 = '216.08.094.196'

replaced = re.sub(r'0', '', test_7)

print("7")
print(replaced)
print()


test_8_9 = 'The quick brown fox jumps over the lazy dog.'

print("8")
search_fox = re.findall(r'(fox)', test_8_9)
print(search_fox)
search_dog = re.findall(r'(dog)', test_8_9)
print(search_dog)
search_horse = re.findall(r'(horse)', test_8_9)
print(search_horse)
print()


print("9")
search_fox = re.search(r'fox', test_8_9)
print(search_fox)
print()


test_10a = 'Regular Expressions'
test_10b = 'Code_Examples'

print("10")
replace_space = re.sub(r' ', r'_', test_10a)
print(replace_space)
replace__ = re.sub(r'_', r' ', test_10b)
print(replace__)
print()


test_11 = 'https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/'

print("11")
pattern = re.compile(r'\d{2,4}')
matches = pattern.finditer(test_11)
for match in matches:
    print(match)
print()


test_12 = '''
The following example creates an ArrayList with a capacity of 50
elements. Four elements are then added to the ArrayList and the ArrayList
is trimmed accordingly.
'''

print("12")
pattern = re.compile(r'\b(a|e)\w*')
matches = pattern.finditer(test_12)
for match in matches:
   print(match)
print()


test_13 = 'Python Exercises, PHP exercises.'

print("13")
replaced = re.sub(r'\W', r':', test_13)
print(replaced)
print()


test_14 = '''
The following example creates an ArrayList with a capacity of 50
elements. Four elements are then added to the ArrayList and the ArrayList
is trimmed accordingly.
'''

print("14")
pattern = re.compile(r'\b(a|e)\w*')
matches = pattern.finditer(test_14)
for match in matches:
   print(match)
print()


test_15 = 'Python    Exercises'

print("15")
remove_spaces = re.sub(r'\s+', r'', test_15)
print(remove_spaces)
