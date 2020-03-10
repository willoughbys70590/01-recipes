# import re

# ingredient has mixed factions followed y unit and ingredient
recipe_line = "1 1/12 ml flour" # change to input statement in due course

mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"

if re.match(mixed_regex, recipe_line):
    print("True")
else:
    print("False ")