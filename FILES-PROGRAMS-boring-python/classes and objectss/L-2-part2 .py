# defining a function in class
class person:
    name='sagar'
    occupation='software developer'
    def info(self):   
        print(f"{self.name} is a {self.occupation}")
a=person()
a.info()

print()
# lets change some values
a.name='Sagar'
a.occupation='softwarere'
a.info()

print()
b=person()
b.name='kumar'
b.occupation='hr'
b.info()
