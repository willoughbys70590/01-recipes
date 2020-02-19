# Get's recipe name and checks it is not blank

# To do
# Allow users to specify a custom error message
# Allow  users to specify wheather numbers are allowed

# Not blank Function goes here
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


# Main routine goes here

source = not_blank("Where is the recipe from?",
                   "The recipe source can't be blank",
                   "yes")

print("Source:  {}". format(source))
