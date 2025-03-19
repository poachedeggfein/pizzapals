print("""==================================
welcome to the pizza pals!
==================================\n""")

#prompting user to type in customer name
nameflag = False

while nameflag == False:

    
    name = input("please enter the customer name: ")
    answer = input("\nyou have entered the customer name " +name+  ", is this correct? ")
    if answer.upper() == "YES":
        print("\nperfect!")
        print("\n===================================\n")
        nameflag = True
    elif answer.upper() == "NO":
        print("\noh no!\n")
    else:
        print("\nplease enter yes or no")

#prompting user to type in customer address
addressflag = False

while addressflag == False:


    address = input("please enter the customer address: ")
    answer = input("\nyou have entered the address " +address+ ", is this correct? ")
    if answer.upper() == "YES":
        print("\namazing!")
        print("\n===================================\n")
        addressflag = True
    elif answer.upper() == "NO":
        print("\nwhoops!\n")
    else:
        print("\nplease enter yes or no") 

#prompting user to type in customer phone number
phoneflag = False

while phoneflag == False:

    
    phonenumber = input("please enter customer phone number: ")
    if len(phonenumber) == 11 and phonenumber.isdigit ():
        answer = input("\nyou have entered the phone number " +phonenumber+ ", is this correct? ")
        if answer.upper() == "YES":
            print("\ngood!")
            print("\n===================================\n")
        phoneflag = True
    elif answer.upper() == "NO":
        print("\ntry again!\n")
    else: 
        print("\nplease re-enter the phone number again that is 11 digits long!\n")    

#prompt user to type in the quantity of pizzas being ordered
while True:
    try:
        quantity = int(input("please enter the number of pizzas: "))
        if quantity >=1 and quantity <=6:
            print("\nperfect!")
            break
        else:
            print("\nplease enter a number between 1 and 6!\n")
    except:
        print("\nlooks like you have tried to enter something that is not a number! please enter a valid number!\n")

#calculating the cosst of the pizza order
total = 0

for i in range(quantity):
    total = total + 5

#outputting personalised bill
print("\n===================================\n")
print("customer name: ", name)
print("customer address: ", address)
print("customer phone number: ", phonenumber)
print("customer pizza quantity: ", str(quantity))
print("the total cost: ", str(total))
print("\n===================================\n")