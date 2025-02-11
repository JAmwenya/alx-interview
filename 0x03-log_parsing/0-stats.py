#!/usr/bin/env python3
"""
Log parsing script that reads stdin line by line and computes metrics.
"""

import sys


def print_stats(file_size: int, status_codes: dict):
    """
    Prints the accumulated metrics.

    Args:
        file_size (int): Total file size accumulated.
        status_codes (dict): Dictionary containing status codes and their counts.
    """
    print(f"File size: {file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def parse_logs():
    """
    Reads stdin line by line, parses log entries, and computes metrics.
    """
    total_file_size = 0
    status_code_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0,
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            try:
                parts = line.split()
                file_size = int(parts[-1])
                status_code = int(parts[-2])

                total_file_size += file_size

                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
            except (IndexError, ValueError):
                # Skip lines with incorrect format
                continue

            if line_count % 10 == 0:
                print_stats(total_file_size, status_code_counts)

    except KeyboardInterrupt:
        print_stats(total_file_size, status_code_counts)
        raise

    print_stats(total_file_size, status_code_counts)


if __name__ == "__main__":
    parse_logs()
