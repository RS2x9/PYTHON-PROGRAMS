'''A DICTIONARY CONTAINS DETAILS OF TWO WORKERS WITH THEIR NAMES AS KEYS AND OTHER DETAILS IN FORM OF
DICTIONARY AS VALUE.WRITE A PROGRAM TO PRINT THE WORKERS INFORMATION IN RECORD FORM  '''
employees={'John':{'age':25,'salary':20000},'Diya':{'age':35,'salary':50000}}
for key in employees:
    print('Employee name:',key)
    print('age:',employees[key]['age'])
    print('salary:',employees[key]['salary'])
