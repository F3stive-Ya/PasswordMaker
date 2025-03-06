import random 


def create_db(file_name):
    #Creates a file and write to it, returns True
    #If error, returns False
    try:
        with open(file_name, 'w') as file:
            pass
        return True
    except:
        return False
    
    

def read_users(file_name):
    
    #Create empty lists of usernames and passwords
    #Returns user_Lst, pass_Lst
    try:
        user_Lst = []
        pass_Lst = []

        with open(file_name, 'r') as file:
            for line in file:
                #Split lines using ',' as a delimiter
                data = line.strip().split(',')
                if len(data) >= 2:
                    user_Lst.append(data[0])
                    pass_Lst.append(data[1])

        return user_Lst, pass_Lst
    except:
        #If the program somehow got here without creating the file
        return None, None
    
        
def display_users(names, passwords):
    # In charge of formatting the end table

    #No user
    if not names or not passwords:
        print("No user found")

        

        
    else:
        #Print the headers with set distances between
        print(f"{'No.':<5} {'Username':<16} {'Password':<16}")
        print("-" * 33)

        #Create an indexed list of tuples
        #Print the list formatted
        for i, (names, passwords) in enumerate(zip(names, passwords), 1):
            print(f'{i:<5} {names:<16} {passwords:<16}')
    
    
    

def valid_name(name):
    # Function validates passed argument to check if >= 3 
    # and if string is only letters
    
    if len(name) >= 3 and name.isalpha():
        with open(USER_DB, 'r') as file:
            #strip and split all lines
            for line in file:
                line = line.strip()
                row = line.split(',')
                if name == row[0]:  
                    print("User already exists.")
                    return False  # Name exists, return False
        return True  # Name is valid and doesn't exist in the file
    else:
        print("Name is invalid.")
        return False  # Invalid name

def generate_password(name):
    first_Let = name[0]
    length = str(len(name))
    i = 0
    
    #Create Strings of possible information
    lower_Set = "abcdefghijklmnopqrjtuvyxyz"
    high_Set = lower_Set.upper()
    digit_Set = "0123456789"
    special_Set = "+-_#$/*"

    #Append all Strings into one Mega String
    password_Set = lower_Set + high_Set + digit_Set + special_Set

    #[a-z][0-9] added to password
    password = first_Let + length
    
    #Make a random selection from password_Set
    #Do this 6 times over and append

    
    while i < 6:
        intLetter = random.choice(password_Set)
        password = password + intLetter
        i += 1
    return password

def sign_up(file_name):

    user_Num = 0
    
    while True:  # Infinite loop that will only stop when 's' is entered
        name = str(input("Enter name ('s' to Stop): "))
        
        if name == 's':
            break
        
        if valid_name(name):  # Check if the name is valid and not already taken
            password = generate_password(name)
            print(f"Hello {name}, your password is: {password}")
            user_Num += 1
            with open(file_name, 'a') as file:
                file.write(f"{name},{password}\n")  # Save the new user with their password
        
                
    return user_Num


    

def change_password(file_name, name, new_password):
    #Return True not in group of 3
    return True
    

    
    


USER_DB = 'UserPassword.csv'

print(USER_DB)

# == DO NOT MODIFY ANY CODE BELOW THIS LINE ==

def main(): 
    print('Create DB:', create_db(USER_DB)) # Create DB: True
    names, passwords = read_users(USER_DB)
    display_users(names, passwords)  # No user found

    print('Count:', sign_up(USER_DB))
    names, passwords = read_users(USER_DB)
    display_users(names, passwords)

    print('Change first name:',      # Change first name: True
         change_password(USER_DB, names[0], 
                          generate_password(names[0]))) 
    print('Change last name: ',      # Change last name: True
          change_password(USER_DB, names[len(names) - 1], 
                          generate_password(names[len(names) - 1])))
    print('Change dumb name: ',      # Change dumb name: False
         change_password(USER_DB, 'ProfSun', # Username does not exist
                         generate_password('ProfSun'))) 

    names, passwords = read_users(USER_DB)
    display_users(names, passwords)
    
if __name__ == '__main__':
    main()