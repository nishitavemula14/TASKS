nums = ["10", "20", "abc", "30", "5"]

valid_nums = []

for num in nums:
  
  try:
    valid_nums.append(int(num))
  except ValueError:
    pass
  
filtered_nums = [num for num in valid_nums if num >10]

Squared_nums = [nums**2 for nums in filtered_nums]

total_sum = sum(Squared_nums)

print("valid numbers:", valid_nums)
print("filtered numbers:", filtered_nums)
print("squared numbers:", Squared_nums)         
print("Sum of the numbers:", total_sum)