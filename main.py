def is_strong_password(password):
  if 8 <= len(password) <= 20:
    if (password[0].isalpha() and 
        any(c.islower() for c in password) and 
        any(c.isupper() for c in password) and 
        any(c.isdigit() for c in password) and 
        any(c.isalnum() for c in password) and 
        not any (c.isspace() for c in password)):
        for i in range(len(password) - 2):
          if (password[i] == password[i+1] == password[i+2]):
            return False
        return True
    else:
      return False
  else:
    return False


print(is_strong_password("a12348B!"))#returns True
print(is_strong_password("15845"))#returns False
print(is_strong_password("happyTime1299"))))#returns True
print(is_strong_password("open sesame12@"))))#returns False
print(is_strong_password("open@me_Mr"))))#returns False
print(is_strong_password("Iwin"))))#returns False
