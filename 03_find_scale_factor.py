# To  Do

# Ask user for servings made by recipe (and check this is a number that is more than)
# Ask servings desired (check this is a number)
# Calculate the scale factor
# Warn the user if the sf less than 0.25 or more than 4

# Functions go here


# Number checking Function
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


# Main routine goes here

serving_size = num_check("what is the recipe serving size? ")
desired_size = num_check("How many servings as needed? ")

scale_factor = desired_size / serving_size

print("scale Factor: {}".format(scale_factor))
