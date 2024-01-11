"""task02 for password"""
import re
rules = " At least 1 letter between[a-z] and 1 letter between [A-Z] \n At leats 1 number between [0-9] \n At least 1 characters [#@$] \n Mginimum length 6 characters \n Maximum length 16 characters"
print(rules)
password = input("Enter your password (but you shoold remember this rules) :")
pattern ="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#@$]).{6,16}$"
element = re.fullmatch(pattern,password)

if element:
    print("Yes, your password saved")
else:
    print("No, it is invalid :0 ") 

#Create programm for password 