def sum_of_digits(n):
    sum = 0
    while n:
        sum += n % 10
        n = n // 10
    print(sum)


def main():
    sum_of_digits(1325132435356)
    sum_of_digits(123456789)
    sum_of_digits(6)

if __name__ == '__main__':
    main()
