#TRAVERSING A DICTIONARY:  accessing and processing each element of it
d={5:'number',\
   'a':'string',\
   (1,2):'tuple'}      #we used \ to write in ,mutiple lines or we can write directly also
for key in d:
    print(key,':',d[key])
