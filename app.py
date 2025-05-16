'''Create a class named ATM with the following attributes: 
 Balance: Initial value of 5000 rupees 
 Pin: Default value of 1234'''

class ATM:
    def __init__(self):
        self.balance = 5000
        self.pin = 1234

     # 1. check_pin(input_pin): Verify if the entered PIN matches the stored PIN        
    def check_pin(self,input_pin):
     return input_pin == self.pin

    # 2. check_balance(): Display the current account balance 
    def check_balance(self,input_pin):
     if self.check_pin(input_pin):
        print(f'Your balance is {self.balance} rupees')
     else:
        print("Invalid Pin")

    #3. deposit(amount): Add money to the account (requires valid PIN) 
    def deposit(self,input_pin,amount):
     if  not self.check_pin(input_pin):
        print('Invalid pin! deposit failed.')
        return
     if amount <= 0:
        print('deposit amount must be positive!.')
        return
     self.balance += amount
     print(f'{amount} Successfully deposit.')
     print(f'New balance: {self.balance}')
            
    #4. withdraw(amount): Remove money from the account (requires valid PIN and sufficient balance) 
    def withdraw(self,input_pin,amount):
     if not self.check_pin(input_pin):
        print("Invalid pin! Withdraw failed.")
        return
     if amount <= 0:
        print("Withdraw amount must be positive!")
        return
     if amount > self.balance:
        print("Insufficient balance")
        return
     self.balance -= amount
     print(f'{amount} withdraw successfully!')
     print(f'Remaining  balance: {self.balance}')
    
    #5. exit(): Terminate the program  
    def exit(self):
     print("Thank you for using ATM.") 


def main():
    atm = ATM()

# wlcome page
    while True:
        print("------------- Welcome to ATM -----------------")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

# choice option
        choice = input("Enter your choice (1-4)")

# check balance
        if choice == '1':
            try:
                pin = int(input("Enter your pin: "))
                atm.check_balance(pin)
            except ValueError:
                print("Invalid input! Pin must be in numbers")

# deposit
        elif choice == '2': 
            try:
                pin = int(input("Enter your pin: "))
                amount = float(input("Enter amount to deposit: "))
                atm.deposit(pin, amount)
            except ValueError:
                print("Invalid input! Please enter numeric values.")

        elif choice == '3':
            try:
                pin = int(input("Enter your PIN: "))
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw(pin, amount)
            except ValueError:
                print("Invalid input! Please enter numeric values.")

        elif choice == '4':
            atm.exit()
            break
        else:
            print("Invalid choice! Please select between 1 and 4.")


if __name__ == "__main__":
    main()