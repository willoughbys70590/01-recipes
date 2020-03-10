# convert fuctions...


# ***** Functions go here ******
def general_converter(how_much, lookup, dictionary, conversion_factor):

    if unit in dictionary:
        mult_by = dictionary.get(unit)
        how_much = how_much * mult_by
        print("Amount in ml{}".format(how_much))
    else:
        print("{} is unchanged".format(how_much))

def unit_checker():

    unit_tocheck = input ("Unit? ")

    # Abbreviation lists
    teaspoon = [" tsp", "teaspoon", "t"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp"]
    ounce = ["oz", "ounce", "fl oz"]
    cup = ["c"]
    print = ["p", "pt", "fl pt"]
    quart = ["q", "qt", "fl qt"]
    mls = ["ml", "milliliter", "milliltre"]
    liter = ["litre", "liter", "l"]
    pound = ["pound", "lb", "#"]

    if unit_tocheck == "":
        print("you chose {}".format(unit_tocheck))
        return unit_tocheck

    elif unit_tocheck == "T" or unit_tocheck.lower () in tablespoon:
        return "tbs"
    elif unit_tocheck.lower() in teaspoon:
        return "tsp"
    elif unit_tocheck.lower() in ounce:
        return "ounce"
    elif unit_tocheck.lower() in cup:
        return "cup"
    elif unit_tocheck.lower() in print:
        return  "print"
    elif unit_tocheck.lower() in quart:
        return "quart"
    elif unit_tocheck.lower() in mls:
        return "mls"
    elif unit_tocheck.lower() in litre:
        return "litre"
    elif unit_tocheck.lower() in pound:
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
    "liter":1000,
}

Keep_going  = ""
while Keep_going == "":
    amount = eval(input("How much?  "))
    amount = float(amount)

    # Get units and change it to match dictionary.
    unit = unit_checker()

    amount = general_converter(amount, unit, unit_central, 1)
    print(amount)

    # Keep_going = input("<enter> or q ")
