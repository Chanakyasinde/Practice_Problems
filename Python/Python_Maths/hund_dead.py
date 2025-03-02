def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1  
            if i != n // i:
                count += 1  
    return count

def main():
    n = int(input().strip())
    divisor_count = count_divisors(n)
    result = (divisor_count * (divisor_count - 1)) // 2
    print(result)

main()
