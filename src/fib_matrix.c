// This is not the best solution for large N
#include <stdio.h>

// Function to multiply two matrices
void multiplyMatrix(long long a[2][2], long long b[2][2]) {
    long long x = a[0][0] * b[0][0] + a[0][1] * b[1][0];
    long long y = a[0][0] * b[0][1] + a[0][1] * b[1][1];
    long long z = a[1][0] * b[0][0] + a[1][1] * b[1][0];
    long long w = a[1][0] * b[0][1] + a[1][1] * b[1][1];

    a[0][0] = x;
    a[0][1] = y;
    a[1][0] = z;
    a[1][1] = w;
}

// Function to calculate the power of a matrix
void powerMatrix(long long matrix[2][2], int n) {
    if (n <= 1) {
        return;
    }

    long long temp[2][2] = {{1, 1}, {1, 0}};
    powerMatrix(matrix, n / 2);
    multiplyMatrix(matrix, matrix);

    if (n % 2 != 0) {
        multiplyMatrix(matrix, temp);
    }
}

// Function to calculate nth Fibonacci number using matrix exponentiation
long long fibonacciMatrix(int n) {
    if (n <= 0) {
        return 0;
    }

    long long matrix[2][2] = {{1, 1}, {1, 0}};
    powerMatrix(matrix, n - 1);

    return matrix[0][0];
}

int main() {
    int n;
    if (scanf("%d", &n) != 1) {
        printf("Error reading input.\n");
        return 1;
    }

    long long result = fibonacciMatrix(n);
    printf("%lld\n", result);

    return 0;
}
