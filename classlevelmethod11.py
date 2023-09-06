class employee:
    @classmethod
    def addcompanyname(cls):
        cls.cname="TECH MAHINDRA"
        
    @classmethod
    def addcompanyaddress(cls):
        cls.companyadd="HYD"
        
    def appendvalues(self):
        self.empno=int(input("enter employee number:"))
        self.empname=input("enter employee name:")
        self.empsalary=float(input("enter employee salary:"))
        self.empdesig=input("enter employee designation:")
        
    def displayempvalues(self):
        print("emp number is:{}".format(self.empno))
        print("emp name is:{}".format(self.empname))
        print("emp salary is:{}".format(self.empsalary))
        print("emp desig is:{}".format(self.empdesig))
    
        # print("emp compname is:{}".format(self.cname))    # Here we are calling class level method throough class name
        # print("emp compname is:{}".format(employee.cname))  # Here we are calling class level method throough class name
        print("emp compaddress  is:{}".format(employee.companyadd)) # Here we are calling class level method throough class name
        print("emp compname is:{}".format(ep1.cname))  # Here we are calling class level method throough object name



employee.addcompanyname()   # Here we are calling class level data members thorugh class name
employee.addcompanyaddress()    # Here we are calling class level data members thorugh class name
#main program
ep1=employee()      # object creation for employee class
print("="*50)

ep1.appendvalues()
# ep1.addcompanyname()    # Here we are calling class level data members thorugh object name
# ep1.addcompanyaddress() # Here we are calling class level data members thorugh object name
print("="*50)


print("="*50)
ep2=employee()  # creating one more object for the employee class
# appending the values to the ep2 object with method calling
ep2.appendvalues()
# ep2.addcompanyname()
# ep2.addcompanyaddress()
print("="*50)
ep2.displayempvalues()
print("="*50)
ep1.displayempvalues()