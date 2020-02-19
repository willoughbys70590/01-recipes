# Iterates through string...

# ask user for string
recipe_stacy = input("what is the recipe name? ")

error = "Your recipe name has numbers in it."
has_error ="yes"

# look at each character in string and if its a number, complain
for letter in recipe_stacy:
    if letter.isdigit() == True:
        print(error)
        has_errors = "yes"
        break

    # give user feedback...
if has_error != "yes":
    print("you are OK")