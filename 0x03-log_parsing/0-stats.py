#!/usr/bin/python3
"""Write a script that reads stdin line by line
and prints stats to stdout
"""


import sys

# Status codes dictionary
status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}

total_size = 0
count = 0  # Line counter

try:
    for line in sys.stdin:
        line = line.strip()  # Remove trailing newline character
        line_list = line.split(" ")

        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            # Check if the status code exists, then increment its count
            if status_code in status_codes_dict:
                status_codes_dict[status_code] += 1

            # Increment the total size
            total_size += file_size

            # Update the line counter
            count += 1

        if count == 10:
            count = 0  # Reset the counter
            print('File size: {}'.format(total_size))

            # Print out status code counts
            for key, value in sorted(status_codes_dict.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except KeyboardInterrupt:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
