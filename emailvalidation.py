email=input("enter your email:")
k,j,d=0,0,0
if len(email)>=6:                                           #1
    if email[0].isalpha():                                  #2
        if( "@"in email) and (email.count("@")==1):         #3
            if (email[-4]==".") or (email[-3]=="."):        #4
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=='.' or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("email id don't contain space 5")
                else:
                    print("valid email...")
            else:
                print("email extension should be eaither .com or .in 4!")
        else:
            print("email id contain only @ symbol at once only. 3")
    else:
        print("starting should upper alphabet 2!")
else:
    print("wrong email id! please try again 1")