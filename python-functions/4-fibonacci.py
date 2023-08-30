# def fibonacci_sequence(n):
#     if n <= 0:
#         return []
#     fibonacci_sequence = (0, 1)
#     n = n_(n-1) + n_(n-2) 
# print(fibonacci_sequence(6))
# print(fibonacci_sequence(1))
# print(fibonacci_sequence(0))
# print(fibonacci_sequence(20))

def validate_password(password):
    # Check length
    if len(password) < 8:
        return False
    
    # Check for uppercase, lowercase, and digit
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    
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
