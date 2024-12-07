def spam():
    eggs=99
    bacon()
    print(eggs)
def bacon():
    ham=101
    eggs=0
spam()

#after calling spam() ,bacon() is also called ,but there is no print() in bacon()
# so only eggs=99 get printed
