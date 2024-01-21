def uppercase_string(input_str):
    """
       Convert the input string to uppercase.

       This function takes a string as input and returns a new string
       with all characters converted to uppercase.
       """
    return input_str.upper()


def capitalize_words(input_str):
    """
    Capitalize the first letter of each word in the input string.
    """
    return ' '.join(word.capitalize() for word in input_str.split())