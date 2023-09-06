class employee():
    
    @classmethod   # defining class level method
    def appendcomname(cls):
        cls.cname="IBM"
    
    
    def appendemployeevalues(self):                 # Here we are definining the instance method 
        print("Iam from appendemployeevalues()")
        print("-"*50)
        print("id of method is:{}".format(id(self)))
        self.eno=int(input("Enter emp number="))
        self.ename=input("enter empname=")
        self.sal=float(input("enter emp salary="))
        self.desg=input("enter emp desg=")
        print("-"*50)
       
    def displayresult(self):
        print("id of method is:{}".format(id(self)))
        print("emp number is :{}".format(self.eno))
        print("emp name is:{}".format(self.ename))
        print("emp salary is:{}".format(self.sal))
        print("emp desg is:{}".format(self.desg))
        print("emp compname is:{}".format(self.cname))
    
employee.appendcomname()   # class level method calling through class name   
# main program
eo1=employee()
eo1.appendemployeevalues()
print("-"*50)
print("id of eo1 in main prog is:{}".format(id(eo1)))

print("content of eo1 after calling append function:",eo1.__dict__)
eo2=employee()
eo2.appendemployeevalues()
print("-"*50)
print("id of eo1 in main prog is:{}".format(id(eo2)))
print("content of eo2 after calling append function:",eo2.__dict__)

print("-"*50)
eo1.displayresult()
print("-"*50)

eo2.displayresult()