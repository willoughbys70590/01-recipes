# Get's recipe name and checks it is not blank


# Not blank Function goes here
def not_blank(question):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            continue
        else:
            return response


# Main routine goes here

recipe_name = not_blank("what is the recipe name?")

print("you are making {}". format(recipe_name))
