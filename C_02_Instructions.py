# Functions go here
def make_statement(statement, decoration):
    """Emphasis headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_ans_list):
    """checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response ==item[0]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


def instructions():
    make_statement("instructions", "ℹ️")

    print('''

This program will ask you for...
    - The name of the product you are selling
    - How many items you plan on selling
    - The costs for each component of the product
    (variable expenses)
    - Whether or not you have fixed expenses ( if you have
    fixed expenses, it will ask you what they are).
    - How much money you want to make (ie: your profit goal)
    
    It will also ask you how much the recommended sales price should
    be rounded to.
    
    The program outputs an itemised list of the variable and fixed
    expenses (which include the subtotals for these expenses).
    
    Finally it will tell you how much you should sell each item for 
    to reach your profit goal.
    
    The data will also be written to a text file which has the 
    same name as your product and today's date.

    ''')


# Main Routine goes here

make_statement("Fund Raising Calculator", "🔥")

print()
want_instructions = string_check("Do you want to see the instructions? ",['yes', 'no'])

if want_instructions == "yes":
    instructions()

print()
print("program continues... ")