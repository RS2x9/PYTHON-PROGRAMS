# STRING FORMATTINFG
letter1="Hey my name is {} and i am from {}"
name="Rishabh"
country="India"
print(letter1.format(name,country))      #format()  input name,country in letter
print(letter1.format(country,name))      # this prints as shown in output
# we want to input at correct places

print()
letter2=f"Hey my name is {name} and I am from {country}"    #here name & country are variables
print(letter2.format(country,name))
# if we wanted to show name,country in fstring as it is then
letter3=f" Hey my name is {{name}} and I am from {{country}}"
print(letter3)

print()
txt1="For only {price:.2f} dollars!"
print(txt1.format(price=49.100045))    # only two degits after decimal is printed
# performing same using fstring
price=49.108946
txt2=f"For only {price:.2f} dollars!"
print(txt2)

print()
print(f"{2*30}")
