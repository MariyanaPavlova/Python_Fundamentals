import math

n = int(input())

years = n * 100
days = math.floor(years * 365.2422)
hours = days * 24
min = hours * 60

print(f'{n} centuries = {years} years = {days} days = {hours} hours = {min} minutes')
