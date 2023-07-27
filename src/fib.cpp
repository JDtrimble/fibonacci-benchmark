#include <iostream>
#include <vector>

using namespace std;

// Function to multiply two matrices
vector<vector<long long>> multiplyMatrix(const vector<vector<long long>>& A, const vector<vector<long long>>& B) {
    int n = A.size();
    int m = B[0].size();
    int p = A[0].size();

    vector<vector<long long>> result(n, vector<long long>(m, 0));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            for (int k = 0; k < p; ++k) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    return result;
}

// Function to calculate matrix exponentiation
vector<vector<long long>> matrixExponentiation(const vector<vector<long long>>& A, int n) {
    int size = A.size();

    if (n == 1) {
        return A;
    }

    vector<vector<long long>> half_pow = matrixExponentiation(A, n / 2);
    vector<vector<long long>> result = multiplyMatrix(half_pow, half_pow);

    if (n % 2 == 0) {
        return result;
    } else {
        return multiplyMatrix(result, A);
    }
}

// Function to calculate nth Fibonacci number using matrix exponentiation
long long nthFibonacci(int n) {
    if (n <= 0) {
        return 0;
    }

    vector<vector<long long>> base = {{1, 1}, {1, 0}};
    vector<vector<long long>> result = matrixExponentiation(base, n - 1);

    return result[0][0];
}

int main() {
    int n;
    cin >> n;

    long long result = nthFibonacci(n);
    cout << result << endl;

    return 0;
}
