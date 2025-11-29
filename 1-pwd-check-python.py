# Chandan
# Hero Vired Assigned 1 - Python Programming

# Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential.
# Create a Python script to check the strength of the password.
# Simple password strength checker

def check_password_strength(password):
    # Start with all checks as False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special= False

    # Check length first
    if len(password) < 8:
        print("Password is too short. It must be at least 8 characters long.")
        return False

    # Go through each character in the password one by one
    for ch in password:
        if ch >= 'A' and ch <= 'Z':
            has_upper = True
        elif ch >= 'a' and ch <= 'z':
            has_lower = True
        elif ch >= '0' and ch <= '9':
            has_digit = True
        else:
            # Treat anything else as special character
            has_special = True

    # Now check all the conditions one by one
    if not has_upper:
        print("Password must contain at least one uppercase letter.")
    if not has_lower:
        print("Password must contain at least one lowercase letter.")
    if not has_digit:
        print("Password must contain at least one digit (0-9).")
    if not has_special:
        print("Password must contain at least one special character (like !, @, #, $, %).")

    # If all are True then password is strong
    if has_upper and has_lower and has_digit and has_special:
        return True
    else:
        return False


# Main program
password = input("Enter a password: ")

if check_password_strength(password):
    print("Password is strong. All rules are satisfied.")
else:
    print("Password is not strong. Please follow the above messages.")
