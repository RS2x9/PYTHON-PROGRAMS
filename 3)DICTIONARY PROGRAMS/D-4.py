#PROGRAM TO CREATE PHONE DICTIONARY FOR ALL MY FRIENDS AND PRINT EACH KEY VALUE PAIR IN SEPERATE LINES
D={}
name,number=[],[]
while True:
    na=input('Enter names or type next to enter numbers')
    if na=='next':
        break
    name.append(na)
while True:
    nu=input('Enter numbers or type next')
    if nu=='next':
        break
    eval(nu)
    number.append(nu)
print('Dictionary is:',end='')
for i in name:
    D[i]=number[name.index(i)]
print(D)
for key in D:
    print(key,':',D[key])
