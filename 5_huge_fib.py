
def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


def matrix_multiply(a, b, m):
    # Matrix multiplication modulo m
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
                result[i][j] %= m
    return result

def matrix_power(matrix, power, m):
    # Compute matrix raised to power modulo m
    result = [[1, 0], [0, 1]]  # Identity matrix
    while power > 0:
        if power % 2 == 1:
            result = matrix_multiply(result, matrix, m)
        matrix = matrix_multiply(matrix, matrix, m)
        power //= 2
    return result

def fib_mod(n, m):
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Fibonacci matrix
    fib_matrix = [[1, 1], [1, 0]]
    # Calculate fib_matrix raised to power n modulo m
    result = matrix_power(fib_matrix, n - 1, m)
    return result[0][0]



if __name__ == '__main__':
    main()
