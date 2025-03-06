# PasswordMaker
Creates passwords based off of User entered Name


The structure of the password from the left-most character is as follows:
1. Same character as First character of Name
2. Integer taken from len() of Name
3. Add 6 randomly generated characters, integers, and special-characters

This creates a unique 8-character password everytime a Name is inputted.
The user names and passwords are then saved to a .csv file. 
Data is extrapolated from the csv file and returned to Standard Output.

Free feel to modify this file.
