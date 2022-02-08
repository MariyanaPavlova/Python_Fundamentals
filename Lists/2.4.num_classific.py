nums = input().split(', ')

pos = [nums[i] for i in range(len(nums)) if int(nums[i]) >= 0]
neg = [nums[i] for i in range(len(nums)) if int(nums[i]) < 0]
even = [nums[i] for i in range(len(nums)) if int(nums[i]) %2 == 0]
odd = [nums[i] for i in range(len(nums)) if int(nums[i]) %2 != 0]

print(f'Positive: {(", ".join(pos))}')
print(f'Negative: {(", ".join(neg))}')
print(f'Even: {(", ".join(even))}')
print(f'Odd: {(", ".join(odd))}')

# for i in range(len(nums)):
#     if int(nums[i]) > 0:
#         pos.append(nums[i])
#print(pos)
