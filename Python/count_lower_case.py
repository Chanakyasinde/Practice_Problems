s = input()
lowercase_count = 0
for char in s:
    if char.islower():
        lowercase_count += 1
print(lowercase_count)
