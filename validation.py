def account_number_validation(accountNumber):

    if accountNumber:

        if len(str(accountNumber)) == 10:

            try:
                int(accountNumber)
                return True
            except ValueError:
                print('Invalid account number, account number should be an integer')
                return False
            except TypeError:
                print('Invalid account number, account number should be an integer')
                return False

        else:
            print('Cannot be more or less than 10 digits')
            return False

    else:
        print('Account number is a required field')
        return False