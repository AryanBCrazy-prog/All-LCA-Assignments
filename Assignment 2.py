""" Assignment 2

Problem Statement:
To find largest of three numbers.
Aim:
Write a python program to find the largest of three numbers.
Objectives:
To learn and implement different forms of if..else statement."""

#================================================================
#Algorithm:
#1. Start
#2. Take three numbers as input
#3. Compare the three numbers to find the largest
#4. Display the largest number
#5. Stop
#================================================================

#=================================================================
# PSUEDOCODE:
# BEGIN
# Input: three numbers a, b, c
# Output: the largest of the three numbers
#
# TRY
#   INPUT a, b, c (as floats from user)
#   IF a > b AND a > c THEN
#     OUTPUT: a is the largest
#   ELSE IF b > a AND b > c THEN
#     OUTPUT: b is the largest
#   ELSE
#     OUTPUT: c is the largest
#   END IF
# EXCEPT (invalid input)
#   OUTPUT: "Invalid input, must be a numeric value"
# END TRY
# END
#=================================================================

#using try and except block to handle invalid input
try:
    #taking float input from user
    a = float(input("Enter first value: "))
    b = float(input("Enter second value: "))
    c = float(input("Enter third value: "))

    #using if..elif..else statement to find the largest value
    if a>b and a>c:
        print(f"The largest value is a = {a}")
    elif b>a and b>c:
        print(f"The largest value is b = {b}")
    else:
        print(f"The largest value is c = {c}")

# handling invalid input
except:
    print("Invaild input , must be a numberic value")
