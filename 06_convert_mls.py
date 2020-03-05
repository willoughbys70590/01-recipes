# ask user for amount
# ask user for unit
# check that unit is in dictionary

# if unit in dictionary, covert to mL

# if no unit given / unit is unknown, Leave as is.

unit_central  = {\
    "tsp":5,
    "tbs":15,
    "cup" : 237,
    "ounce": 30,
    "print": 473,
    "quart": 946,
    "pound":454,
}

amount = eval(input("how much?  "))
amount = float(amount)

unit = input("units?  ")

if unit in unit_central:
    mult_by = unit_central.get(unit)
    amount = amount * mult_by
    print("amount in ml {}". format(amount))
else:
    print("{} is unchanged".format(amount))