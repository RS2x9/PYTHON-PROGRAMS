                                        # STRING-METHODS
# STRINGS ARE IMMUTABLE
a='Harry'
print(len(a))

#upper()  :prints all characters in upper case
print(a.upper())

#lower()  :prints all characters in lower case
print(a.lower())
print()

#srtip()   : removes any characters before and after string
b="   Harry     "
print(b.strip())    #by default strip() removes spaces
c='!!!Harry!!!'
print(a.strip('!'))    # removal characters  can also be specified

# rstrip()   : removes trailling characters
print(c.rstrip('!'))

# lstrip()   :removes leading characters
print(c.lstrip('!'))

print()

# replace()  :replaces the occurences of characters with other characters
d='!!!Harry!!!Harry!!!!'
print(d.replace('Harry','John'))

# split()  : converts the string into List as shown. This is different from list()
e='!!! Harry !!! Harry !!!!'
f=e.split()
print(f)   #see the spaces carefully and formation of strings
print(e)   #original string will not change as strings are immutable

print()

# capitalize()  : converts the first letter into capital and others into small
srt1='hello'
print(srt1.capitalize())

# center()  :alings the string at the center at the given parameters
srt1='hello'
str2='Welcome to console'
print(len(str2))
print(str2.center(50))
print(len(str2.center(50)))   #to move the string right,number of characters added to left is(50-len(str2))

print()

# endswith()  :checks a given set of characters ends with specified character or not
print(str2.endswith('ole'))
print(str2.endswith('e'))

#find()   : searches for first occurences of given character and returns the index where it is present.
          #if character is/are absent it returns -1
str3="His's name is Don"
print(str3.find("is"))
print(str3.find('na'))

# index()   : retuns the index.it don't gives -1 when specified characters are absent
print(str3.index('s'))
print(str3.index('is'))
# print(str3.index('hello'))   # this raise an error

print()
# isalnum()  :returns True if A-Z,a-z,0-9 are present,otherwise it returns False
str3="His's name is Don"
d='!!!Harry!!!Harry!!!!'
print(str3.isalnum())
print(d.isalnum())
str4='jfgf'
print(str4.isalnum())

# isalpha()   :returns True if A-Z,a-z,otherwise False
str5='Welcome'
print(str5.isalpha())
str6='Welcome00'
print(str6.isalpha())

print()
# islower()   : returns True if all characters are small letters
print(str5.islower())

# isprintable()   : returns if all the characters are printable
str6='Welcome00'
print(str6.isprintable())
str7='Welcome\n'
print(str7.isprintable())   #False because \n is not printable character

# isspace()  : returns True if string contains white space,otherwise False
str6='Welcome00'
print(str6.isspace())

# istitle()   :returns True if all first letter of each letter is capital
str8='Welcome Home'
print(str8.istitle())

# isupper()   :returns True if all characers are in capital letters
print(str8.upper())

# stratswith()   : checks whether a given function starts with specified characters
print(str8.startswith('Wel'))

print()
# swapcase()  : changes from upper to lower case and vice versa
x='Hello'
print(x.swapcase())

# title()  :capitalizes 1st character of string and subsequent characters to lower case
w='heLlo'
print(w.title())
