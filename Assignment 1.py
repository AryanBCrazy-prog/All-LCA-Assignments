""" Assignment 1

Aim:
Write a python program to create a Dictionary, Tuple and List of students and perform the 
Following operations: Add, Delete, Update. 

Objectives:
To learn and implement List, Tuple and Dictionary data structures. """

# ==========================================
# ALGORITHM:
# 1. Create a list of students.
# 2. Create a tuple of students.
# 3. Create a dictionary of students.
# 4. Print the list, tuple and dictionary.
# 5. Add a new student to the dictionary and print the updated dictionary.
# 6. Update an existing student's name in the dictionary and print the updated dictionary.
# 7. Delete a student from the dictionary and print the updated dictionary.
# ==========================================

# ==========================================
# PSEUDOCODE:
# BEGIN
#     SET Student_List to a list of student names
#     SET Student_tuple to a tuple of student names
#     SET Student_Dict to a dictionary containing student IDs and names
#
#     DISPLAY Student_List, Student_tuple, and Student_Dict
#
#     ADD student ID 106 with name "Panchal" to Student_Dict
#     DISPLAY the updated Student_Dict
#
#     CHANGE the name for student ID 101 to "Shweta"
#     DISPLAY the updated Student_Dict
#
#     DELETE student ID 105 from Student_Dict
#     DISPLAY the updated Student_Dict
# END
# ==========================================

#This is a student list:-
Student_List = ["Nikhil" , "Prachi" , "Pratiksha" , "Kavya" , "Arjun"]
#This is a student tuple:-
Student_tuple = ("Rahul" , "Sachin" , "Rishab" , "Somya" , "Zaheer")
#This is a student dictionary:- 
Student_Dict = {
    101:"Nikhil" ,
    102:"Prachi",
    103:"Pratiksha",
    104:"Kavya",
    105:"Arjun" 
}

#printing the student list, tuple and dictionary:-
print(f"Student_list is : {Student_List}")
print(f"Student_tuple is : {Student_tuple}")
print(f"Student_Dict is : {Student_Dict}")

#Adding the data in Student_List:-
Student_Dict[106] = "Panchal"
print(f"After adding Data in Student_Dict Is :{Student_Dict}")

#Updating the data in Student_List:-
Student_Dict[101] = "Shweta"
print(f"After updating Data for 101 in Student_Dict is :{Student_Dict}")

#Deleting the data in Student_List:-
del Student_Dict[105]
print(f"After Deleting Data for 105 in Student_dict is :{Student_Dict}")
