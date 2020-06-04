def input_user_id():
    #Enter user_id
    print('User ID')
    print('-'*25)
    user_id = int(input('Enter your User ID: ',))
    print('-'*25)
    print('')

    return(user_id)

def initial_input(user_id):
    print('')
    fixed_income = float(input('How much is your monthly income? \n',))
    print('')

    print("You're kicking! Next, let's talk about savings. \n")
    print('In managing our finance right, it is important to save our money before we spend it.')
    print("Once we've set aside some amount for savings, the rest of the money will be wholly ours to spend without guilt. \n")
    fixed_saving = float(input(f'How much out of the RM{fixed_income} do you wish to save?\n',))
    print("\nThat's a great start! This is just an initial amount, if you feel like saving more, you can always update in the future")
    print('Remember, the more money we save today, the more money we will have to spend later.\n')

    print('Next, list down all your fixed expenses, such as house rent, streaming subscriptions, etc.')
    print('These expenses are fixed in nature, such that you will be paying the same amount every month. \n')
    fixed_expense = get_total_fixed_expense(user_id)
    print("You're doing great! Now, all your fixed expenses are checked.")
    print("we will keep those in mind for you, so you don't have to worry about it. ;)\n")

    print("Now, let's move on to the variable expenses \n")
    print("Contrary to the fixed expenses, these expenses aren't the same each month.")
    print('These are things like your groceries, fuel, or the monthly dates with your special ones. \n')
    variable_expense = get_total_variable_expense(user_id)
    print('Awesome! Now, we have your estimated variable expenses.')
    print("Every month, we will tell you how much your monthly spending as compared to ones you've listed.")
    print('You can always update anytime if you think the estimations are too far off.\n')

    print("The next component is an important component in financial planning that people don't prioritize, insurance")
    print("Insurance is preparing for the worst case. The chances of you being permanently disabled is low, however we need to cater that, just in case.")
    print("Two main insurance needed are medical insurance, and life insurance.\n")
    is_life_insurance = input('Do you have life insurance?\n',)
    is_medical_insurance = input('Do you have medical insurance?\n',)
    print("\nIf you still don't have an insurance, don't worry. There are many options in the market.")
    print("When you're free, you can contact your high school friends who are now insurance agents, or better, you can talk to us here.")
    print("We will help you decide which insurance is best for you.")
    return fixed_income, fixed_expense, variable_expense, fixed_saving, is_life_insurance, is_medical_insurance

def variable_input():
    print('Variable values')
    print('-'*50)
    month, year = int(input('Month:',)), int(input('Year:',))
    print('')
    variable_income = float(input("Enter this month's variable income:",))
    variable_saving = float(input("Enter this month's additional savings:",))
    account_balance = float(input("Enter this month's total account balance:",))
    return month, year, variable_income, variable_saving, account_balance

def get_total_fixed_expense(user_id):
    # TODO save total fixed expense in a sheet
    expense_type = ''
    i = 1
    expense_amt_list = []
    expense_type_list = []
    while expense_type != 'exit':
        #input
        expense_type = input(f'Fixed Expense {i}: ',)
        expense_amt = float(input('Monthly payment: ',))
        ask_more = input('\nDo you have more fixed expenses?\n', )
        print('')
        #append to list
        expense_type_list.append(expense_type)
        expense_amt_list.append(expense_amt)
        #when to break
        if ask_more != 'yes':
            break
        i += 1

    # save to csv
    ## read current csv
    ## delete previous entries of the id
    ## create
    ## append new entry of the id
    ### do the same for below
    
    return(sum(expense_amt_list))

def get_total_variable_expense(user_id):
    # TODO save total_variable expense somewhere
    expense_type = ''
    i = 1
    expense_amt_list = []
    expense_type_list = []
    while expense_type != 'exit':
        #input
        expense_type = input(f'Variable Expense {i}: ',)
        expense_amt = float(input('Estimated Amount: ',))
        print('')
        ask_more = input('Add more fixed expenses?\n', )
        print('')
        #append to list
        expense_amt_list.append(expense_amt)
        expense_type_list.append(expense_type)
        #when to break
        if ask_more != 'yes':
            break
        i += 1
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
        debt_enddate = input('Final payment date (dd/mm/yyyy): ',)

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
    return(sum(debt_amt_list))

def goal(user_id):
    print('')
    print('Goal')
    print('-'*50)

    goal_type = ''
    i = 1
    goal_type_list = []
    goal_amt_list = []
    goal_enddate_list = []
    while goal_type != 'exit':
        #input
        goal_type = input(f'Goal {i}: ',)
        goal_amt = float(input('Goal Amount: ',))
        goal_enddate = input('When you need the money (dd/mm/yyyy): ',)

        ask_more = input('Do you have any more goal? Answer: ', )
        #append to list
        goal_type_list.append(goal_type)
        goal_amt_list.append(goal_amt)
        goal_enddate_list.append(goal_enddate)
        #when to break
        if ask_more != 'yes':
            break
        i += 1
    print('-'*50)
    return(goal_type_list, goal_amt_list)