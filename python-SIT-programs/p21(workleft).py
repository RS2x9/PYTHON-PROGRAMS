#this program has some mistaks
def spam():
    eggs='spam local'
    print(eggs)
def bacon():
    eggs='bacon local'
    print(eggs)
    spam()
    print(eggs)
    eggs='global'
    bacon()
    print(eggs)
