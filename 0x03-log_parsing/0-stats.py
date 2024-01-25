#!/usr/bin/python3
import sys

def print_stats(total_size, status_counts):
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts):
        print("{}: {}".format(status_code, status_counts[status_code]))

def parse_line(line):
    parts = line.split()
    if len(parts) != 10 or parts[8] != "\"GET" or parts[9] != "/projects/260" or not parts[7].isdigit():
        return None
    return int(parts[7]), int(parts[9])

def main():
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            parsed = parse_line(line.strip())
            if parsed:
                file_size, status_code = parsed
                total_size += file_size
                status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if i % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        pass  # Handle keyboard interruption

    print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
