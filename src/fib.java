import java.util.Arrays;
import java.util.Scanner;

public class fib {
    // Function to calculate nth Fibonacci number using memoization
    public static long fibonacci(int n, long[] memo) {
        if (n <= 1) {
            return n;
        }

        if (memo[n] != -1) {
            return memo[n];
        }

        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
        return memo[n];
    }

    // Function to initialize the memoization array and call the fibonacci function
    public static long nthFibonacci(int n) {
        long[] memo = new long[n + 1];
        Arrays.fill(memo, -1);

        long result = fibonacci(n, memo);
        return result;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        long result = nthFibonacci(n);
        System.out.println(result);

        scanner.close();
    }
}
