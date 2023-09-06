class employee():
    def appendemployeevalues(self):                 # Here we are definining the instance method 
        print("Iam from appendemployeevalues()")
        print("-"*50)
        self.eno=100
        self.ename="Anji"
        self.sal=12000
        self.desg="Data Scientist"
        print("-"*50)
        
        
# main program
eo1=employee()
print("id of eo1:",id(eo1))
print("content of eo1 before calling append function:",eo1.__dict__)
eo1.appendemployeevalues()
print("content of eo1 after calling append function:",eo1.__dict__)