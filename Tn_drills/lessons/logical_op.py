entered_pin = int(input("Enter bank pin: "))
stored_pin = 4321
pin_correct = entered_pin == stored_pin

if pin_correct == True:
    print("<<< Available Services >>>")
    print()
    print("1. Withdrawal")
    print("2. Send money")
    print()

    balance = 7000000

    choice = int(input("Select an option (1 or 2): "))

    if choice == 1:
        withdrawal = int(input("Enter Amount for withdrawal: "))

        if withdrawal <= balance:
            balance -= withdrawal
            print("withdrawal successful")
            print("Remaining balance: ", balance)

        else:
            print("Insufficient balance")
            print("Balance: ", balance)

    elif choice == 2:
        amount = int(input("Enter amount to send: "))
        account_num = int(input("Enter account number: "))

        if account_num >= 11:
            print("Invalid account number.")
            
        else:
            if amount <= balance:
                balance -= amount
                print(f"{amount} Has successfully been transferred to {account_num}")
                print("Remaining balance: ", balance)

            else:
                print("Insufficient balance.")

    else:
        print("Invalid choice selected.")        

else:
    print("Incorrect PIN. Access denied.")
        
