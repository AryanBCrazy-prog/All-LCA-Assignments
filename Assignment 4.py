""" Assignment 4

Problem Statement :
Write a Python program to create an array and perform addition of two matrices.(Using list and NumPy array.)

Aim: write a Python program to create an array and perform addition of two matrices.

Objective: 
To learn the basics of array and it's operation.
To learn the mathematical operations using arrays and the concept of structured datastorage in Python programming."""

#=============================================================================================================
# Algorithm:
# 1. Start
# 2. Import NumPy as np
# 3. Create matrix A as a 4 x 4 Python list
# 4. Create matrix B as a 4 x 4 Python list
# 5. Add matrices A and B using np.add()
# 6. Store the result in numpy_sum
# 7. Display the sum of the matrices
# 8. Stop
#=============================================================================================================

#=============================================================================================================
# Pseudo Code:
# START
#
# IMPORT NumPy as np
#
# CREATE matrix A as a 4 x 4 Python list
# CREATE matrix B as a 4 x 4 Python list
#
# numpy_sum <- np.add(A, B)
# DISPLAY "Sum of matrices using NumPy:"
# DISPLAY numpy_sum
#
# STOP
#=============================================================================================================

import numpy as np

# Create two matrices using Numpy arrays
A = [
	[12, -7, 25, 4],
	[-18, 31, 6, -22],
	[9, 14, -27, 38],
	[45, -16, 3, 11],
]
print("Matrix A:")
print(np.array(A))
B = [
	[-5, 19, 8, -13],
	[27, -4, -15, 20],
	[16, -21, 34, -6],
	[-29, 7, 18, 24],
]
print("Matrix B:")
print(np.array(B))

# Addition of two matrices using NumPy
numpy_sum = np.add(A, B)
print("Sum of matrices using NumPy:")
print(numpy_sum)