""" 
Assignment 5

Problem Statement:
Introduction to string

Aim :
Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9). 

Objectives:
1.To learn the basics of string and it's operation.
2.To learn the Variable declaration, User input and output using string in python programming 

"""
#===============================================================================================================================
# Algorithm:
# 1. Start.
# 2. Import Python's regular expression module.
# 3. Read a string from the user.
# 4. Create a regular expression pattern that accepts only:
#       a-z, A-Z, and 0-9.
# 5. Match the complete input string against the pattern.
# 6. If the complete string matches the pattern, display that the string
#    contains only letters and digits.
# 7. Otherwise, display that the string contains invalid characters.
# 8. Stop.
#===============================================================================================================================

#===============================================================================================================================
# Pseudo Code:
# START
#    IMPORT regular expression module
#    INPUT string
#    pattern ← "[a-zA-Z0-9]+"
#
#    IF the complete string matches pattern THEN
#        PRINT "The string contains only letters and digits."
#    ELSE
#        PRINT "The string contains invalid characters."
#    END IF
# STOP
#===============================================================================================================================

import re

# Read a string from the user
user_string = input("Enter a string: ")

# Create a regular expression pattern that accepts only a-z, A-Z, and 0-9
pattern = r"[a-zA-Z0-9]+"

# Match the complete input string against the pattern
if re.fullmatch(pattern, user_string):
    print("The string contains only letters and digits.")
else:
    print("The string contains invalid characters.")