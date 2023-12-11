def columnar_transposition(text, column_order):
    # Base case: If the column order is empty, return an empty string
    if not column_order:
        return ""

    # Determine the current column to read
    current_column = int(column_order[0])

    # Initialize a list to store characters for the current column
    current_column_chars = []

    # Iterate through the text and add characters to the current column
    for i, char in enumerate(text):
        if i % len(column_order) == current_column - 1:
            current_column_chars.append(char)

    # Remove the first digit from the column order
    remaining_order = column_order[1:]

    # Recursively process the remaining columns
    encoded_text = columnar_transposition(text, remaining_order)

    # Combine the characters for the current column with the previously encoded text
    return "".join(current_column_chars) + encoded_text

# Get input from the user
input_text = input("Enter the text to be encoded: ")
column_order = input("Enter the column order: ")

# Remove any spaces from the column order
column_order = column_order.replace(" ", "")

# Call the function and print the encoded text
encoded_text = columnar_transposition(input_text, column_order)
print(encoded_text)
