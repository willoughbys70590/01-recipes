# modules to be used...
import csv
import re

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
# Number checking Function (number must be afloat that ismore than 0)
def num_check(question):

    error = "please enter a number that is more than zero"

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def get_sf():
    serving_size = num_check("what is the recipe serving size? ")
    desired_size = num_check("How many servings as needed? ")

    scale_factor = desired_size / serving_size

    if scale_factor <0.25:
        dodgy_sf = input("warning: This scale factor is very small"
                      " might struggle to accurately weigh the ingredients. \n"
                      "do you want to fix this and make more servings? ").lower()
    elif scale_factor > 4:
         dodgy_sf = input("warning: this scale factor is quite large - you might "
                      "have issues with mixing bowl volumes and oven space.  "
                      "\nDo you want to fix this and make a smaller "
                      "batch? ").lower()
    else:
        dodgy_sf = "no"

    return  scale_factor

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
scale_factor = get_sf()
print(scale_factor)
# Loop for each ingredient...

# Get ingredient amount
# Get ingredient name
# Get unit
# Convert unit to ml
# Convert from ml to g
# Put updated ingredient in list
