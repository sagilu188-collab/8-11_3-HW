def get_statistics(numbers):
  stats = {
        'sum': sum(numbers),
        'avg': sum(numbers) / len(numbers),
        'min': min(numbers),
        'max': max(numbers),
        'length': len(numbers)
    }
  return stats

nums = []
while True:
 number = int(input("Enter a number: "))
 if number <= 0:
     break
 nums.append(number)

print(nums)
result = get_statistics(nums)
print(result)