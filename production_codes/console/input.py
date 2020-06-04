def input_user_id():
    #Enter user_id
    print('User ID')
    print('-'*25)
    user_id = int(input('Enter your User ID: ',))
    print('-'*25)
    print('')

    return(user_id)

def fixed_input(user_id):
    print('Fixed values')
    print('')
    print('-'*50)
    fixed_income = float(input('Enter your monthly fixed income:',)) 
    print('-'*50)
    fixed_expense = get_total_fixed_expense(user_id)
    variable_expense = get_total_variable_expense(user_id)
    print('')
    fixed_saving = float(input('Enter your monthly fixed savings:',))
    print('')
    is_life_insurance = float(input('Do you have life insurance:',))
    is_medical_insurance = float(input('Do you have medical insurance:',))
    print('-'*50)

    return fixed_income, fixed_expense, variable_expense, fixed_saving, is_life_insurance, is_medical_insurance

def variable_input():
    print('Variable values')
    print('-'*50)
    month, year = int(input('Month:',)), int(input('Year:',))
    print('')
    variable_income = float(input("Enter this month's variable income:",))
    variable_saving = float(input("Enter this month's additional savings:",))
    account_balance = float(input("Enter this month's total account balance:",))
    print('-'*50)
    return month, year, variable_income, variable_saving, account_balance

def get_total_fixed_expense(user_id):
    # TODO save total fixed expense in a sheet
    print('')
    print('Fixed Expenses')
    print('-'*50)

    expense_type = ''
    i = 1
    expense_amt_list = []
    expense_type_list = []
    while expense_type != 'exit':
        #input
        expense_type = input(f'Fixed Expense {i}: ',)
        expense_amt = float(input('Amount: ',))
        ask_more = input('Add more fixed expenses? Answer: ', )
        #append to list
        expense_type_list.append(expense_type)
        expense_amt_list.append(expense_amt)
        #when to break
        if ask_more != 'yes':
            break
        i += 1
    print('-'*50)

    # save to csv
    ## read current csv
    ## delete previous entries of the id
    ## create
    ## append new entry of the id
    ### do the same for below
    
    return(sum(expense_amt_list))

def get_total_variable_expense(user_id):
    # TODO save total_variable expense somewhere
    print('')
    print('Estimated Variable Expenses')
    print('-'*50)

    expense_type = ''
    i = 1
    expense_amt_list = []
    expense_type_list = []
    while expense_type != 'exit':
        #input
        expense_type = input(f'Variable Expense {i}: ',)
        expense_amt = float(input('Estimated Amount: ',))
        ask_more = input('Add more fixed expenses? Answer: ', )
        #append to list
        expense_amt_list.append(expense_amt)
        expense_type_list.append(expense_type)
        #when to break
        if ask_more != 'yes':
            break
        i += 1
    print('-'*50)
    return(sum(expense_amt_list))

def debt(user_id):
    # TODO add debt and save in a csv
    """ add debt"""
    # TODO save total_variable expense somewhere
    print('')
    print('Debt')
    print('-'*50)

    debt_type = ''
    i = 1
    debt_amt_list = []
    debt_type_list = []
    debt_pmt_list = []
    debt_enddate_list = []
    while debt_type != 'exit':
        #input
        debt_type = input(f'Debt {i}: ',)
        debt_amt = float(input('Total Debt Amount: ',))
        debt_pmt = float(input('Debt payment per month: ',))
        debt_enddate = float(input('Final payment date (dd/mm/yyyy): ',))

        ask_more = input('Do you have any more debt? Answer: ', )
        #append to list
        debt_amt_list.append(debt_amt)
        debt_type_list.append(debt_type)
        debt_pmt_list.append(debt_pmt)
        debt_enddate_list.append(debt_enddate)
        #when to break
        if ask_more != 'yes':
            break
        i += 1
    print('-'*50)
    #print(expense_type_list,expense_amt_list,user_id)
    return(sum(debt_amt_list))

# def goal(user_id):
#     # TODO input goals and save in csv
#     pass