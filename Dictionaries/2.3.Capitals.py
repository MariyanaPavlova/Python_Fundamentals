first_line = input().split(', ')
second_line = input().split(', ')

dict_zip = dict(zip(first_line, second_line))
{print(f'{key} -> {value}') for key, value in dict_zip.items()}
