#  JUST LIKE SWITCH IN C LANGUAGE WE CAN USE match case STATEMENTS in python
# match is used to match the value written infront of case
x=int(input('Enter any digit'))
match x :
    case 0:
        print('Monday')
    case 1:
        print('Tuesday')
    case 2:
        print('Wednesday')
    case 3:
        print('Thrusday')
    case _  if x!=4 :
        print('Enjoy')
#  I DNT KNOW WHY THIS IS GIVING ERROR
