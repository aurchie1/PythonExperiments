from calendar import weekday
import datetime
from math import e



class person:
    def __init__(self, name, DOB, gender):

        self.DOB = datetime.datetime.strptime(DOB, "%m-%d-%Y").date()
        self.name = str(name)
        self.gender = gender

    def __str__(self):
        return f"{self.name} was born {self.DOB} and is {self.gender}"
    
 
    
rich = person("Rich", "10-13-1952", "Male")

print(rich.DOB)

futureDate = datetime.date.today().__add__(datetime.timedelta(days=180))
print(futureDate.weekday())
print(futureDate)


#print(dir(datetime.date))

#if datetime.date.today() == datetime.date.today().weekday():
#    print("Its a weekday")

#else:
#    print("Its a weekend")
#