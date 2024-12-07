''' WRITE A PYTHON PROGRAM TO CREATE DICTIONARY,NAME OF COMPETITION WIINERS AS KEYS
AND NUMBER OF THEIR WINS AS VALUES '''
D={}
name,won=[],[]
while True:
    a=input('Enter name of winners or type next')
    b=eval(input('Enter number of win or type next'))
    if a=='next' or b=='next':
        break
    name.append(a)
    won.append(b)
for i in name:
    D[i]=won[name.index(i)]
print('Created dictionary:',D)
