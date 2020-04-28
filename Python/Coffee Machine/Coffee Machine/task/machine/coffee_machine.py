# Write your code here

water = int(input("Write how many ml of water the coffee machine has: ")) // 200
milk = int(input("Write how many ml of milk the coffee machine has: ")) // 50
coffee_beans = int(input("Write how many grams of coffee beans the coffee machine has: ")) // 15
cups = int(input("Write how many cups of coffee you will need: "))
min_cups = min(water, milk, coffee_beans)

if min_cups == cups:
    print("Yes, I can make that amount of coffee")
elif min_cups < cups:
    print("No, I can make only " + str(min_cups) + " cups of coffee")
elif min_cups > cups:
    print("Yes, I can make that amount of coffee (and even " + str(min_cups - cups) + " more than that)")
