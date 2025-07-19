# Strings Exercises

# 1. Create a variable and assign it the string "Just do it!"
quote = "Just do it!"

# 2. Access the "!" from the variable by index and print() it
print(quote[-1])  # Accessing last character using negative index

# 3. Print the slice "do" from the variable
print(quote[5:7])  # Characters from index 5 up to (but not including) 7

# 4. Get and print the slice "it!" from the variable
print(quote[8:])  # Slice from index 8 to the end

# 5. Print the slice "Just" from the variable
print(quote[:4])  # Slice from beginning up to (but not including) index 4

# 6. Get the string slice "do it!" from the variable and concatenate it with "Don't "
slice_part = quote[5:]  # "do it!" from index 5 to end
result = "Don't " + slice_part  # Concatenating "Don't " with "do it!"
print(result)  # Output: "Don't do it!"
