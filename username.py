import sys
import os

def generate_usernames(first_name, last_name):
    usernames = []
    # Add username combinations with uppercase letters
    usernames.append(first_name[0].upper() + '.' + last_name.capitalize())
    usernames.append(first_name.capitalize() + '.' + last_name[0].upper())
    usernames.append(first_name.capitalize() + last_name.capitalize())
    usernames.append(last_name.capitalize() + '.' + first_name.capitalize())
    usernames.append(last_name.capitalize() + first_name.capitalize())
    # Add username combinations with lowercase letters
    usernames.append(first_name[0].lower() + '.' + last_name.lower())
    usernames.append(first_name.lower() + '.' + last_name[0].lower())
    usernames.append(first_name.lower() + last_name.lower())
    usernames.append(last_name.lower() + '.' + first_name.lower())
    usernames.append(last_name.lower() + first_name.lower())
    # Add first name and last name themselves
    usernames.append(first_name)
    usernames.append(last_name)
    return usernames

def process_file(input_file):
    usernames = []
    with open(input_file, 'r') as file:
        for line in file:
            names = line.strip().split()
            if len(names) == 2:
                first_name, last_name = names
                usernames.extend(generate_usernames(first_name, last_name))
    return usernames

def save_usernames(usernames, output_file):
    with open(output_file, 'w') as file:
        for username in usernames:
            file.write(username + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python username.py inputfile outputfile")
        sys.exit(1)
    
    input_file = sys.argv[1]
    if not os.path.isfile(input_file):
        print("Invalid input file path.")
        sys.exit(1)
        
    output_file = sys.argv[2]

    usernames = process_file(input_file)
    save_usernames(usernames, output_file)
    print(f"Usernames have been saved to {output_file}")
