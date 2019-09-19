# volidation for mobile number.
import re
regex=re.compile(r"\d(10)")
while True:
    mobno=input("enther mobile no")
    if len(mobno)==10:
        result=regex.search(mobno)
        if result:
            print("valid mobileno")
            break
        else:
            print("mobno should contain digits only")
    else:
        print("mobno should contain 10 digits")
