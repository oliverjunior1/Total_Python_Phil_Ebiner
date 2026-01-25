# Create a function called describe_person, which takes his name as parameters and then an indeterminate number of
# arguments. This function should display on the screen:
#
# Characteristics of {name}:
# {argument_name}: {argument_value}
# {argument_name}: {argument_value}
# etc...
# For example:
#
# describe_person("Ash", eye_color="brown", hair_color="black")
#
# Will print to the screen:
#
# Characteristics of Ash:
# eye_color: brown
# hair_color: black

def describe_person(name, **kwargs):
    print(f"Characteristcs of {name}")
    for x, y in kwargs.items():
        print(f"{x}:{y}")

describe_person()
