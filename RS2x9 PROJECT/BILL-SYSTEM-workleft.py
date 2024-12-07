import pprint 
print("Hello Costomer!!!".center(80))
print()
H_Foods={"SOUP":
         {'1.Sweet Corn Soup':40.00,'2.Vegetable Soup':50.00},
         "STARTER(NONVEG)":
         {'1.Chicken65':80.00,'2.Chicken Chilly':75.00,'3.Chicken Manchurian':75.00},
         "TANDOOR(NONVEG)":
         {'1.Tandoori Chicken':210.00,'2.Kabab':130,'3.Chicken Tikka':100}}
pprint.pprint(H_Foods) ; print()

so=int(input('1. SOUP: or 0.exit'))  ; print()
def soup() :
    global s1 ; s1=0
    while True:
        a=int(input('''1. Sweet corn soup at 40.00:
2. Vegetable soup at 50.00:
0. exit''')) ; print()
        quantity=int(input('How many?'))     # how many orders for same food
        print()
        if a==1:
            s1=s1+(H_Foods["SOUP"]['1.Sweet Corn Soup'] )*quantity
        if a==2:
            s1=s1+(H_Foods["SOUP"]['2.Vegetable Soup'])*quantity
        if a==0 or quantity==0:
            break
    print('Total soup AMOUNT:',s1) ; print()
    
if so==1:
    soup()
elif so==0:
    break

sn=int(input('Enter 2 To select STARTER(NONVEG):'))  ; print()
def starter_nveg() :
    global s2 ;s2=0
    while True:
        print('''1. for Chicken65 at 80.00:
2. Chicken Chilly at 75.00:
3. Chicken Manchurian at 75.00:
0. exit''') ; print()
        a=int(input())
        quantity=int(input('How many'))     # how many orders for same food
        print()
        if a==1:
            s2=s2+(H_Foods["STARTER(NONVEG)"]['1.Chicken65'])*quantity
        if a==2:
            s2=s2+(H_Foods["STARTER(NONVEG)"]['2.Chicken Chilly'])*quantity
        if a==3:
            s2=s2+(H_Foods["STARTER(NONVEG)"]['3.Chicken Manchurian'])*quantity
        if a==0 or quantity==0:
            break
    print('Total STARTER(NONVEG) AMOUNT:',s2) ; print()
if sn==2:
    starter_nveg()
    
tn=int(input('Enter 3 to select TANDOOR(NONVEg):'))   ; print()
def tandoor_nveg() :
    global s3 ; s3=0
    while True:
        print('''1. Tandoori Chicken at 210.00:
2.Kabab at 130 :
3. Chicken Tikka at 100 :
0. exit''') ; print()
        a=int(input())
        quantity=int(input('How many?'))     # how many orders for same food
        print()
        if a==1:
            s3=s3+(H_Foods["TANDOOR(NONVEG)"]['1.Tandoori Chicken'])*quantity
        if a==2:
            s3=s3+(H_Foods["TANDOOR(NONVEG)"]['2.Kabab'])*quantity
        if a==3:
            s3=s3+(H_Foods["TANDOOR(NONVEG)"]['3.Chicken Tikka'])*quantity
        if a==0 or quantity==0:
            break
    print('Total TANDOOR(NONVEG) AMOUNT:',s3) ; print()
if tn==3:
    tandoor_nveg()
    
print('PAYBLE AMOUNT:',s1+s2+s3)
