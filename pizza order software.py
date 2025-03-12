print("""==================================
welcome to the pizza pals!
==================================\n""")

#prompting user to type in customer name
nameflag = False

while nameflag == False:


    name = input("please enter the customer name: ")
    answer = input("\nyou have entered the customer name " +name+  ", is this correct? ")
    if answer.upper() == "YES":
        print("\nperfect! \n")
        nameflag = True
    elif answer.upper() == "NO":
        print("\noh no! \n")
    else:
        print("\nplease enter yes or no")

#prompting user to type in customer address
addressflag = False

while addressflag == False:


    address = input("please enter the customer address: ")
    answer = input("\nyou have entered the address " +address+ ", is this correct? ")
    if answer.upper() == "YES":
        print("\namazing!")
        addressflag = True
    elif answer.upper() == "NO":
        print("\nwhoops! \n")
    else:
        print("\nplease enter yes or no") 

#prompting user to type in customer phone number
phoneflag = False

while phoneflag == False:

    phonenumber = input("\nplease enter customer phone number: ")
    if len(phonenumber) == 11 and phonenumber.isdigit ():
        answer = input("\nyou have entered the phone number " +phonenumber+ ", is this correct? ")
        if answer.upper() == "YES":
            print("\ngood!")
        phoneflag = True
    else:
        print("\nplease re-enter the phone number again that is 11 digits long!")    

#outputting personalised bill
print("\n===================================\n")
print("customer name: ", name)
print("customer address: ", address)
print("customer phone number", phonenumber)
print("\n===================================\n")