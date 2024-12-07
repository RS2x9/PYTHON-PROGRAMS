#  FINDING CENTER OF RECTANGLE

    
class Point:
    x=3 ; y=4
blank=Point()

class Rectangle:
    ''' hi'''
box=Rectangle()
box.width=100 ; box.height=200
box.corner=Point()
box.corner.x=0
box.corner.y=0

def find_center(box):
    p=Point()
    p.x=box.corner.x+box.width/2
    p.y=box.corner.y+box.height/2
    return p

def print_point(p):
    print('(%g,%g)'% (p.x,p.y))

print_point(find_center(box))
