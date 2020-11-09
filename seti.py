def decimal_to_binary(decimal_number):
    """Returns the array of digits in binary representation of a decimal number"""
    # decimal_number = int(input("Give me a number: "))
    binary_number = []
    while decimal_number > 0:
        if decimal_number % 2 == 1:
            binary_number.insert(0, 1)
        else:
            binary_number.insert(0, 0)
        decimal_number = decimal_number // 2
    return binary_number



def binary_to_decimal(binary_digits):
    """Returns the decimal (number) representation of a binary number represented by an array of 0/1 digits"""
    binary_digits.reverse()
    decimal_number = 0
    for i in range(len(binary_digits)):
        decimal_number += 2 ** i * binary_digits[i]
    return decimal_number


def decimal_to_base(decimal_number, destination_base):
    """Returns the digits in destination_base representation of the decimal number"""
    destination_digits = []
    result = []
    possible_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(0, destination_base):
        destination_digits.append(possible_digits[i])
    while decimal_number > 0:
        remainder = decimal_number % destination_base
        remainder = destination_digits[remainder]
        result.insert(0, remainder)
        decimal_number = decimal_number // destination_base
    return result



def base_to_decimal(digits, original_base):
    """Returns the decimal (number) representation of an array of digits given in original_base"""
    possible_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    decimal_number = 0
    digits.reverse()
    for i in range(0, len(digits)):
        value = possible_digits.index(str(digits[i]))
        decimal_number += (original_base ** i) * value
    return decimal_number


def digits_as_string(digits, base):
    """Returns the string representation of an array of digits given in base"""
    result = ""
    letters = []
    possible_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for digit in digits:
        if digit > 9:
            digit = possible_digits[digit]
            letters.append(digit)
        elif digit <= 9:
            digit = str(digit)
            letters.append(digit)
    result = "".join(letters)
    return result


def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    decimal_number = base_to_decimal(original_digits, original_base)
    print(decimal_to_base(decimal_number, destination_base))


convert_base([1, 1, 2, 0], 3, 2)
