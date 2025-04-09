def CalculateSales():

    total = 0
    pay = int(input("What was the price paid? "))
    while(pay != -1):
        total += pay
        pay = int(input("What was the price paid? "))
    print("Your pay is $", ((total * .2) + 200))

CalculateSales()
