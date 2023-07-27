def multiply_matrix(matrix1, matrix2):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def power_matrix(matrix, n):
    result = [[1, 0], [0, 1]]  # Identity matrix
    while n > 0:
        if n % 2 == 1:
            result = multiply_matrix(result, matrix)
        matrix = multiply_matrix(matrix, matrix)
        n //= 2
    return result

def fibonacci(n):
    if n <= 0:
        return 0
    matrix = [[1, 1], [1, 0]]
    result_matrix = power_matrix(matrix, n - 1)
    return result_matrix[0][0]

if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))
