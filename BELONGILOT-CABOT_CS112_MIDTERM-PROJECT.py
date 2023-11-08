balance = 0
print("|--Welcome to C&M Banking--|")
print("|--------------------------|")

while True:
    pass_ask = int(input('|Set PIN: '))
    pass_ask2 = int(input('|Confirm PIN: '))
    
    if pass_ask2 != pass_ask:
        print("|PIN does not match! please try again")

    elif pass_ask2 == pass_ask:
        print("|Registration successful! You may start your transaction")
        
        while True:
            correct_pass = int(input('|Enter PIN: '))
            
            if correct_pass == pass_ask:

                while True:
                    print("-----------------------------------------------------------------")
                    print("|Would you like to: \n|(D)eposit \n|(W)ithdraw \n|(B)alance Check")
                    print("|Current Balance: ₱", balance)
                    choice = input("|Enter desired transaction here ('D'/'W'/'B'): ")
                    
                # Balance inquiry

                    if choice.lower() == 'b' or choice.upper() == 'B':
                        print('|Your balance is currently: ₱', int(balance))

                # Deposit money

                    elif choice.lower() == 'd' or choice.upper() == 'D':
                        deposit = eval(input('|Please Enter Amount: '))
                        current = balance + deposit
                        print('|Your balance is now: ₱', current)
                        balance = current
                    
                # Withdraw balance

                    elif choice.lower() == 'w' or choice.upper() == 'W':
                        withdraw = eval(input('|Please Enter amount: '))
                        if balance < withdraw:
                            print('|You have insufficient balance!')
                        elif balance >= withdraw:
                            current = balance - withdraw
                            print("|You have withdrawn ₱",withdraw, ", your current balance is ₱", current)
                            balance = current
                                                   
                    else:
                        print("|Invalid Operation!")
                    
                    # Another transaction
                    
                    another = input('|Do you want to make another transaction (yes/no)? ')
                    if another.lower() != 'yes':
                        print('|Thank you for using C&M Banking! \n')
                        break
            else:
                print("|Invalid Password! Try again.")