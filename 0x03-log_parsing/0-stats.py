#!/usr/bin/python3
"""Write a script that reads stdin line by line
and prints stats to stdout
"""


#!/usr/bin/python3

import sys

# Define the valid status codes
valid_status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}

# Initialize variables to store statistics
total_size = 0
status_code_counts = {code: 0 for code in valid_status_codes}
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()

        if len(parts) >= 7:
            status_code = parts[-2]
            file_size = parts[-1]

            if status_code in valid_status_codes:
                status_code_counts[status_code] += 1

            try:
                file_size = int(file_size)
                total_size += file_size
            except ValueError:
                # Ignore lines with non-integer file size
                continue

            line_count += 1

            if line_count == 10:
                print(f"File size: {total_size}")
                for code, count in sorted(status_code_counts.items()):
                    if count > 0:
                        print(f"{code}: {count}")
                line_count = 0

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print(f"File size: {total_size}")
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{code}: {count}")

print(f"File size: {total_size}")
for code, count in sorted(status_code_counts.items()):
    if count > 0:
        print(f"{code}: {count}")
