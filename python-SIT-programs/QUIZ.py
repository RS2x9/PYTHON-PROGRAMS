def main():
    print("1.QUIZ 2. ADD")
    o=input('Enter Choice:')
    if o=='1':
        stratquiz()
    if o=='2':
        addque()
        
def addque():
    file=open(r"C:\PYTHON PROGRAMS\python-SIT-programs\quizquestions.txt","w")
    while True:
        print()
        q=input("Enter Questions:")
        o=input("Enter options:")
        a=input("Enter Answer:")
        d=[q,"\n",o,"\n",a,"\n"]
        # writelines()  :write items of lists in file
        file.writelines(d)
        c=input("press d when done / press c for continue:")
        if c=="d" :
            break
        file.close()
        main()
def startquiz():
    file=open(r"C:\PYTHON PROGRAMS\python-SIT-programs\quizquestions.txt","a")
    s1=file.readlines()
    n=input('Enter Player Name')
    ctr=0    # question counter
    p=0      # total prize money
    LL=0     # life lines counter
    print()
    pm=[1000,10000,100000,300000,500000,7500000,10000000]   #pm:prize money
    pc=0        #pc: prize money counter
    while True:
        q=s1[0+ctr]
        o=s1[1+ctr]
        a=s1[2+ctr]
        print("Prize Money:",pm[pc])
        print()
        print(q)
        print(o)
        ans=input('Enter Answer:')
        if ans+"\n"==a:
            p=p+pm[pc]
            print()
            print("Congratulation ",pm[pc])
            print("Total prize:",p)
        else :
            p=p-pm[pc-1]
            LL=LL+1
            if LL==3:
                break
            print()
            print('Incoorect,Lost:',pm[pc-1])
            print('Total prize:',p)
        print()
        c=input("press d to continue / press c to continue")
        print()
        ctr=ctr+3
        pc=pc+1
        if c=="d":
            break
        print("total Points:",p)
        main()
main()
