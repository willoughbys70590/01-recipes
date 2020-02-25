# Ingredients List


# Not blank Function goes here
def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # look at each character in string and if its a number
            for letter in response:
                if letter.isidigit():
                    has_errors = "yes"

        if response == "" or has_errors != "":
            print(error)
            continue
        else:
            return response

# Main routine...

# Set up empty ingredients list
ingredients = []

# Loop to ask user to enter an ingredient
stop = ""
while stop != "xxx":
    # Ask user for ingredient (via not blank function)
    get_ingredients = not_blank("please type in an ingredient name (or 'xxx')",
                                "this cant be blank",
                                "yes")

    # stop loopin if exit code is typed and there are more
    # than 2 ingredients
    if get_ingredients.lower() == "xxx" and len(ingredients) >  1:
        break

    # If exit code is not entered, add ingredient to list
    else:
        ingredients.append(get_ingredients)

# Output list
print(ingredients)

