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


# Number checking Function (number must be afloat that is more than 0)
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


def get_all_ingredients():
    # Set up empty ingredients list
    ingredients = []

stop = ""
while stop != "xxx":
    # Ask user for ingredient (via not blank function)
    get_ingredients = not_blank("please type in an ingredient name (or 'xxx')",
                                "this cant be blank",
                                "yes")

    # stop loopin if exit code is typed and there are more
    # than 2 ingredients
    if get_ingredients.lower() == "xxx" and len(ingredients) > 1:
        break

    # If exit code is not entered, add ingredient to list
    else:
        ingredients.append(get_ingredients)

        return ingredients


def general_converter(how_much, lookup, dictionary, conversion_factor):

    if lookup in dictionary:
        mult_by = dictionary.get(lookup)
        how_much = how_much * float(mult_by) / conversion_factor
        converted = "yes"

    else:
        converted = "no"

    return [how_much, converted]

def unit_checker(unit):

    unit_tocheck = unit

    # Abbreviation lists
    teaspoon = [" tsp", "teaspoon", "t"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp"]
    ounce = ["oz", "ounce", "fl oz"]
    cup = ["c", "cup", "cups"]
    pint = ["p", "pt", "fl pt"]
    quart = ["q", "qt", "fl qt"]
    mls = ["ml", "milliliter", "milliltre"]
    liter = ["litre", "liter", "l"]
    pound = ["pound", "lb", "#"]

    if unit_tocheck == "":
        # print("you chose {}".format(unit_tocheck))
        return unit_tocheck
    elif unit_tocheck == "T" or unit_tocheck.lower() in tablespoon:
        return "tbs"
    elif unit_tocheck.lower() in teaspoon:
        return "tsp"
    elif unit_tocheck.lower() in ounce:
        return "ounce"
    elif unit_tocheck.lower() in cup:
        return "cup"
    elif unit_tocheck.lower() in pint:
        return "pint"
    elif unit_tocheck.lower() in quart:
        return "quart"
    elif unit_tocheck.lower() in mls:
        return "mls"
    elif unit_tocheck.lower() in liter:
        return "litre"
    elif unit_tocheck.lower() in pound:
        return "pound"

# ****** Main Routine goes here *******
unit_central = {
        "tsp": 5,
        "tbs": 15,
        "cup": 237,
        "ounce": 30,
        "print": 473,
        "quart": 946,
        "pound": 454,
        "liter": 1000,
    }

# *** generate food dictionaries ****
# open file
groceries = open('01_ingredients_ml_to_g.csv')

# Read data into a list
csv_groceries = csv.reader(groceries)

# Create a dictionary to hold the data
food_dictionary = {}

# Add the data from the list into the dictionary
# (first item in a row is key, next is definition)

    for row in csv_groceries:
        food_dictionary[row[0]] = row[1]

    # print(food_dictionary)


# ***** Main routine ******

# set up dictionaries

# set up list to hold 'modernised' ingredients
modernised_recipe = []

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

# Get amounts, units and ingredients from user...
full_recipe = get_all_ingredients()

# print(full_recipe)

# Split each line of the recipe into amount, unit and ingredient...
mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"
convert = "yes"

for recipe_line in full_recipe:
    recipe_line = recipe_line.strip()

    # Get amount...
    if re.match(mixed_regex, recipe_line):

        # Get mixed numbers by matching the regex
        pre_mixed_num = re.match(mixed_regex, recipe_line)
        mixed_num = pre_mixed_num.group()

        # Replace space with a + sign...
        amount = mixed_num.replace(" ", "+")
        # change the stiring into a decimal
        amount = eval(amount)
        amount = amount * scale_factor
        print(amount)

        # Get unit and inghredient...
        compile_regex = re.compile(mixed_regex)
        unit_ingredient = re.split(compile_regex, recipe_line)
        unit_ingredient = (unit_ingredient[1]).strip()  # remove extra white space from

    else:
        get_amount = recipe_line.split(" ", 1)      # split line at first space

        try:
            amount = eval(get_amount[0])        # convert amount to float if possible
            amount = amount * scale_factor
        except NameError:
            amount = get_amount[0]
            modernised_recipe.append(recipe_line)
            continue

        unit_ingredient = get_amount[1]

    # Get unit and ingredient...
    get_unit = unit_ingredient.split(" ", 1)        # splits text at first space

    unit = get_unit[0]
    # Convert unit to ml

    num_spaces = recipe_line.count(" ")
    if num_spaces > 1:
        # item has unit and ingredient
        unit = get_unit[0]
        ingredient = get_unit[1]
        unit = unit_checker(unit)

        #if unit is already in grams, add it to list
        if unit == "g":
            modernised_recipe.append("{:0f} g{}".format(amount, ingredient))
            continue

        # convert to mls if possible...
        amount = general_converter(amount, unit, unit_central, 1)
        # print(amount)

        #if we converted to mls try and convert to grams
        if amount[1] == "yes":
            amount_2 = general_converter(amount[0], ingredient, food_dictionary,250)

            #if the ingredient is in the list,covert it
            if amount_2[1] == "yes":
                modernised_recipe.append("{:.0f} g {}".format(amount_2[0], ingredient))     # rather than printing, update modernised list (g)

            # if the ingredient is not in the list, leave the unit as ml

            else:
                modernised_recipe.append("{:.0f} ml {}".format(amount(0), unit_ingredients))
                continue
        # If the unit is not mls, leave the line unchanged
        else:
            modernised_recipe.append("(:.2f) () ()".format(amount(0),unit, ingredients))


    else:
        # Items only has ingredient (no unit)
        modernised_recipe.append("{} {}".format(amount, unit_ingredient))

 # Put updated ingredient in list


# output ingredient list
for items in modernised_recipe:
    print(items)

