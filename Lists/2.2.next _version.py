version = input().split('.')
version_str = ''.join(version)

version_int = int(version_str)
new_ver = version_int + 1

new_ver_str = str(new_ver)
new_ver_str_ = '.'.join(new_ver_str)
print(new_ver_str_)
