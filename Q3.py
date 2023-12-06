s = input("Please Enter the world to check: ")
if s == s[::-1]:
    print(f"The word {s} is palindrome.")
else:
    print(f"The word {s} is not palindrome, \n because {s[::-1]} is not equal to {s}")