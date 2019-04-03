'''
Daniel Ludwig - A02220549
'''

import os
'''
importing the operating system
'''

file_directory = os.path.dirname(os.path.realpath(
    __file__))  # Found on SO: https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
csv_file_name = '{}/atomcust.csv'.format(file_directory)
#pulls the atomcust.csv fine and appends it

def is_not_null_string(user_string):
    return user_string is None or len(user_string) == 0
'''
Sets the function is_not_null_string to check and make sure the space wasn't left blank
'''

def is_str_positive_integer(int_as_str):
    try:
        new_int = int(int_as_str)
        return new_int >= 0
    except:
        pass
    return False
'''
Sets the function is_str_positive_integer to make sure the integer is a positive number
'''

count = 0
#count counts how many times something was inputted

class Customer(object):
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.phone = ''
        self.email = ''
        self.marital_status = ''
        self.date_of_birth = ''
        self.children = '-1'
        self.political_affiliation = ''
        self.household_income = ''
        self.fishing_license_recent = 'ƒ'
        #Assigns self to identify that its apart of the customer

    def __str__(self):
            return 'Customer named: {} {} >'.format(self.first_name, self.last_name)
            #sets the customers name as a combination of the first name and last name

    def to_csv_format(self):
            csv_format = '{}, {}, {}, {}, {}, {}, {}, {}, {}, {} \n ',' \n'.format(
                self.first_name,
                self.last_name,
                self.phone,
                self.email,
                self.marital_status,
                self.date_of_birth,
                self.children,
                self.political_affiliation,
                self.household_income,
                self.fishing_license_recent
            )
            return csv_format
            #converts the inputted information into .csv format

    def enter_customer_info(self):
        while is_not_null_string(self.first_name):
            self.first_name = input('Please enter the first name: ')
        while is_not_null_string(self.last_name):
            self.last_name = input('Please enter the last name ')
        while is_not_null_string(self.phone):
            self.phone = input('Please enter the phone number: ')
        while is_not_null_string(self.email):
            self.email = input('Please enter the email address: ')
        while is_not_null_string(self.marital_status):
            self.marital_status = input('Please enter the marital status: ')
        while is_not_null_string(self.date_of_birth):
            self.date_of_birth = input('Please enter the date of birth: ')

        while not is_str_positive_integer(self.children):
            self.children = input('Please enter the number of children: ')
        while not is_str_positive_integer(self.household_income):
            self.household_income = input('Please enter the annual household income: ')

        while self.political_affiliation.lower() not in ['r', 'd', 'o', 'None']:
            self.political_affiliation = input('Please enter the political affiliation: ')
        while self.fishing_license_recent.lower() not in ['y', 'n']:
            self.fishing_license_recent = input('Please enter if held a valid fishing license in the last 4 years: ')
        return self
        #Inputs all needed information and give some restrictions on what can be entered

if __name__ == '__main__':
    data_file = open(csv_file_name, 'a+')
    add_customer = True

    while add_customer:
        customer = Customer()
        customer.enter_customer_info()
        data_file.writelines(customer.to_csv_format())
        add_customer = input('Would you like to add another customer (y, n): ')
        add_customer =  add_customer.lower() in ['yes', 'y']
        count += 1
        #Adds the customer's info to the database and asks if they would like to add another customer
        #also adds one to count

    data_file.close()
'''
Closes the program
'''

print(count, 'records were entered.') # prints how many records were recorded
print(customer) #prints the name of the customer
print('Thanks for inputting the information. Now go have a pretty good day!') #thanks the person for inputting the information