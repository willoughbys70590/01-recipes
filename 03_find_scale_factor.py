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

print("scale Factor: {}".format(scale_factor))
