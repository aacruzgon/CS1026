#Developed by: Alan Cruz
#Date: Jan 26th
#Desc: A program that inquiries dietary needs among a party and subsequently lists the meals for dinner

# list of foods based on dietary needs
pizza = ["y", "y", "n"]
falafel = ["y", "y", "y"]
pasta = ["n", "y", "n"]
steak = ["y", "n", "y"]

# Dictionary for the food prices
mealPrice = {
    "pizza": 44.50,
    "pasta": 48.99,
    "falafel": 52.99,
    "steak": 49.60,
    "beverage": 5.99
}

#variables that track the amount of food items order by the invitees
numbOfPizzas = 0
numbOfPastas = 0
numbOfFalafels = 0
numbOfStakes = 0
numbOfBeverages = 0


numberOfInvitees = int(input("Please enter the number of invitees:"))
print()
#Prevents division by 0 error
if numberOfInvitees > 0:
# Global variable initialization
    finalOrder = []
    i = 1

# Algorithm that takes dietary needs and converts them into available food by the restaurant 
    while i <= numberOfInvitees:
        print(
            f'Please enter the order details for invitee Number {i}/{numberOfInvitees}')
    # Local variable that stores the dietary needs of the invitees
        orderDetails = []
        keto = input('Do you want a keto friendly meal?')
        if keto == "y":
            orderDetails.append(keto)
        else:
            keto = "n"
            orderDetails.append(keto)
        vegan = input("Do you want a vengan meal?")
        if vegan == "y":
            orderDetails.append(vegan)
        else:
            vegan = "n"
            orderDetails.append(vegan)
        glutenFree = input("Do you want a Gluten-free meal?")
        if glutenFree == "y":
            orderDetails.append(glutenFree)
        else:
            glutenFree = "n"
            orderDetails.append(glutenFree)
    # Converting the dietary needs "orderDetails" into the meals offered and storing the meal into the "finalOrder" variable
        if orderDetails == falafel:
            finalOrder.append("falafel")
            numbOfFalafels += 1
        elif orderDetails == pasta:
            finalOrder.append("pasta")
            numbOfPastas += 1
        elif orderDetails == pizza:
            finalOrder.append("pizza")
            numbOfPizzas += 1
        elif orderDetails == steak:
            finalOrder.append("steak")
            numbOfStakes += 1
        else:
            finalOrder.append("beverage")
            numbOfBeverages += 1
        i += 1
        print("-"*20)

# Algorithm that calculates the recipe cost
    servertip = int(input("How much do you want to tip your server (% percent)?"))
    print()
# variable initialization
    totalCost = 0
    for meal in finalOrder:
        if meal in mealPrice:
            totalCost = totalCost + mealPrice[meal]
            totalCostTax = totalCost * 1.13
            finalTotalCost = totalCostTax * ((100+servertip)/100)
        

# Recipe Statement
    print(f'You have {numberOfInvitees} invitees with the following orders:')
    print(f'{numbOfPizzas} invitees ordered Pizza. The cost is: ${44.50*numbOfPizzas:.2f}')
    print(f'{numbOfPastas} invitees ordered Pasta. The cost is: ${48.50*numbOfPastas:.2f}')
    print(f'{numbOfFalafels} invitees ordered Falafel. The cost is: ${52.99*numbOfFalafels:.2f}')
    print(f'{numbOfStakes} invitees ordered Steak. The cost is: ${49.60*numbOfStakes:.2f}')
    print(f'{numbOfBeverages} invitees ordered only beverage. The cost is: ${5.99*numbOfBeverages:.2f}')
    print()
    print(f'The total cost before tax is ${totalCost:.2f}')
    print(f'The total cost after tax is ${totalCostTax:.2f}')
    print(f'The total cost after {servertip}% tip is ${finalTotalCost:.0f}')