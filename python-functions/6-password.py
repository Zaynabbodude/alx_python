def validate_password(password):
  
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        
        if has_uppercase and has_lowercase and has_digit:
            break
    
    if not (has_uppercase and has_lowercase and has_digit):
        return False
    
    # Check for spaces
    if ' ' in password:
        return False
    
    return True

print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))