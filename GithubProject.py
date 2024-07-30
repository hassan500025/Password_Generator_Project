    # Password Generator Project :
    # Random And String Package :


import random
import string

         # Function to get the username :
         
def get_username():
    username = input("Enter Your Username : ")
    return username

         # Function to get the password length :
         
def get_password_length():
    length = int(input("Enter The Length Of The Password (Between 5 And 10 Characters OtherWise Default Is 8) : "))
    if str(length).isdigit() and 5 <= length <= 10:
        return length
    else:
        print("Using Default Length : 8")
        return 8

        # Function to get the password operator :
        
def get_password_operator():
    operator = {
        'Uppercase' : input("Include Uppercase Letters ? (Yes/No, Default Is Yes): ").lower() in ['Yes', ''],
        'Lowercase': input("Include Lowercase Letters ? (Yes/No, Default Is Yes): ").lower() in ['Yes', ''],
        'Digits': input("Include Digits ? (Yes/No, Default Is Yes): ").lower() in ['Yes', ''],
        'Symbols': input("Include Symbols ? (Yes/No, Default Is Yes): ").lower() in ['Yes', '']
    }
    
             # Ensure at least one operator is selected
             
    if not any(operator.values()):
        print("No Operator Selected OrherWise Using Default Operator : Include All Character Types.")
        operator = {'Uppercase': True, 'Lowercase': True, 'Digits': True, 'Symbols': True}
    return operator

               # Function to generate the password

def generate_password(length, operator):
    chars = ''
    if operator['Uppercase']:
        chars += string.ascii_uppercase
    elif operator['Lowercase']:
        chars += string.ascii_lowercase
    elif operator['Digits']:
        chars += string.digits
    elif operator['Symbols']:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

         # Main loop
while True:
       # Get the username
    username = get_username()
    
       # Get the password length
    length = get_password_length()

       # Get the password operator
    operator = get_password_operator()

       # Generate the password
    password = generate_password(length, operator)

       # Display the generated username and password
    print(f"Your Generated Username Is : {username}")
    print(f"Your Generated Password Is : {password}")

       # Ask if the user wants to generate another username and password
    again = input("Do You Want To Generate Another Username And Password ? (Yes/No): ").lower()
    if again != 'yes':
        print('Tnx For Using Our Program 😍')
        break
