def main():
    n = int(input())
    print(last_digit_sum_of_fibonacci_squares(n))

def fibonacci_last_digit(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b % 10, (a + b) % 10
    return b

def last_digit_sum_of_fibonacci_squares(n):
    remainder = n % 60
    sum_last_digit = sum(fibonacci_last_digit(i) ** 2 % 10 for i in range(remainder + 1))
    return sum_last_digit % 10

if __name__=='__main__':
    main()