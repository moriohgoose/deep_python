import sys
import os
from sys import stdin

def wc(files):
    total_lines = total_words = total_bytes = 0

    if not files:
        lines = sys.stdin.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_bytes = sum(len(line.encode()) for line in lines)
        print(f"{num_lines} {num_words} {num_bytes}")
    else:
        for file in files:
            num_lines = num_words = num_bytes = 0
            with open(file, 'r') as f:
                for line in f:
                    num_lines += 1
                    num_words += len(line.split())
                    num_bytes += len(line.encode())
                print(f"{num_lines} {num_words} {num_bytes} {file}")
                total_lines += num_lines
                total_words += num_words
                total_bytes += num_bytes

        if len(files) > 1:
            print(f"{total_lines} {total_words} {total_bytes} total")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        wc(sys.argv[1:])
    else:
        wc([])