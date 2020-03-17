import re

# ingredient has mixed factions followed y unit and ingredient
recipe_line = "1 1/12 ml flour" # change to input statement in due course

mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"

if re.match(mixed_regex, recipe_line):
        print("true")
        # Get mixed numbers by matching the regex
        pre_mixed_num = re.match(mixed_regex, recipe_line)
        mixed_num = pre_mixed_num.group()

        # Replace space with a + sign...
        amount = mixed_num.replace(" ", "+")
        # change the stiring into a decimal
        amount = eval(amount)
        print(amount)

        # Get unit and inghredient...
        compile_regex = re.complile(mixed_regex)
        print(compile_regex)
        unit_ingredient = re.split(compile_regex, recipe_line)
        print(unit_ingredient)


get_unit = unit_ingredient.split(" ", 1)        # splits text at first space
print(get_unit)