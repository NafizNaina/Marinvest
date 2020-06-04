from console.input import *
from console.dashboard import *
import pandas as pd
import os


# read csv from a parent directory
input_data = pd.read_csv(os.path.join(os.getcwd(), '..', 'data','input_data.csv'))

# input user id
user_id = input_user_id()

# import current data from user id
id_data = input_data['User ID'].tolist()

# Get fixed data from previous month 
# if none, enter new fixed data
if user_id not in id_data:
    print(f'Welcome to Marinvest, User {user_id}! \n')
    print('Marinvest is a financial planning app that will make your financial life easy!')
    print("All that you have to do is to update your monthly income and and account balances, then we'll take care of the rest! \n")
    print('To get started, we need to know more about you... \n')
    print('First, we need to have a rough idea on how much you make and spend.')
    print('Rough estimates are fine. However more precise information will allow us give more accurate insights \n')
    print('Initial setup')

    fixed_income, fixed_expense, variable_expense, fixed_saving, is_life_insurance, is_medical_insurance = initial_input(user_id)

    # goals (will calculate PMT based on some interest rate)
    ## 1. retirement
    ## 2. others
else:
     # filter data based on id
    id_input_data = input_data[input_data['User ID'] == user_id]
    print(id_input_data)
    # if there's more than 1, choose the latest month/year
    if len(id_input_data) > 1:
        id_input_data = id_input_data[(id_input_data['Month'] == id_input_data['Month'].max()) & (id_input_data['Year'] == id_input_data['Year'].max())]
    
    # get fixed values
    fixed_income = int(id_input_data['Fixed Income'])
    fixed_expense = int(id_input_data['Fixed Expense'])
    variable_expense = int(id_input_data['Variable Expense'])
    fixed_saving = int(id_input_data['Fixed Savings'])
    is_life_insurance = int(id_input_data['is_life_insurance'])
    is_medical_insurance = int(id_input_data['is_medical_insurance'])

    # print message
    print('In our database, your:')
    print('')
    print(f'Fixed income is {fixed_income}')
    print(f'Fixed expenses is {fixed_expense}' )
    print(f'Fixed saving is {fixed_saving}')
    print(f'Estimated variable expenses is {variable_expense}')
    print(f'is_life_insurance is {is_life_insurance}')
    print(f'is_medical_insurance is {is_medical_insurance}')
    print('')
    update = input("Do you wish to update anything? \nAnswer: ",)
    print('')

    if update == 'yes':
        fixed_income, fixed_expense, variable_expense, fixed_saving, is_life_insurance, is_medical_insurance = fixed_input(user_id)
    
# variable values
month, year, variable_income, variable_saving, account_balance = variable_input()

# save new input
new_input = [user_id,month,year,fixed_income,variable_income,fixed_expense,variable_expense,fixed_saving,variable_saving,account_balance,is_life_insurance,is_medical_insurance]
updated_input_data = input_data.append(pd.Series(new_input, index = input_data.columns), ignore_index=True).drop_duplicates(subset=['User ID','Month','Year'], keep="last")
updated_input_data.to_csv(os.path.join(os.getcwd(), '..','data' ,'input_data.csv'), index = False, header=True)

# create list of stuff needed for dashboard
# use updated_input_data
print("THERE WILL BE A DASHBOARD HERE WHICH WILL TELL THE USEFUL INFORMATION")
dashboard(updated_input_data)
# net flow
# total balance (increase of x from last month)
# investment profit
# DSR debt / income
# savings based on goals vs current savings