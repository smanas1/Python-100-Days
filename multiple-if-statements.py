print("Ticket Price For Age")

# Ask user for their age

userAge = int(input("Enter your age \n"))

if userAge < 18 :
   
    if userAge < 10 :
        print("Ticket Price: $5")

    elif userAge <= 17:
        print("Ticket Price: $7")
else :
    print("Ticket Price: $15")
