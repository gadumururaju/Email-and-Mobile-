class employee():
    def appendemployeevalues(self):                 # Here we are definining the instance method 
        print("Iam from appendemployeevalues()")
        print("-"*50)
        self.eno=int(input("Enter emp number="))
        self.ename=input("enter empname=")
        self.sal=float(input("enter emp salary="))
        self.desg=input("enter emp desg=")
        print("-"*50)
    '''    
    def displayresult(self):
        print("emp number is:".format(self.eno))
        print("emp name is:".format(self.ename))
        print("eno salary is:".format(self.sal))
        print("eno desg is:".format(self.desg))
    '''
        
# main program
eo1=employee()
print("id of eo1:",id(eo1))
print("content of eo1 before calling append function:",eo1.__dict__)
eo1.appendemployeevalues()
print("content of eo1 after calling append function:",eo1.__dict__)
eo2=employee()
print("id of eo2:",id(eo2))
print("content of eo2 before calling append function:",eo2.__dict__)
eo2.appendemployeevalues()
print("-"*50)
print("content of eo2 after calling append function:",eo2.__dict__)

print("-"*50)