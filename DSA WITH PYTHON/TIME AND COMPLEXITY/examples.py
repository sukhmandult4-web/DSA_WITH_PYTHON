"""
=========================================
TIME COMPLEXITY EXAMPLES
=========================================
"""

# O(1) - Constant Time
# Accessing the first element of a list.

numbers = [10, 20, 30, 40, 50]
print(numbers[0])


# ---------------------------------------

# O(n) - Linear Time
# Printing every element in a list.

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)


# ---------------------------------------

# O(n²) - Quadratic Time
# Nested loops.

n = 5

for i in range(n):
    for j in range(n):
        print(i, j)


# ---------------------------------------

# O(log n) - Logarithmic Time
# Binary Search (concept only).

arr = [2, 4, 6, 8, 10, 12, 14]
target = 10

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Found")
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1


"""
=========================================
SPACE COMPLEXITY EXAMPLES
=========================================
"""

# O(1) Auxiliary Space
# Only one extra variable is used.

x = 5
y = 10
z = 15

total = x + y + z

print(total)


# ---------------------------------------

# O(n) Auxiliary Space
# Creating another list of the same size.

numbers = [1, 2, 3, 4, 5]
double = []

for num in numbers:
    double.append(num * 2)

print(double)


# ---------------------------------------

# Input Space vs Auxiliary Space

marks = [90, 80, 95]

average = sum(marks) / len(marks)

print(average)

# Input Space  -> marks
# Auxiliary Space -> average