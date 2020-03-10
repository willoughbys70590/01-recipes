# modules to be used...
# import csv

# ***** Functions ******

def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        has_errors = ""
        response = input(question)

        if num_ok !="yes":
            # look at each character in string and if its a number, complain
            for letter in response:
                if letter.isdigit():
                    has_errors = "yes"
                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response

# ***** Main routine ******

# set up dictionaries

# set up list to hold 'modernised' ingredients

# Ask user for recipe name and check its not blank
recipe_name = not_blank("what is the recipe name?",
                        "The recipe name cant be blank and cant contain numbers",
                        "no")
# Ask user where for recipe is originally from (numbers OK)
source = not_blank("Where is the recipe from?",
                   "The recipe source can't be blank",
                   "yes")
# Get serving sizes and scale factor

# Loop for each ingredient...

# Get ingredient amount
# Get ingredient name
# Get unit
# Convert unit to ml
# Convert from ml to g
# Put updated ingredient in list
