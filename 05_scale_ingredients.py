# Ingredients List


# Number checking Function
def num_check(question):

    error = "please enter a number that is more than zero"

    valid = False
    while not valid:

        # if response is the exit code, return the exit code
        response = input(question)

        if response.lower() == "xxx":
            return "xxx"

        # Otherwise check that the response is a number that is more than zero
        try:
            response = float(response)

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


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

# Replace line below with component 3 in due course
scale_factor = eval(input("scale Factor "))

# Set up empty ingredients list
ingredients = []

# Loop to ask user to enter an ingredient
stop = ""
while stop != "xxx":

    amount = num_check("what is the amount for the ingredients? ")

    # stop loopin if exit code is typed and there are more
    # than 2 ingredients
    if amount == "xxx" and len(ingredients) >  1:
        break

    elif amount == "xxx" and len (ingredients) <2:
        print("you need at least two ingredients in the list.  "
              "please add more ingredients. ")
    # If exit code is not entered, add ingredient to list
    else:
        # Ask user for ingredient (via not blank function)
        get_ingredients = not_blank("please type in an ingredient name ",
                                    "this cant be blank",
                                    "yes")
        amount = float(amount) * scale_factor

        # Remove decimal point for whole numbers
        if amount % 1 == 0:
            amount = int(amount)
        elif amount * 10 % 1 == 0:
            amount = "{:.1f}".format(amount)
        else:
            amount = "{:.2f}".format(amount)

        ingredients.append("{} units {}".format(amount, get_ingredients))

# Output list
for items in ingredients:
    print(item)
