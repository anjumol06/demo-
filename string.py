def reverse_string(input_string):
    # Using slicing to reverse the string
    reversed_string = input_string[::-1]
    return reversed_string

# Example usage
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print("Original String:", input_string)
print("Reversed String:", reversed_string)
