""" Assignment 4

Aim : Write a Python program that accepts the length of three sides of a triangle as inputs. The program should indicate whether or not the triangle 
is a right - angled triangle using function.

Objectives: To learn and implement Function.
"""
#===========================================================================
# Algorithm:
# 1. Start
# 2. Define a function is_right_triangle(side1,side2,side3) that takes three side lengths as input.
# 3. Inside the function, sort the three side lengths in ascending order.
# 4. Check if the sum of the squares of the two smaller sides is equal to the square of the largest side.
# 5. If the condition is true, return True (indicating it is a right-angled triangle), otherwise return False.
# 6. Prompt the user to input the lengths of the three sides of the triangle.
# 7. Call the is_right_triangle function with the input side lengths.
# 8. Based on the return value of the function, print whether the triangle is right-angled or not.
# 9. End
#===========================================================================

#============================================================================
# Pseudocode:
# START
#
# DEFINE FUNCTION is_right_triangle(side1, side2, side3)
#     SORT side1, side2, and side3 in ascending order
#     STORE the sorted values as first_side, second_side, and largest_side
#
#     IF first_side^2 + second_side^2 = largest_side^2 THEN
#         RETURN TRUE
#     ELSE
#         RETURN FALSE
#     END IF
# END FUNCTION
#
# INPUT the lengths of the first, second, and third sides
#
# result = is_right_triangle(first input, second input, third input)
#
# IF result = TRUE THEN
#     DISPLAY "The sides form a right-angled triangle"
# ELSE
#     DISPLAY "The sides do not form a right-angled triangle"
# END IF
#
# END
#============================================================================



def is_right_triangle(side1,side2,side3):
    sides=sorted([side1,side2,side3])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True 
    else:
        return False

a = int(input("1st side length: "))
b = int(input("2nd side length: "))
c = int(input("3rd side length: "))

if is_right_triangle(a,b,c):
    print(f"Sides {a},{b},{c} form a right angled triangle")
else:
    print(f"Sides {a},{b},{c} do not form a right angled triangle")
