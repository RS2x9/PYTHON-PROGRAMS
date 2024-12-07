# PROGRAM TO WISH ACCORDING TO CURRENT TIME
import time
# strftime('%H:%M:%S')   : gives the current timings
tstamp=time.strftime('%H:%M:%S')    #H=hour,M=min,S=second
print(tstamp)
# print(type(tstamp))   tstamp is string type datatype
thour=int(time.strftime('%H'))
#print(thour)
tmin=int(time.strftime('%M'))
#print(tmin)
tsec=int(time.strftime('%S'))
thour>0
if thour<3 :
    print('Hello')
elif (thour>=3 and thour<12 ) and (tmin<=59 or tsec<=59):
    print('Good morning')
elif thour==12:
    print('Its noon time')
elif (thour>12 and thour<16) :
    print('Good afternoon')
elif (thour>=16 and thour<=19):
    print('Good evening')
else:
    print('Have a good day')
