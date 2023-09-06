class student: pass    # Here student is prigrmmer defind data type
#    crs="Python"    # Here crs is class level data member & memory space created only once


student.crs="Python"  # Here class level data member defining out side of class
#main program
s1=student()
print("id of s1 object:",id(s1))
s1.sno=20       # Here sno,sname,marks are object level/ instance data members of s1 object only
s1.sname="Raju"  # These memory space is created every time
s1.marks=56.35
print("{}\t{}\t{}\t{}\t class level data member access through object(s1.) name".format(s1.sno,s1.sname,s1.marks,s1.crs))
print("{}\t{}\t{}\t{}\t class level data member access through class(student) name".format(s1.sno,s1.sname,s1.marks,student.crs))
#print("content of s1:",s1.__dict__)
print("-"*50)
s2=student()            # Here sno,sname,marks are object level/instance data members of s2 object only
s2.sno=30                
s2.sname="chiru"
s2.marks=80.5
print("id of s2 object:",id(s2))
print("{}\t{}\t{}\t{}\t class level data member access through class(student) name".format(s2.sno,s2.sname,s2.marks,student.crs))
print("{}\t{}\t{}\t{}\t class level data member access through object(s2.) name".format(s2.sno,s2.sname,s2.marks,s2.crs))
#print("content of s2 object:",s2.__dict__)
print("-"*50)
s3=student()
print("content of s3=",s3.__dict__)
print("id of s3 object",id(s3))
print("-"*50)
