# Accept 4 numbers from console and find the second largest number using 
# if else only. Duplicate numbers are not allowed.

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number:"))
d=int(input("Enter fourth number: "))

#check for duplicate numbers
if a == b or a == c or a == d or b == c or b == d or c == d:
    print("Duplicate numbers are not allowed.")
    exit()

if a > b and a > c and a > d:
    largest =a
    # second_largest = max(b, c, d)
    if b>c and b>d:
        second_largest = b
    elif c > b and c > d:
        second_largest = c
    else:
        second_largest = d

elif b > a and b > c and b > d:
    # largest = b
    # second_largest = max(a, c, d)
    largest =b
    # second_largest = max(b, c, d)
    if a>c and a>d:
        second_largest = a
    elif c > a and c > d:
        second_largest = c
    else:
        second_largest = d

elif c > a and c > b and c > d:
    # largest = c
    # second_largest = max(a, b, d)
    largest =c
    # second_largest = max(b, c, d)
    if b>a and b>d:
        second_largest = b
    elif a > b and a > d:
        second_largest = a
    else:
        second_largest = d
else:
    # largest = d
    # second_largest = max(a, b, c)
    largest = d
    if a > b and a > c:
        second_largest = a
    elif b > a and b > c:
        second_largest = b
    else:
        second_largest = c

print("\nThe second largest number is:", second_largest)
print("The largest number is:", largest)


# The code above accepts four numbers from the user and determines the second largest number
# without allowing duplicates. It uses if-else statements to compare the numbers    
# and find the largest and second largest values. If any duplicates are found, it exits with a message.
# The final output displays the second largest and largest numbers.
# without using any loops or complex data structures.
# in the list.

# maximum  = max(a,b,c,d)
# print("The largest number is:", maximum)
