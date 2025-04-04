pin = "2025"
balance = 0  
recharge_pin = input("Enter your recharge PIN to load money: ")

if recharge_pin == "*151#"or "*153#":  
    amount_recharged = 100  
    balance += amount_recharged
    
else:
    print("Invalid recharge PIN. Please try again.")
    exit()

print("\nEcoCash Menu:\n1. Check Balance\n2. Send Money")
option = input("Select an option (1 or 2): ")

if option == "1": 
    print(f"Your current balance is: ${balance}")

elif option == "2":  
    recipient = input("Enter recipient phone number: ")
    amount = float(input("Enter amount to send: "))
    
    if amount <= 0:
        print("Invalid amount. Please enter a valid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        entered_pin = input("Enter your PIN to confirm transaction: ")
        
        if entered_pin == pin:
            balance -= amount
            print(f"Transaction successful! You sent ${amount} to  TYTEM THABANI.")
            print(f"New balance: ${balance}")
        else:
            print("Incorrect PIN. Transaction failed.")
else:
    print("Invalid option. Please try again.")

print("Thank you for using EcoCash!")