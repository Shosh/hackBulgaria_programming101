def sum_of_divisors(n):
    sum = 0
    divisor = 1
    while divisor <= n:
        if n % divisor == 0:
            sum += divisor
        divisor += 1
    return sum


def main():
    print(sum_of_divisors(8))
    sum_of_divisors(7)
    sum_of_divisors(1)
    sum_of_divisors(1000)

if __name__ == '__main__':
    main()
