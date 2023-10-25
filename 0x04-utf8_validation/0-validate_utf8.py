#!/usr/bin/python3
"""
This function determines if a given data set represents a valid UTF-8 encoding.
A character in UTF-8 can be 1 to 4 bytes long.
The data set can contain multiple characters.
The data will be represented by a list of integers.
Each integer represents 1 byte of data, therefore you only
need to handle the 8 least significant bits of each integer.
"""


def validUTF8(data):

    """
    Prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else return False
    """
    remaining_bytes = 0

    # Iterate through the list of integers
    for byte in data:
        # Check if the byte is within the valid range (0 to 255)
        if byte < 0 or byte > 255:
            return False

        # If we are not in the middle of processing a multi-byte character
        if remaining_bytes == 0:
            # Determine the number of leading ones in the byte
            if (byte >> 7) == 0b0:
                remaining_bytes = 0  # 1-byte character
            elif (byte >> 5) == 0b110:
                remaining_bytes = 1  # 2-byte character
            elif (byte >> 4) == 0b1110:
                remaining_bytes = 2  # 3-byte character
            elif (byte >> 3) == 0b11110:
                remaining_bytes = 3  # 4-byte character
            else:
                return False  # Invalid leading bits

        else:

            if (byte >> 6) != 0b10:
                return False

        remaining_bytes -= 1

    return remaining_bytes == 0
