'''
Anagram are strings that has same number of each character in both words.
'''
from collections import Counter
str1 = input("Enter String One : ")
str2 = input("Enter String Two :")
print( len(str1) -  len(str2) == 0 and len(Counter(str1) - Counter(str2)) == 0)


