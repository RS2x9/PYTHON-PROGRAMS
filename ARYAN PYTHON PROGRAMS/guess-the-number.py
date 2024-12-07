import random
num=random.randint(0,10)
i=0
while i<6:
    guess=int(input("Enter your Guess:"))
    if guess!=num:
            if i<5:
                   if guess<num:
                          print("Too Low")
                   else:
                        print("Too High")
            else:
                   print("The number was",num)
    else:
        print("You got it right")
        break
    i+=1
        
        
        
