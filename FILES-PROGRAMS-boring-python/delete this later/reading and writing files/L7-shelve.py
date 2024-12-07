# shelve module : this is a database where we can store values using dictionary
import shelve
with shelve.open('TestDB') as db:
    db['a']=1    # here a is key and 1 is value
    db['b']=2
    db['c']=3
# now retriving the vaues from database
with shelve.open('TestDB') as db:
    print(type(db))  # just ceheckig type of database
    print(db)
    print()
    print(dict(db))
    print(db['c'])

# to update the database
print()
data={'e':4,'f':5,'g':10}
with shelve.open('TestDB') as db:
    db.update(data)
    print(dict(db))
d={'a':100,'h':200}
with shelve.open('TestDB') as db:
    db.update(d)
    print(dict(db))
