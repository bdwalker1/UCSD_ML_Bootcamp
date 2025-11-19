# teststring = ""
# while (teststring == "") or (len(teststring) < 6):
#     teststring = input("Please enter a test string: ")
#
#     if len(teststring) < 6:
#         print("Your string is too short.")
#         print("Please enter a string of at least 6 characters.")

# try:
#     testint = int(input("Please enter a positive integer: "))
#     if testint % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# except ValueError:
#     print("Please try again with a positive integer.")

print("Please enter side lengths for a triangle.")
a = int(input("Side a: "))
b = int(input("Side b: "))
c = int(input("Side c: "))

tritype = ""

if a != b and b != c and c != a:
    tritype = "scalene"
elif a == b and b == c:
    tritype = "equilateral"
else:
    tritype = "isosceles"

print(f"A triangle with these side lengths is: {tritype}")

