#Greets Customer and gives instructions to continue to next step
print('Hello, my name is Jarvis your virtual assistant. I will help you order a pizza!')
print('I am going to ask you a few questions. After typing an answer, press enter.')

#requests name from customer and greets by name
userName = input('\nEnter your name: ')
while len(userName) == 0:
    userName = input("Name cannot be blank! Please enter your name: ")
if userName.lower() == 'marcello martinez':
    print(f'\nWelcome back sir, all systems prepared.')
else:
    print(f'\nHello, {userName}. Nice to meet you.')
keepGoing = 'y'
while keepGoing.lower() == 'y':
    #variables for pizza such as size,flavor,crust,amount, and method of delivery
    size = input('\nWhat size do you want? Enter small, medium, or large: ')
    while size.lower() not in ["small", "medium", "large"]:
        size = input("Invalid value! Please enter small, medium, or large: ")
    flavor = input("\nEnter flavor of pizza: ")
    while len(flavor) == 0:
        flavor = input("Flavor cannot be blank! Please enter a flavor: ")
    crusttype = input('\nWhat type of crust do you want: ')
    while len(crusttype) == 0:
        crusttype = input("Crust type cannot be blank! Please enter crust type: ")
    quantity = input('\nHow many of these do you want to order? Enter a numeric value: ')
    while not quantity.isdigit():
        quantity = input("\nValue not recognized. Please enter a numeric value: ")
    quantity = int(quantity)   
    method = input('\nIs this carry out or delivery: ')
    while method.lower() not in ["carry out", "delivery"]:
        method = input("Invalid value! Please enter carry out or delivery: ")

    #if else statement for price-size and method of recieving order.
    if size.lower() == 'small':
        pizzaCost = 8.99
    elif size.lower() == 'medium':
        pizzaCost = 14.99
    elif size.lower() == 'large':
        pizzaCost = 17.99
    salesTax = 1.1
    if method.lower() == 'delivery':
        deliveryFee = 5
    else:
        deliveryFee = 0

    #Calculates total cost of pizza
    total = (pizzaCost * quantity) * salesTax + deliveryFee

    print('-' * 10)
    print(f'Thank you, {userName}, for your order.')
    print(f'Your {quantity} {size} {flavor}, pizza(s) with {crusttype} crust costs ${total:,.2f}.')
    if total >= 50:
        print('\nCongratulations! You have earned a super coupon for $10 Off your next order!')
    else:
        print('\nNote: Orders over $50 will earn a super coupon for $10 Off your next purchase!')
    print('-' * 10)

    print("Order has been received. ETA 1 min!")
    for min in range(1, 0, -1):
        print(min, "minutes remaining")
        for seconds in range(60, 0, -1):
            print(seconds, end = "\r")
            import time
            time.sleep(1)
    print("order is ready!")

    keepGoing = input("Do you want to place another order? Enter y or n: ")
    while keepGoing.lower() not in ["y", "n"]:
        keepGoing = input("Invalid value. Please enter y or n: ")


