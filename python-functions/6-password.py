def validate_password(password):
    if password < 8: 
      return False 
    if password:
      pass_uppercase = True
      pass_lowercase = True
      pass_digit = True
       
    else:
       return False

print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))