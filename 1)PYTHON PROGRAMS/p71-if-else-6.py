''' program to display a menu for calculating area or perimeter of circle          '''

import math
print(''' press 1 for finding area of circle
press 2 for finding perimeter of circle''')
choice=int(input())
r=float(input('Enter radius of circle:'))
area=math.pi*math.pow(r,2)
per=2*math.pi*r
if choice==1 :
        print('area is:',area)
if choice==2 :
        print('perimeter is:',per)
else :
    print('enter valid choice number')
