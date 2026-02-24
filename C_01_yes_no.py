# Functions go here
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

# Main routine goes here
levels = ['easy', 'medium', 'hard']
while True:
    want_instructions = string_check(question="Do you want to see instructions?", valid_ans_list=['yes', 'no'])
    print(f"You chose {want_instructions}")
