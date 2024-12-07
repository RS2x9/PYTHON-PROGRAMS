# DICTIONARY FUNCTIONS AND METHODS
# len() :COUNT KEY:VALUE pair as one element
a={1:12,2:34,3:45}
print(len(a))
print()
# dict()  :creates dictionary

'''  CREATE A DICTIONARY WHERE KEY,VALUE PAIRS(ROLL,MARKS) VALUES ARE AVAILABLE
IN 3 DIFFERENT LISTS AS [1,67.8],[2,75.5],[3,72.5]  '''
# method-1
data=[[1,67.8],[2,75.5],[3,72.5]]
D=dict(data)
print('Created dictionary:',D)

print()
# method-2
M=dict(zip([1,2,3],[67.8,75.5,72.5]))
print('Created dctionary:',M)
