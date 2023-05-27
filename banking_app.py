import datetime
class Bank:
    '''
    Adding global variables which will be used across multiple functions.
    Global variable description:
    database: It is a dictionary that holds record of all users.
    account_number: It is the default pattern of the account numbers for all the users.
    '''
    database = {};
    account_number = 0;
    def __init__(self):
        self.account_number = 4645519960462000;
        
    def menu(self):
        '''
        menu() prints all the options available for the users to choose from.
        This function returns the option entered by user.
        '''
        print('\nPlease select any option from the below menu:');
        print("""
        1. Create account
        2. Deposit money
        3. Withdraw money
        4. Transfer money
        5. Balance Enquiry
        6. Quit""");
        choice = input();
        return choice;
    
    def create_account(self):
        '''
        This function is used to add details of new user or existing users' new account details in database.
        User will be required to enter following details to open new account:
        1. Full name.
        2. Date of birth in DDMMYY format.
        3. Residential addrress.
        4. Password/Pin for their bank account.
        Account number will be allocated automatically to each new bank account.
        By default balance for each user will be 0.
        '''
        new_user = []; #It is a list that will hold data of new user.
        balance = 0.0; #As it is a new account, account balance will be 0 for each new user.
        name_format = True; #It is a flag to check if there are numeric or special characters in name.
        name = input('Enter your full name ');
        #Checking if there are any numeric or special characters in the name entered by user
        for i in name:
            if((i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z') or (i == ' ')):
               continue;
            else:
               print('No numeric digit or special characters allowed.');
               name_format = False;
               break;
        #Asking the user if they wants to continue with account creation or return to main menu.
        if (name_format == False):
               print('Press Y to re-enter your name or press any other key to exit?');
               proceed = input();
               if(proceed == 'Y' or proceed == 'y'):
                   self.create_account();
                   return;
               else:
                   print("Returning to main menu!");
                   return;
               
        new_user.append(name);
        dob = input('Enter your date of birth in the format DDMMYYYY ');
        
        #Checking if there are any alphabetic or special characters in the date of birth entered by the user.
        for i in dob:
            if(i >= '0' and i <= '9'):
               continue;
            else:
               print('No alphabet or special characters allowed. \nReturning to main menu');
               return;
            
        if(len(dob) != 8):
            print('Please enter the date in correct format: DDMMYYYY \nReturning to Main menu');
            return;
        
        '''
        Checking if the date of birth entered is correct or not.
        For example: 32012008 is incorrect because there are only 31 days in Jan not 32.
        '''
        date = int(dob[:2]);
        month = int(dob[2:4]);
        year = int(dob[4:]);
        leap = False;
        
        #checking if the year is leap or not, so that we can check if there were 28 days or 29 days in the month of February
        if (year % 400 == 0) & (year % 100 == 0):
            leap = True;
        elif (year % 4 ==0) and (year % 100 != 0):
            leap = True;
        else:
            leap = False;
        
        #Checking if the date and month is entered correctly
        if ((month == 2) & (leap == True)):
            if ((date < 1) | (date > 29)):
                print('Invalid date entered \nReturning to main menu');
                return;
        elif ((month == 2) & (leap == False)):
            if ((date < 1) | (date > 28)):
                print('Invalid date entered \nReturning to main menu');
                return;
        elif ((month > 0) & (month < 8) & (month % 2 == 1)):
            if ((date < 1) | (date > 31)):
                print('Invalid date entered \nReturning to main menu');
                return;
        elif ((month > 7) & (month < 13) & (month % 2 == 0)):
            if ((date < 1) | (date > 31)):
                print('Invalid date entered \nReturning to main menu');
                return;
        elif ((month > 2) & (month < 8) & (month % 2 == 0)):
            if ((date < 1) | (date > 30)):
                print('Invalid date entered \nReturning to main menu');
                return;
        elif ((month > 7) & (month < 13) & (month % 2 == 1)):
            if ((date < 1) | (date > 30)):
                print('Invalid date entered \nReturning to main menu');
                return;
        else:
            print('Incorrect Month number entered, enter bewteen 01 and 12, where 01 stands for Jan and 12 stands for Dec');
            print('Returning to main menu');
            return;

        #Checking if the year in date of birth entered is correct or not.
        dob_entered = datetime.date(year, month, date);
        current_date = datetime.date.today(); #using this function, getting current date.
        
        if(year < 1898):
            print('Incorrect year entered! Till date the longest that any human have lived is for 122 years.');
            print('Returning to main menu');
            return;
        
        elif (dob_entered > current_date):
            print('Time machine is not invented yet! Sorry you can\'t go in future and create bank account.' );
            print('Returning to main menu.')
            return;
        
        new_user.append(dob);
        
        #Asking user to enter their resedential address.
        address = input('Enter your address ');
        new_user.append(address);
        
        #As a new bank account is getting created, hence default balance will be 0.
        new_user.append(balance);
        
        #Asking user to enter password to make their account secure.
        password = input('Enter a pin/password for your bank account ');
        new_user.append(password);
        
        '''
        account_number is a variable that holds a default pattern for account number.
        Each time a new account is created, we just add 1 to the default pattern.
        '''
        self.account_number += 1;
        
        #database is a dictionary that holds data of all users. account_number is made key here, since it is identical for each user.
        self.database[self.account_number] = new_user;
        
        print('\nFollowing are your bank account details: ');
        print('Account Number: {} \nName: {} \nDOB: {}-{}-{}'. format(self.account_number, new_user[0], date, month, year));
        print('Address: {} \nBalance: {} \nPassword: {}'. format(new_user[2], new_user[3], new_user[4]))
        return;
    
    def deposit_sum(self):
        '''
        deposit_sum() is used when user wants to deposit money in an account.
        For depositing, user must specify the account number and the sum.
        '''
        acc_num = input('Enter your account number ');
        #Checking if there are no alphabetic or special characters in the account number entered by user.
        try:
            acc_num = int(acc_num);
        except ValueError:
            print('Invalid account number! Would you like to continue or not?\n Press Y to re-enter account number or Press any button for main menu');
            proceed = input();
            if(proceed == 'Y' or proceed == 'y'):
                self.deposit_sum();
                return;
            else:
                return;
            
        #Checking if the account number entered exist in our database.
        user_info = self.database.get(acc_num);
        password_index = 4; # As password is stored at 4th index of user_info list.
        if(user_info == None):
            print('Account not found!');
        else:
            password = input('Enter your password: ');
            if (password == user_info[password_index]): 
                amount = input('Enter the amount ');
                #Checking if there are no alphabetic or special characters in the amount entered by the user.
                try:
                    amount = float(amount);
                except ValueError:
                    print('Invalid input! Returning to main menu');
                    return;
                balance_index = 3; #balance is at 4th position in list which store user info.
                if (amount <= 0):
                    print('''Please enter correct amount
                    Your account balance is: ''', user_info[balance_index]);
                else:
                    user_info[balance_index] += amount;
                    print('{} deposited to your account.\nYour account balance is {}'.format(amount,user_info[balance_index]));
            else:
                print('Invalid password entered. Returning to main menu.');
                
        return;
    
    def withdraw_sum(self):
        '''
        withdraw_sum() is used when user wants to withdraw money from an account.
        For depositing, user must specify the account number and the sum.
        '''
        acc_num = input('Enter your account number ');
        try:
            acc_num = int(acc_num);
        except ValueError:
            print('Invalid account number! Would you like to continue or not?\n Press Y to re-enter account number or Press any button for main menu');
            proceed = input();
            if(proceed == 'Y' or proceed == 'y'):
                self.withdraw_sum();
                return;
            else:
                return;
        user_info = self.database.get(acc_num);
        password_index = 4; # As password is stored at 4th index of user_info list.
        if(user_info == None):
            print('Account not found!');
        else:
            password = input('Enter your password: ');
            if (password == user_info[password_index]):
                amount = input('Enter the amount ');
                try:
                    amount = float(amount);
                except ValueError:
                    print('Invalid input! Returning to main menu');
                    return;
                balance_index = 3; #balance is at 4th position in list which store user info.
                if (amount > user_info[balance_index]):
                    print('Insufficient Balance! \nYour account balance is: ', user_info[balance_index]);
                elif (amount <= 0):
                    print('''Please enter correct amount
                    Your account balance is: ''', user_info[balance_index]);
                else:
                    user_info[balance_index] -= amount;
                    print('Please collect the sum: {} \nYour account balance is {}'.format(amount,user_info[balance_index]));
            else:
                print('Invalid password entered. Returning to main menu');
        return;
    
    def transfer_sum(self):
        '''
        transfer_sum() is used when user wants to transfer money from their account to another.
        For depositing, user must specify the account number and the sum.
        '''
        sender_acc_num = input('Enter your account number ');
        try:
            sender_acc_num = int(sender_acc_num);
        except ValueError:
            print('Invalid account number! Returning to main menu.');
            return;
        user_info_sender = self.database.get(sender_acc_num);
        password_index = 4; # As password is stored at 4th index of user_info_sender list.
        if(user_info_sender == None):
            print('Account not found! Returning to main menu');
            return;
        else:
            password = input('Enter your password: ');
            if (password != user_info_sender[password_index]):
                print('Invalid password entered. Returning to main menu');
                return;
        receiver_acc_num = input('Enter account number of recipient ');
        try:
            receiver_acc_num = int(receiver_acc_num);
        except ValueError:
            print('Invalid account number! Returning to main menu.');
            return;
        user_info_receiver = self.database.get(receiver_acc_num);
        amount = input('Enter the amount ');
        try:
            amount = float(amount);
        except ValueError:
            print('Invalid input! Returning to main menu');
            return;
        balance_index = 3; #balance is at 4th position in list which store user info.
        if (amount > user_info_sender[balance_index]):
            print('Insufficient Balance! \nYour account balance is: ', user_info_sender[balance_index]);
        elif (amount <= 0):
            print('''Please enter correct amount
            Your account balance is: ''', user_info_sender[balance_index]);
        else:
            user_info_sender[balance_index] -= amount;
            print('{} has been transferred to recipient. \nYour account balance is {}'.format(amount,user_info_sender[balance_index]));
            
            #if recepient's account number is not found in the database, it indicates recepient's account is in other Bank.
            #But if it is found in our database, then we need to add the amount in the recepient's account.
            if (user_info_receiver != None):
                user_info_receiver[balance_index] += amount;
            else:
                print('As recepient\'s Account is in other bank, amount will be deposited in next 1 hour.')
        return;
    
    def balance_enquiry(self):
        '''
        balance_enquiry() is used to do balance enquiry of the account entered by the user.
        For this, user need to enter the account numnber.
        '''
        acc_num = input('Enter your account number ');
        try:
            acc_num = int(acc_num);
        except ValueError:
            print('Invalid account number! Would you like to continue or not?\n Press Y to re-enter account number or Press any button for main menu');
            proceed = input();
            if(proceed == 'Y' or proceed == 'y'):
                self.balance_enquiry();
                return;
            else:
                return;
        user_info = self.database.get(acc_num);
        if(user_info == None):
            print('Account not found! Returning to main menu.');
        else:
            balance_index = 3;
            password_index = 4;
            password = input('Enter your password: ');
            if (password == user_info[password_index]):
                print('Your account balance is ', user_info[balance_index]);
        return;
      
def Main():
    bank_account = Bank();
    choice = bank_account.menu();
    print('You have entered: ', choice);
    while(choice != 6):
        try:
            choice = int(choice);
        except ValueError:
            print('Invalid input!');
            choice = bank_account.menu();
            continue;
        if(choice == 1):
            bank_account.create_account();
            choice = bank_account.menu();
        elif(choice == 2):
            bank_account.deposit_sum();
            choice = bank_account.menu();
        elif(choice == 3):
            bank_account.withdraw_sum();
            choice = bank_account.menu();
        elif(choice == 4):
            bank_account.transfer_sum();
            choice = bank_account.menu();
        elif(choice == 5):
            bank_account.balance_enquiry();
            choice = bank_account.menu();
        elif(choice == 6):
            print("Thank you for banking with us!");
            #exit(0);
        else:
            print('Invalid Input! Please select the right option!');
            choice = bank_account.menu();
            
if(__name__ == '__main__'):
    Main()
