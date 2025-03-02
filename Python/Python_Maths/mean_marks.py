n = int(input())
total_marks = 0
for _ in range(n):
    mark = int(input())
    total_marks += mark

average = total_marks / n
print(f"{average:.1f}")
