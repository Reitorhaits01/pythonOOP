class Person():
    def __init__(self,age,fname,lname,gender):
        self.age = age
        self.fname= fname
        self.lname= lname
        self.gender = gender

    def fullname(self):
        allnames= f"{self.fname} {self.lname}"
        return allnames
    
    def yearofbirth(self, year):
        return year - self.age

person1 = Person(23,"tumu","eve","female")
person2= Person(34,"nuwa","hape","male")
# print(person1.fullname())
# print(person2.yearofbirth(2024))

class Customer():
    def __init__(self,name,goodsbought,price,):
        self.name= name
        self.goodsbought= goodsbought
        self.price= price

    def totalamount(self):
        totalamount= self.price * self.goodsbought
        return totalamount

    def receipt(self):
        customername= f"Customer Name: {self.name}\n"
        goodsbought=f"Goods Bought: {self.goodsbought}\n"
        price=f"Price: {self.price}\n"
        totalamount= f"Total Amount: {self.totalamount()}\n"
        
        print(customername, goodsbought,price, totalamount)

customer1= Customer("ee", 5, 3000)
print(customer1.receipt())


# print(customer1.totalamount())