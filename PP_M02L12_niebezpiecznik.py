
password = input("Insert password: ")

# conditions that the password must meet
length = False
lowercase = False
uppercase = False
special_char = False
no_space = True

# check if the conditions are met
if len(password) >= 8:
    length = True
for char in password:
    if char.isalpha() and char.islower():
        lowercase = True
    if char.isalpha() and char.isupper():
        uppercase = True
    if (not char.isalpha()) and (not char.isspace()):
        special_char = True
if password.isspace() or ' ' in password:
    no_space = False
       
conditions_met = length and lowercase and uppercase and special_char and no_space


# password is secure
if conditions_met:
    print("Your password is secure.")

# password is NOT secure - recommendations
else:
    recommendation = ""
    if not length:
        recommendation += "- Your password must have at least 8 characters.\n"
    if not lowercase:
        recommendation += "- Your password must include a lowercase letter.\n"
    if not uppercase:
        recommendation += "- Your password must include an uppercase letter.\n"
    if not special_char:
        recommendation += "- Your password must include a special character.\n"
    if not no_space:
        recommendation += "- Your password CANNOT include any whitespace characters.\n"

    print("Your password is not secure enough. Please comply to the following recommendations:")
    print(recommendation)
