n = int(input())
temperatures = []
for _ in range(n):
    temperature = float(input())
    temperatures.append(temperature)
temperature_range = max(temperatures) - min(temperatures)
print(f"{temperature_range:.1f}")
