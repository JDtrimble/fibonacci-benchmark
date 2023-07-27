#include <stdio.h>
#include <stdlib.h>

// Function to calculate nth Fibonacci number using memoization
long long fibonacci(int n, long long* memo) {
    if (n <= 1) {
        return n;
    }

    if (memo[n] != -1) {
        return memo[n];
    }

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
    return memo[n];
}

// Function to calculate nth Fibonacci number
long long nthFibonacci(int n) {
    long long* memo = (long long*)malloc((n + 1) * sizeof(long long));
    for (int i = 0; i <= n; ++i) {
        memo[i] = -1;
    }

    long long result = fibonacci(n, memo);

    free(memo);
    return result;
}

int main() {
    int n;
    scanf("%d", &n);

    long long result = nthFibonacci(n);
    printf("%lld\n", result);

    return 0;
}
