def multiply_numbers(num1, num2):
    """
    This function takes two numbers as input and returns their product.
    """
    result = num1 * num2
    return result
my_product = multiply_numbers (-2,-6)
print(my_product)
def add_numbers(num1, num2):
    """
    This function takes two numbers as input and returns their sum.
    """
    result = num1 + num2
    return result
My_sum = add_numbers(5,7)
print(My_sum)

def perform_operations(num1, num2):
    """
    This function performs multiplication and addition using the results
    of the multiply_numbers and add_numbers functions.
    """
# Call the multiply_numbers function
    product = multiply_numbers(num1, num2)
    print(product)

    # Call the add_numbers function
    sum= add_numbers(num1, num2)
    print(sum)
    

    # Display the results
    print(f"Multiplication Result: {product}")
    print(f"Addition Result: {sum}")


# Test Case 1: Positive numbers
perform_operations(3, 4)

# Test Case 2: Negative numbers
perform_operations(-2, 6)

# Test Case 3: Zero and positive number
perform_operations(0, 9)

# Test Case 4: Zero and negative number
perform_operations(0, -5)
