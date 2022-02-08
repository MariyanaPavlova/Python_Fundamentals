nums = [int(el) for el in input().split(', ')]
#nums = list(map(lambda x: int(x), input().split(", ")))
#nums = list(map(int, input().split(', ')))

group = 10
max_num = max(nums)

while nums:
    nums_group = []

    for i in nums:
        if i in range(group-10, group+1):
            nums_group.append(i)

    for i in nums_group:
        nums.remove(i)

    print(f"Group of {group}'s: {nums_group}")
    group += 10


