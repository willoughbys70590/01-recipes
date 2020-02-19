# To  Do

# Ask user for servings made by recipe (and check this is a number that is more than)
# Ask servings desired (check this is a number)
# Calculate the scale factor
# Warn the user if the sf less than 0.25 or more than 4

# Functions go here



# Main routine goes here

serving_size = float(input("what is the recipe serving size? "))
desired_size = float(input("How many servings as needed? "))

scale_factor =desired_size / serving_size

print("scale Factor: {}".format(scale_factor))