
def main():
    m, n = map(int, input().split())
    tn = fib_mod(n+2)
    if tn > 0:
        tn_ = tn - 1
    else:
        tn_ = 9
    tm = fib_mod(m+1)
    if tm>0:
        tm_ = tm - 1
    else:
        tm_ = 9

    if tn_ < tm_ :
        print(tn_ + 10 - tm_)
    else:
        print(tn_ - tm_)

    


def matrix_multiply(a, b, c=10):
    # Matrix multiplication modulo m
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
                result[i][j] %= c
    return result

def matrix_power(matrix, power, c=10):
    # Compute matrix raised to power modulo m
    result = [[1, 0], [0, 1]]  # Identity matrix
    while power > 0:
        if power % 2 == 1:
            result = matrix_multiply(result, matrix, c)
        matrix = matrix_multiply(matrix, matrix, c)
        power //= 2
    return result

def fib_mod(n, c=10):
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Fibonacci matrix
    fib_matrix = [[1, 1], [1, 0]]
    # Calculate fib_matrix raised to power n modulo m
    result = matrix_power(fib_matrix, n - 1, c)
    return result[0][0]



if __name__ == '__main__':
    main()
