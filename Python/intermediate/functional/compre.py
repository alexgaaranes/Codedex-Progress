numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]

even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 != 0]

print("Original Numbers:", numbers)
print("Even Numbers:", even_nums)
print("Odd Numbers:", odd_nums)
