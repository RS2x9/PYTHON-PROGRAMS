#GUESS-THE-NUMBER-PROGRAM
               #RISHABH SINGH(4SI23EC062)
import random
print('HELLO THERE! \n EATEN BREAKFAST TODAY!!!')
ran=random.randint(0,10)
i=0
while i<6:
    guess_num=int(input('GUESS THE NUMBER:'))
    if guess_num!=ran:
        if i<5:
            if guess_num<ran:
                print('OPPS!! LOW GUESS')
            else:
                print('OOPS!! DIFFERENCE IS HIGH')
        else:
            print('the randomly choosed number was:',ran)
    else:
        print('WOW! YOU GUESSED IT RIGHT')
        break
    i=i+1
    
    
