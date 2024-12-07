def spam(devideby):
    return 42/devideby
print(spam(2))
print(spam(12))
#print(spam(0))     # Zero Division Error
print()
# new code
try:
    print(spam(10))
    print(spam(0))
except ZeroDivisionError :
    print('invalid statement')

