#!/usr/bin/env python3
''' Log Parsing
'''
import sys

# Initialize metrics
total_file_size = 0
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

# Function to print statistics
def print_stats():
    ''' print_stats
    '''
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

try:
    line_count = 0

    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Validate format and parse
        if len(parts) < 7:
            continue

        try:
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            # Update metrics
            total_file_size += file_size
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1
        except ValueError:
            continue

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print statistics on keyboard interrupt
    print_stats()
    raise

# Print final statistics
print_stats()
