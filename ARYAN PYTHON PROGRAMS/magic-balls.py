import random
print("What's going on ?")
def answerNumber(a):
 if   a==1:
    return('good')
 elif a==2:
    return('Nice')
 elif a==3:
    return('Do Hard labour')
 elif a==4:
    return('poor')
 elif a==5 :
    return('outstanding')
 elif a==6:
    return('Awesome')
 elif a==7:
    return('Bad')
 elif a==8:
    return('goodnight')
 elif a==9:
    return('Byeeee')
r=random.randint(1,9)
print(answerNumber(r))


