str.isalnum()
# This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
print('ab123'.isalnum())
# This return True
print('ab123#'.isalnum())
# This return False

# -------------------------------------
str.isalpha()
#This method checks if all the characters of a string are alphabetical (a-z and A-Z).
print('abcD'.isalpha())
# this return True
print('abcd1'.isalpha())
# this return False

# -------------------------------------
str.isdigit()
# This method checks if all the characters of a string are digits (0-9).
print('1234'.isdigit())
# this return True
print('123edsd'.isdigit())
# this return False

# -------------------------------------
str.islower()
# This method checks if all the characters of a string are lowercase characters (a-z).
print('abcd123#'.islower())
# this return True
print('Abcd123#'.islower())
# this return False

# -------------------------------------
str.isupper()
# This method checks if all the characters of a string are uppercase characters (A-Z).
print('ABCD123#'.isupper())
# this return True
print('Abcd123#'.isupper())
# this return False
