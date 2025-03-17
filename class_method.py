# Quest 1:= Create student class that takes name and marks of 3 subject as 
#         arguments in constructor. 
#         then create a method to print the average.

class Students:
    def __init__(self,name,business,economics, accounts):
        self.name = name
        self.business = business
        self.economics = economics
        self.accounts = accounts
        print("This is your final year marks sheet := ")

    def your_name(self):
        print("welcome student", self.name)

    def avg_marks(self, avg):
        self.avg = avg
        avg = self.business + self.economics + self.accounts
        total_avg = avg / 3
        print("Your Total avg is := ", total_avg)
        print("You pass your exames ")


s1 = Students("Anurag",55,67,96)

print(s1.name,"Your marks in business := ", s1.business,"Your marks in economics := ",s1.economics,"Your marks in account := ",s1.accounts)

s1.your_name()
s1.avg_marks(s1)

s2 = Students("Piyush",78,84,93)
print(s2.name,"Your marks in business := ", s2.business,"Your marks in economics := ",s2.economics,"Your marks in account := ",s2.accounts)

s2.your_name()
s2.avg_marks(s2)


#  or =============================================================================================================================================

class sage_students:
    def __init__(self,name,marks):              #in this method we save the marks in list like := [55,76,84]
        self.name = name
        self.marks = marks
        print("Hello", self.name)

    @staticmethod                              # i used staticmethod too in this solu
    def welcome():
        print("You pass the exam congs")

    def final_avg(self):
        sum = 0
        for i in self.marks:
            sum = i + sum
            avg = sum / 3
        print("Your avg marks is  := ",avg)


gadha1 = sage_students("Mohan", [64,66,80])
gadha1.final_avg()
gadha1.welcome()


# Great! Here are *10 Python class method questions*, progressing from basic to advanced:  

# ### *Basic Level*  
# 1️⃣ **Create a class Car** with an instance attribute brand. Define a class method set_default_brand that sets a default brand for all car objects.
class car():
    brand_name = "TATA"
    def __init__(self,brand_name):
        self.brand_name = brand_name
        

car1 = car("BMW")
print(car1.brand_name)


# 2️⃣ **Create a Person class** with a class method from_birth_year that takes a birth year and returns an instance of Person with the calculated age. 


class persion():
    def __init__(self,name,birth_year):
        self.name = name
        self.birth_year = birth_year
        print("Hello", self.name)

    def year(self):
        count = self.birth_year
        age = 0
        while count <= 2025:
            age += 1
            count += 1
        final_age = age - 1
        print("Your are", final_age, "Year old")

p1 = persion("Monty", 2003)
print(p1.name)
p1.year()
            

# 3️⃣ **Create a class BankAccount** with an instance attribute balance. Use a class method to set a default interest rate for all accounts.
class BankAccount():
    interest_rate = 10
    year = 5
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
        print("Thank You", self.name,"Your deposite amount is := ", self.amount)

    def calculate(self):
        intereat_rate = (self.amount * self.year * self.interest_rate)/ 100
        final_balance = self.amount + intereat_rate
        print(self.name, "Your total interest after 5 year is := ",intereat_rate )
        print("And your total bank balance is ", final_balance)
        
b1 = BankAccount("Monty", 10000)
b1.calculate()

b2 = BankAccount("Ankit", 8000)
b2.calculate()

        
# 4️⃣ **Create a class TemperatureConverter** with a class method celsius_to_fahrenheit that converts Celsius to Fahrenheit.
class  Converter():
    def __init__(self,celsius):
        self.celsius = celsius

    def change(self):
        fahrenheit = (self.celsius * 9/5) + 32
        print("Your Room temperature in fehrenhit:= ", fahrenheit)
    
temp1 = Converter(25)
temp1.change()

# 5️⃣ **Create a Student class** with a class method from_string that takes a string formatted as "Name-Age-Grade" and returns a Student object.
class marks_sheet():
    def __init__(self, name, age, grade):
        self.name = name 
        self.age = age
        self.grade = grade 
        print("I will finding the data of ", self.name)
        print("Welcome", self.name,"This is your marks sheet")

    def list(self):
        final_sheet = [self.name, self.age, self.grade]
        print("Your final report card:=  ", final_sheet)
    

report1 = marks_sheet("Anurag", 19, "A")
report1.list()
          

