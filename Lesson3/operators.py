# Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators:")
print("a + b =", a + b)   # Addition
print("a - b =", a - b)   # Subtraction
print("a * b =", a * b)   # Multiplication
print("a / b =", a / b)   # Division (float)
print("a // b =", a // b) # Floor Division
print("a % b =", a % b)   # Modulus
print("a ** b =", a ** b) # Exponentiation

# Assignment Operators
x = 5
print("\nAssignment Operators:")
x += 2  # x = x + 2
print("x += 2:", x)
x -= 1  # x = x - 1
print("x -= 1:", x)
x *= 3  # x = x * 3
print("x *= 3:", x)
x /= 2  # x = x / 2
print("x /= 2:", x)
x //= 2 # x = x // 2
print("x //= 2:", x)
x %= 2  # x = x % 2
print("x %= 2:", x)
x **= 3 # x = x ** 3
print("x **= 3:", x)

# Comparison Operators
print("\nComparison Operators:")
print("a == b:", a == b)   # Equal to
print("a != b:", a != b)   # Not equal to
print("a > b:", a > b)     # Greater than
print("a < b:", a < b)     # Less than
print("a >= b:", a >= b)   # Greater than or equal to
print("a <= b:", a <= b)   # Less than or equal to

# Logical Operators
print("\nLogical Operators:")
print("a > 5 and b < 5:", a > 5 and b < 5) # Logical AND
print("a > 5 or b > 5:", a > 5 or b > 5)   # Logical OR
print("not(a > 5):", not(a > 5))           # Logical NOT

# Bitwise Operators
print("\nBitwise Operators:")
print("a & b:", a & b)   # Bitwise AND
print("a | b:", a | b)   # Bitwise OR
print("a ^ b:", a ^ b)   # Bitwise XOR
print("~a:", ~a)         # Bitwise NOT
print("a << 2:", a << 2) # Bitwise left shift
print("a >> 2:", a >> 2) # Bitwise right shift

# Membership Operators
list1 = [1, 2, 3, 4]
print("\nMembership Operators:")
print("2 in list1:", 2 in list1)     # in
print("5 not in list1:", 5 not in list1) # not in

# Identity Operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print("\nIdentity Operators:")
print("x is z:", x is z)         # True, same object
print("x is y:", x is y)         # False, different objects with same content
print("x is not y:", x is not y) # True

# End of