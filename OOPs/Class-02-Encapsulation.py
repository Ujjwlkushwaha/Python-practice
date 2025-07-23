## Encapsulation - Process of bundling attributes and methods inside a single unit which is class.
##                  - Encapsulation also provide data security feature mean you can set visibility feature.
#                    - who can access your data and who can not.

# public members : when you create a class by defualt every attribute and methods are set to be public.

# Private member- these members are only accessible inside the class.
#                       - Private member start with "__";
#                       - If I wanted to accesss private member outside the class we have to make a public getter method
class Parent:

    def __init__(self,name, caste, salary):
        self.name = name     # Public instance attribute
        self.__caste = caste  # Private instance attribute
        self.__salary = salary # Private instance attribute


    def get_salary(self):
        return self.__salary

obj = Parent("Ujjwal" , "hindi" , 3333)
# print(obj.__salary) # Show error -  'Parent' object has no attribute '__salary 

# get private values using public method

salary = obj.get_salary()  # this way you can access private members
print(salary) # 3333



# Best Example ->   Create an account class with some attribute and create methods for debit credit and printing balance

class Account:

    bank_name = "State bank of india"

    def __init__(self):
        print("Account created successfully! ")


    def __init__(self, name, acc_no, acc_pass, acc_amt ):
        self.name = name
        self.__acc_no = acc_no
        self.__acc_pass = acc_pass # All details must be private 
        self.__acc_amt = acc_amt
        print("Account created successfully! ")


    def ower_details(self, acc_pass):
        if( acc_pass == self.__acc_pass):
            print(f"Owner Name : {self.name}\nAcc_no : {self.__acc_no}\nBank : {self.bank_name}")
        else:
            print("Pin is incorrect !! ")

    def get_balance(self, act_pass):
        if( act_pass == self.__acc_pass ):
            print(f"Name : {self.name}\nAcc_no : {self.__acc_no}")

    # debit amount
    def debit(self , amt , act_pass ):
        if( act_pass == self.__acc_pass ):
            self.__acc_amt -= amt
            print(f"Amount {amt} debited successfully !. Your current balance is {self.__acc_amt}")
        else:
            print("Pin is incorrect !")
            return
        
    # Crediting the amount 
    def credit(self , amt ):
        self.__acc_amt += amt
        print(f"Amount {amt} credited successfully !. Your current balance is {self.__acc_amt}")

    
        
acc1 = Account("ujjwal" , 123456, 1234 , 500000)

acc1.ower_details(1234) 

acc1.credit(500) # Amount 500 credited successfully !. Your current balance is 500500

acc1.debit(500 , 1234) # Amount 500 debited successfully !. Your current balance is 500000

# print( acc1.__acc_pass )  'Account' object has no attribute '__acc_pass

