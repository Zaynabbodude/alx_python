def validate_password(password):
    if password > 8: 
      return True 
    if password == ("uppercase, lowercase, digit"):
       return True
    else:
       return False

print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))