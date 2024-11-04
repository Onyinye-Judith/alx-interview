#!/usr/bin/python3

ef valid_utf8(data: list[int]) -> bool:
        """
            Validate UTF-8 encoding.

             Arg: 
             data: List of integers representing bytes of data.

             Returns:
                     True if data is valid UTF-8 encoding, False otherwise.
                         """
                         bytes_left = 0

                             for byte in data:
                                         # Convert byte to binary and remove '0b' prefix
                                                 binary = bin(byte)[2:].zfill(8)

                                                         # Check for single-byte sequence (ASCII)
                                                                 if bytes_left == 0 and binary[0] == '0':
                                                                                 continue

                                                                                     # Check for start of multi-byte sequence
                                                                                             if bytes_left == 0:
                                                                                                             # Determine number of bytes in sequence
                                                                                                                         if binary.startswith('110'):
                                                                                                                                             bytes_left = 1
                                                                                                                                                         elif binary.startswith('1110'):
                                                                                                                                                                             bytes_left = 2
                                                                                                                                                                                         elif binary.startswith('11110'):
                                                                                                                                                                                                             bytes_left = 3
                                                                                                                                                                                                                         else:
                                                                                                                                                                                                                                             return False  # Invalid start byte

                                                                                                                                                                                                                                                 # Validate continuation bytes
                                                                                                                                                                                                                                                         else:
                                                                                                                                                                                                                                                                         if not binary.startswith('10'):
                                                                                                                                                                                                                                                                                             return False  # Invalid continuation byte
                                                                                                                                                                                                                                                                                                     bytes_left -= 1

                                                                                                                                                                                                                                                                                                         # Check if there are remaining bytes left to process
                                                                                                                                                                                                                                                                                                             return bytes_left == 0
