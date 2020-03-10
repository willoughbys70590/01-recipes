# ask user for amount
# ask user for unit
# check that unit is in dictionary

# if unit in dictionary, covert to mL

# if no unit given / unit is unknown, Leave as is.


# ***** Functions go here ******
def unit_checker():

    unit_tocheck = input ("Units? ")

    # Abbreviation lists
    teaspoon = [" tsp", "teaspoon", "t"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp"]

    if unit_tocheck == "":
        print("you chose {}".format(unit_tocheck))
        return unit_tocheck

    elif unit_tocheck == "T" or unit_tocheck.lower () in tablespoon:
        return "tbs"
    elif unit_tocheck.lower() in teaspoon:
        return "pound"

# ****** Main Routine goes here *******
unit_central  = {
    "tsp":5,
    "tbs":15,
    "cup" : 237,
    "ounce": 30,
    "print": 473,
    "quart": 946,
    "pound":454,
}

Keep_going  = ""
while Keep_going == "":
    amount = eval(input("How much?  "))
    amount = float(amount)

    # Get units and change it to match dictionary.
    unit = unit_checker()

    if unit in unit_central:
        mult_by = unit_central.get(unit)
        amount = amount * mult_by
        print("amount in ml {}". format(amount))
    else:
        print("{} is unchanged".format(amount))

    Keep_going = input("<enter> or q ")
