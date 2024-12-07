# print largest of three number
while True:
    a=float(input('enter 1st number:'))
    b=float(input('enter 2nd number:'))
    c=float(input('enter 3rd number:'))
    if b<a>c:
        print(a, 'is the greatest')
    elif a<b>c :
        print(b,' is greatest')
    elif a<c>b :
        print(c,'is greatest')
    elif a==b==c :
        print('all are equal')
