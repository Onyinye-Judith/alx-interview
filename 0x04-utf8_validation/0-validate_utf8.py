#!/usr/bin/python3
"""
This module contains a function that validates UTF-8 encoding.
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

                Parameters:
                    data (List[int]): A list of integers representing bytes of data.

                        Returns:
                            bool: True if data is a valid UTF-8 encoding, else False.
                                """
                                    # Number of continuation bytes needed
                                        num_bytes = 0

                                            # Masks for leading bits in different byte patterns
                                                byte1_mask = 0b10000000  # 128, to check leading 1 or 0
                                                    byte2_mask = 0b11000000  # 192, to check '10' in continuation bytes
                                                        byte3_mask = 0b11100000
                                                            byte4_mask = 0b11110000
                                                                byte5_mask = 0b11111000

                                                                    for byte in data:
                                                                                # Mask the byte to keep only the least significant 8 bits
                                                                                        byte = byte & 0xFF

                                                                                                if num_bytes == 0:
                                                                                                                # Determine the number of bytes in the UTF-8 character
                                                                                                                            if (byte & byte1_mask) == 0:
                                                                                                                                                continue  # 1-byte character
                                                                                                                                                        elif (byte & byte3_mask) == 0b11000000:
                                                                                                                                                                            num_bytes = 1  # 2-byte character
                                                                                                                                                                                        elif (byte & byte4_mask) == 0b11100000:
                                                                                                                                                                                                            num_bytes = 2  # 3-byte character
                                                                                                                                                                                                                        elif (byte & byte5_mask) == 0b11110000:
                                                                                                                                                                                                                                            num_bytes = 3  # 4-byte character
                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                            return False  # Invalid leading byte
                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                # Check if byte is a continuation byte (starts with '10')
                                                                                                                                                                                                                                                                                                            if (byte & byte2_mask) != 0b10000000:
                                                                                                                                                                                                                                                                                                                                return False
                                                                                                                                                                                                                                                                                                                                        num_bytes -= 1

                                                                                                                                                                                                                                                                                                                                            # All bytes should be accounted for
                                                                                                                                                                                                                                                                                                                                                return num_bytes == 0

