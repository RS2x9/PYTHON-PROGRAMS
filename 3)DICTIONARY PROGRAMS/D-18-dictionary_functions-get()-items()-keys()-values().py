# <dictionary name>.get(key,[defaut]) :gives value of given key.if key is not present then python gives error.
# to stop this error message ,we can specify our message
empl1={'salary':10000,'dept':'sales','age':24,'name':'john'}
print("dictionary:",empl1)
print(empl1.get('dept'))
print(empl1.get('design','key is not present'))  #as design is not in dict,so defalut argument will be printed
print()

# <dictionary>.items()  : returns all key:value pair as a sequence of tuples
print(empl1.items())
#or
mylist=empl1.items()
for i in mylist:
    print(i)
    
print()

#<dictionary name>.keys()   : reurns all the keys
empl1={'salary':10000,'dept':'sales','age':24,'name':'john'}
print(empl1.keys())

print()

# <dictionary name>.values() :returns all the values associated with keys
empl1={'salary':10000,'dept':'sales','age':24,'name':'john'}
print(empl1.values())
