"""Python Program to Check Whether a String is Palindrome or Not"""
# Program to check if a string is palindrome or not
# 1) Find reverse of string
# 2) Check if reverse and original are same or not
# Driver code
s = "malayalam"
if s == s[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
