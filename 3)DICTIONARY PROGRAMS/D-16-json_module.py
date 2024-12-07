# if we wanted to print the pair of dictionary in different lines then use dumps() of json module
#json.dumps(<dictionary>,indent=2)  n=number of spaces in front of every line
import json
winners={'nihar':3,'rohan':5,'zeba':3,'roshan':1,'james':5}
print(json.dumps(winners,indent=2)) ; print('now see the magic')
print(json.dumps(winners,indent=10))   # see the difference
