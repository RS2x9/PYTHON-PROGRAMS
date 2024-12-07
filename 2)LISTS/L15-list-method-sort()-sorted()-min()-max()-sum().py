                                  #LIST FUNCTION AND METHOD
                                         #sort()
#ARANGES THE ELEMENTS IN INCREASING OR DECREASING ORDER:  ARRANGS IN LEXOGRAPHICAL ORDERING ie ASCII VALUES
#NO NEW LIST IS CREATED
t1=['e','i','q','a','q','p']
t1.sort()
print(t1)
t1.sort(reverse=True)  #PRINTS THE ELEMENTS IN REVERSE ORDER
print(t1)
t1.sort(reverse=False)   #PRINTS THE ELEMENTS IN ASCENDING ORDER
print(t1)
print()

                                   #sorted()
#FOR ARRANGING IN ASCENDING AND DESCENDING ORDER AND TO CREATE A NEW LIST
val=[17,24,15,30]
sval=sorted(val)  #ARRANGES THE ELEMENTS IN ASCENDING RDER
print('val:',val)
print('sval:',sval)
print('id of val:',id(val),',','id of sval:',id(sval))
rsval=sorted(val,reverse=True)
print('rsval:',rsval)
print()

                                 #min()
#RETURNS WHOSE VALUE IS MINIMUM
L=[1,1,1,1,5.0]
print('min in L:',min(L))
                                #max()
#RETURNS WHOSE VALUE IS MAXIMUM
print('max is:',max(L))
                               #sum()
#RETURNS SUM OF ALL THE ELEMENTS OF THE LIST
print('sum is :',sum(L))
