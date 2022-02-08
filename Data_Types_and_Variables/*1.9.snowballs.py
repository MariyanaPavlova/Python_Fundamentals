n = int(input())
max=0

for i in range(n):

    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_snow/snowball_time)**snowball_quality
    if snowball_value >= max:
        max = int(snowball_value)
        a = snowball_snow
        b = snowball_time
        c = snowball_quality

print(f'{a} : {b} = {max} ({c})')