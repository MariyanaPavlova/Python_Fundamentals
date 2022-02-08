#["1", "2", "3"]
num_str = input().split(", ")

num_int = [int(i) for i in num_str]

num_map = list(map(lambda i: int(i), num_str))

num_map_r = list(map(int, num_str))

print(num_int)