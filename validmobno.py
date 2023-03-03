import re
while(True):
	mno=input("Enter Ur Mobile Number:")
	if(len(mno)==10):
		res=re.search("\d{10}" ,mno)
		while(True):
			if mno[0]!=0 or mno[0]!=1 or mno[0]!=2 or mno[0]!=3 or mno[0]!=4 or mno[0]!=5:
				print("starting number should be6-9 ")
				break;
			else:
				print("good")

		if(res!=None):
			print("Ur Mobile Number is Valid:")
			break;
		else:
			print("U Mobile Shoud not contains strs or symbols")
	else:
		print("Ur Mobile Must Contains 10 Digits only:")
print("successfully completed")