import sys

from classes import Product

CheapProduct = Product("Tofu Bar", 1.19)
AverageProduct = Product("Wooden Box", 59.99)
ExpensiveProduct = Product("Phone", 999.99)
Products = [CheapProduct,AverageProduct,ExpensiveProduct]

def ChooseProduct():
    print("The Products available are:")
    txtProduct = "{}.  {} for {}€"
    number = 1
    for product in Products:
        print(txtProduct.format(number,product.name, product.price))
        number += 1
    chosenProduct = int(input("Input number of wanted product:"))-1
    txtProduct = "You chose: {}"
    if chosenProduct >= len(Products) or chosenProduct < 0:
        print("Not Available")
        sys.exit()
    else:
        print(txtProduct.format(Products[chosenProduct]))
    return chosenProduct




def SellingMachine():
    price = Products[chosenProduct].price
    print(price)
    payment = float(input("How many Euros are you putting in the machine?"))
   # print (payment)
    change = payment - price
  #  print (change)
    paymentTypes = [500,200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.009]
    print("You get:")
    for pay in paymentTypes:
        changetemp = 0
        if change > pay:
            changetemp = int(change / pay)
            change -= changetemp * pay
        if changetemp >= 1:
            if pay >= 5:
                print(changetemp,pay,"€-banknotes")
            elif pay == 0.009:
                print(changetemp,"0,01 €-coins")
            else:
                print(changetemp,pay,"€-coins")


chosenProduct =ChooseProduct()
SellingMachine()