#Leoxur coffee shop program
print("*"*50)
coffee_shop=input("Enter your name:\n")
print("*"*50)

print("*"*50)
print("Welcome to Leoxur coffee shop :",coffee_shop, "!")
print("1: Coffee")
print("2: Tea")
print("3: Lemon Tea")
print("4: Milk")
print("*"*50)




#While loop for taking the input from the customer drink


while True:
    drink=input("Select the drink to have(Coffee/Tea/LemonTea/Milk):\n")
    print("*" * 50)

#Drink Selecting \ Pricing algorithm

    if drink=="1":
        print("select your cup size")
        print("*" * 50)

        size =input("enter your cup size\n1: 50ml\n2: 60ml\n3: 70ml\n")
        print("*" * 50)
        if size=="1":
            print("The total cost is Rs.10/-")
        elif size =="2":
            print("The total cost is Rs.15/- ")
        elif size =="3":
            print("The total cost is Rs.20/-")
        else:
            print("invalid input")
        break
    elif drink == "2":
        print("Select your cup size")
        size = input("enter your cup size\n1: 50ml\n2: 60ml\n3: 70ml\n")
        if size == "1":
            print("The total cost is Rs.8/-")
        elif size == "2":
            print("The total cost is Rs.12/- ")
        elif size == "3":
            print("The total cost is Rs.18/-")
        else:
            print("invalid input")
        break
    elif drink == "3":
        print('select your cup size')
        size = input("enter your cup size\n1: 50ml\n2: 60ml\n3: 70ml\n")
        if size == "1":
            print("The total cost is Rs.8/-")
        elif size == "2":
            print("The total cost is Rs.12/- ")
        elif size == "3":
            print("The total cost is Rs.18/-")
        else:
            print("invalid input")
        break
    elif drink == "4":
        print("enter your cup size")
        size = input("enter your cup size\n1: 50ml\n2: 60ml\n3: 70ml\n")
        if size == "1":
            print("The total cost is Rs.10/-")
        elif size == "2":
            print("The total cost is Rs.15/- ")
        elif size == "3":
            print("The total cost is Rs.20/-")
        else:
            print("invalid input")
        break
    else:
        print("Invalid input")



#Payment form the customer

print("*"*50)
print("Please select the payment method")
print("1:PIN")
print("2:Reg No:")
print("3:Customer ID")
print("*"*50)

payment=int(input("please select :\n"))
print("*"*50)
if payment==1:
    print("enter the pin")
    print("*" * 50)
    PIN=int(input("please provide your 4 digit pin :\n"))
    print("payment sucessfull")
    print("please keep the correct size cup on the filling area")
    print("*" * 50)
    fill = input("Fill or Cancle :\n")
    if fill == "fill":
        i = 0
        while i <100:
            i = i + 1
            print("[][][][][][][][][][][][][][][][][][]", i, "%")
    else:
        print("the money is refunded to your wallet")
elif payment==2:
    print("enter the register number")
    PIN=int(input("please provide your 12 digit pin :\n"))
    print("payment sucessfull")
    print("please keep the correct size cup on the filling area")
    fill = input("Fill or Cancle :\n")
    if fill == "fill":
        i = 0
        while i <100:
            i = i + 1
            print("[][][][][][][][][][][][][][][][][][]", i, "%")
    else:
        print("the money is refunded to your wallet")
elif payment==3:
    print("enter the Customer ID")
    PIN=int(input("please provide your 8 digit pin :\n"))
    print("payment sucessfull")
    print("please keep the correct size cup on the filling area")
    fill=input("Fill or Cancle :\n")
    if fill=="fill":
        i=0
        while i<100:
            i=i+1
            print("[][][][][][][][][][][][][][][][][][]",i,"%")
    else:
        print("the money is refunded to your wallet\n")



else:
    print("plese select another responce")


#feedback from the customer


print("*"*50)
print("Thank You", coffee_shop, "for Grab a Coffee on LEOXUR")

print('''
for the further feedback please contact On
Email: leoxurcafe@leoxur.com''')
print("*"*50)












