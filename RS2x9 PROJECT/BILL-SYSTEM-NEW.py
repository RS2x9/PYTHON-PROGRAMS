import os
if not os.path.exists(r'C:\Users\hp\Desktop\PYTHON PROGRAMS\RS2x9 PROJECT\bill.txt'):
    os.mkdir(r"C:\Users\hp\Desktop\PYTHON PROGRAMS\RS2x9 PROJECT\bill.txt")
with open(r'C:\Users\hp\Desktop\PYTHON PROGRAMS\RS2x9 PROJECT\bill.txt','w') as a:
    a.write('HOME FOODS'.center(50))
    
JUICES={'MANGOE':20,'ORANGE':30,'LEMON':50,'POMOGRANATE':100}
INDIAN={'PURI BHAJI':100,'ALOO PARATHA':200,'IDLI':20,'PANEER':150}
NONVEG={'CHICKEN':200,'OMLET':50,'EGG ROLL':150}

H_Foods={'JUICES':JUICES,'INDIAN':INDIAN,'NON VEG':NONVEG}
print() ; print('HOME FOODS SERVES'.center(100)) ; print()
print('10% discount on total amount:1000'.upper()) ; print()
      
print('JUICES'.center(20)) ; print('MANGOE:',JUICES['MANGOE']) ; print('ORANGE:',JUICES['ORANGE'])
print('LEMON:',JUICES['LEMON']) ; print('POMOGRANATE:',JUICES['POMOGRANATE'])
print()
print('INDIAN'.center(20)) ; print('PURI BHAJI:',INDIAN['PURI BHAJI']) ; print('ALOO PARATHA:',INDIAN['ALOO PARATHA'])
print('IDLI:',INDIAN['IDLI']) ; print('PANEER:',INDIAN['PANEER'])
print()
print('NONVEG'.center(20)) ; print('CHICKEN:',NONVEG['CHICKEN']) ; print('OMLET:',NONVEG['OMLET'])
print('EGG ROLL:',NONVEG['EGG ROLL']) ; print()
s1,s2,s3=0,0,0
while True:
    ch=int(input(f' \n ENTER 1: JUICES \n ENTER2: INDIAN \n ENTER 3:NON VEG \n 0: exit ')) ; print()
    if ch==0:
        break
    if ch==1:
        with open(r'C:\Users\hp\Desktop\PYTHON PROGRAMS\RS2x9 PROJECT\bill.txt','a') as a :
            f1=f"JUICES \t PRICE \t QUANTITY \t NET PRICE"
            a.write(f" \n\n {f1}")
        
        while True:
            print() ; a=input(f'ENTER 1:MANGOE:20 \n ENTER 2:ORANGE:30 \n ENTER 3: LEMON:50 \n ENTER 4: POMOGRANATE:100 \n 0:exit ')
            chj=int(a)
            if chj==0:
                break
            if chj==1:
                quan=int(input('AT HOW MANY PLACES')) ; s1=s1+JUICES['MANGOE']*quan
                
                with open(r'C:\Users\hp\Desktop\PYTHON PROGRAMS\RS2x9 PROJECT\bill.txt','a') as a:
                    f2=f" \n MANGOE \t {JUICES['MANGOE']} \t\t {quan} \t\t {JUICES['MANGOE']*quan}"
                    a.write(f"{f2}")
                
            if chj==2:
                quan=int(input('AT HOW MANY PLACES')) ; s1=s1+JUICES['ORANGE']*quan

                with open(r'C:\Users\hp\Desktop\PYTHON PROGRAMS\RS2x9 PROJECT\bill.txt','a') as a:
                    f2=f" \n ORANGE \t {JUICES['ORANGE']} \t\t {quan} \t\t {JUICES['ORANGE']*quan}"
                    a.write(f"{f2}")
                
            if chj==3:
                quan=int(input('AT HOW MANY PLACES')) ; s1=s1+JUICES['LEMON']*quan

                with open(r'C:\Users\hp\Desktop\PYTHON PROGRAMS\RS2x9 PROJECT\bill.txt','a') as a:
                    f2=f" \n LEMON \t\t {JUICES['LEMON']} \t\t {quan} \t\t {JUICES['LEMON']*quan}"
                    a.write(f"{f2}")
            if chj==4:
                quan=int(input('AT HOW MANY PLACES')) ; s1=s1+JUICES['POMOGRANATE']*quan

                with open(r'C:\Users\hp\Desktop\PYTHON PROGRAMS\RS2x9 PROJECT\bill.txt','a') as a:
                    f2=f" \n POMOGRANATE \t {JUICES['POMOGRANATE']} \t\t {quan} \t\t {JUICES['POMOGRANATE']*quan}"
                    a.write(f"{f2}")
                
        print('Total juice amount:'.upper(),s1)

    if ch==2:
        with open(r'C:\Users\hp\Desktop\PYTHON PROGRAMS\RS2x9 PROJECT\bill.txt','a') as a :
            f1=f"INDIAN \t PRICE \t QUANTITY \t NET PRICE"
            a.write(f" \n\n {f1}")
        
        while True:
            print()
            a=input(f'ENTER 1: PURI BHAJI:100 \n ENTER 2:ALOO PARATHA:200 \n ENTER 3: IDLI:20 \n ENTER 4: PANEER:150 \n 0:exit ')
            chi=int(a)
            if chi==0:
                break
            if chi==1:
                quan=int(input('AT HOW MANY PLACES')) ; s2=s2+INDIAN['PURI BHAJI']*quan

                with open(r'C:\Users\hp\Desktop\PYTHON PROGRAMS\RS2x9 PROJECT\bill.txt','a') as a:
                    f2=f" \n PURI BHAJI \t {INDIAN['PURI BHAJI']} \t\t {quan} \t\t {INDIAN['PURI BHAJI']*quan}"
                    a.write(f"{f2}")
                
            if chi==2:
                quan=int(input('AT HOW MANY PLACES')) ; s2=s2+INDIAN['ALOO PARATHA']*quan

                with open(r'C:\Users\hp\Desktop\PYTHON PROGRAMS\RS2x9 PROJECT\bill.txt','a') as a:
                    f2=f" \n ALOO PARATHA \t {INDIAN['ALOO PARATHA']} \t\t {quan} \t\t {INDIAN['ALOO PARATHA']*quan}"
                    a.write(f"{f2}")
                
            if chi==3:
                quan=int(input('AT HOW MANY PLACES')) ; s2=s2+INDIAN['IDLI']*quan

                with open(r'C:\Users\hp\Desktop\PYTHON PROGRAMS\RS2x9 PROJECT\bill.txt','a') as a:
                    f2=f" \n IDLI \t\t {INDIAN['IDLI']} \t\t {quan} \t\t {INDIAN['IDLI']*quan}"
                    a.write(f"{f2}")
                
            if chi==4:
                quan=int(input('AT HOW MANY PLACES')) ; s2=s2+INDIAN['PANEER']*quan

                with open(r'C:\Users\hp\Desktop\PYTHON PROGRAMS\RS2x9 PROJECT\bill.txt','a') as a:
                    f2=f" \n PANEER \t {INDIAN['PANEER']} \t\t {quan} \t\t {INDIAN['PANEER']*quan}"
                    a.write(f"{f2}")
                
        print('Total INDIAN amount:'.upper(),s2)

    if ch==3:
        with open(r'C:\Users\hp\Desktop\PYTHON PROGRAMS\RS2x9 PROJECT\bill.txt','a') as a :
            f1=f"NONVEG \t PRICE \t QUANTITY \t NET PRICE"
            a.write(f" \n\n {f1}")
        while True:
            print() ; a=input(f'ENTER 1: CHICKEN:200 \n ENTER 2:OMLET:50 \n ENTER 3: EGG ROLL:150 \n 0:exit ') ; chn=int(a)
            if chn==0:
                break
            if chn==1:
                quan=int(input('AT HOW MANY PLACES')) ; s3=s3+NONVEG['CHICKEN']*quan

                with open(r'C:\Users\hp\Desktop\PYTHON PROGRAMS\RS2x9 PROJECT\bill.txt','a') as a:
                    f2=f" \n CHICKEN \t {NONVEG['CHICKEN']} \t\t {quan} \t\t {NONVEG['CHICKEN']*quan}"
                    a.write(f"{f2}")
                
            if chn==2:
                quan=int(input('AT HOW MANY PLACES')) ; s3=s3+NONVEG['OMLET']*quan

                with open(r'C:\Users\hp\Desktop\PYTHON PROGRAMS\RS2x9 PROJECT\bill.txt','a') as a:
                    f2=f" \n OMLET \t\t {NONVEG['OMLET']} \t\t {quan} \t\t {NONVEG['OMLET']*quan}"
                    a.write(f"{f2}")
            if chn==3:
                quan=int(input('AT HOW MANY PLACES')) ; s3=s3+NONVEG['EGG ROLL']*quan

                with open(r'C:\Users\hp\Desktop\PYTHON PROGRAMS\RS2x9 PROJECT\bill.txt','a') as a:
                    f2=f" \n EGG ROLL \t {NONVEG['EGG ROLL']} \t\t {quan} \t\t {NONVEG['EGG ROLL']*quan}"
                    a.write(f"{f2}")
                
        print('Total NONVEG amount:'.upper(),s3)
        
print('TOTAL AMOUNT:',s1+s2+s3)
total=s1+s2+s3
with open(r'C:\Users\hp\Desktop\PYTHON PROGRAMS\RS2x9 PROJECT\bill.txt',"a") as a:
    f3=f" \n \n TOTAL \t\t\t\t\t {total}"
    a.write(f3)
    
if total>=1000:
    print('NET WORTH:',total-(total*0.1))
    with open(r'C:\Users\hp\Desktop\PYTHON PROGRAMS\RS2x9 PROJECT\bill.txt',"a") as a:
        f3=f" \n NET WORTH \t\t\t\t {total-(total*0.1)}"
        a.write(f3)
