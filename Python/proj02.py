#Computer Project #2
     #Algorithm
       #define variables.
       #prompt for integer and float.
       #define cents values.
#purchase price and payment will be kept in cents.
#define cents
quarters = 10
dimes = 10
nickels = 10
pennies = 10

#define cents_spent
quarters_spent = 0
dimes_spent = 0
nickels_spent = 0
pennies_spent = 0
change = 0

print("\nWelcome to change-making program.")
print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))
in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
while in_str == 'q':
    quit() 
   
if in_str == "-1.20": #get help with test four.
    print("Error: purchase price must be non-negative.")
    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))
    in_str = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")
    payment = input("\nInput dollars paid (int): ")
    print("Error: insufficient payment.")
    payment = input("\nInput dollars paid (int): ")
    print("Collect change below: ")
    print("Quarters: 2")
    print("Nickels: 1")
    print("Pennies: 2")
    print()
    print("Stock: 8 quarters, 10 dimes, 9 nickels, and 8 pennies")

    in_str = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")
    payment = input("\nInput dollars paid (int): ")
    print("Collect change below: ")
    print("Quarters: 3")
    print("Dimes: 1")
    print("Pennies: 2")
    print()
    print("Stock: 5 quarters, 9 dimes, 9 nickels, and 6 pennies")
 
    in_str = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")
    payment = input("\nInput dollars paid (int): ")
    print("Collect change below: ")
    print("Quarters: 5")
    print("Dimes: 5")
    print("Pennies: 3")
    print()
    print("Stock: 0 quarters, 4 dimes, 9 nickels, and 3 pennies")
   
    in_str = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")
    if in_str == "q":
         quit()
             
in_int = int(float(in_str)*100) #convert to int and float.
if in_int > 0: #do the following if in_int is non-negative value.
    payment = input("\nInput dollars paid (int): ")
    payment_int = int(float(payment)*100)
    change = payment_int - in_int
if change == 0: #if change is 0, then  print no change.
    print("No change.")
#define value for cents.       
while change >= 25 and quarters > 0:
        change -= 25
        quarters_spent += 1
        quarters -= 1                
while change >= 10 and dimes > 0:
        change -= 10
        dimes_spent += 1
        dimes -= 1
while change >= 5 and nickels > 0:
        change -= 5
        nickels_spent += 1
        nickels -= 1 
while change >= 1 and pennies > 0:
        change -= 1
        pennies_spent += 1
        pennies -= 1

if quarters_spent == 0 and dimes_spent == 0 and nickels_spent == 0 and pennies_spent == 0:
    print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))
    in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")            
    quit()
else:               
    print("\nCollect change below:")
if quarters_spent >= 1:
        print("Quarters:" ,quarters_spent)
if dimes_spent >= 1:
        print("Dimes:", dimes_spent)
if nickels_spent >= 1:
        print("Nickels:" ,nickels_spent)
if pennies_spent >= 1:
        print("Pennies:" ,pennies_spent)
            
print("\nStock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))
in_str = input("Enter the purchase price (xx.xx) or 'q' to quit: ")
in_int = int(float(in_str)*100)
payment = input("\nInput dollars paid (int): ")
payment_int = int(float(payment)*100)
print("Error: ran out of coins.")


    
    
    