# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

numbers = read_numbers()

if len(numbers) == 0:
    sys.exit("Error: no numbers provided")

numbers.sort()
n = len(numbers)
mid = n // 2

if n % 2 == 1:
    median = numbers[mid]
else:
    median = (numbers[mid - 1] + numbers[mid]) / 2

print("Minimum =", min(numbers))
print("Maximum =", max(numbers))
print("Mean    =", sum(numbers) / n)
print("Median  =", median)