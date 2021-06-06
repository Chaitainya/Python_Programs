first_name = input("enter the first name: ")
last_name = input("enter the last name: ")

if first_name == "" and last_name == "":
    print("Cannot be empty")
elif first_name != "Leon" and last_name != "123":
    print("invalid details")
elif first_name != "Leon":
    print("first name incorrect")
elif last_name != "123":
    print("last name incorrect")
else:
    print("Login Success")