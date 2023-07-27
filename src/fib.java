import java.math.BigInteger;
import java.util.Arrays;
import java.util.Scanner;

public class fib {
    // Function to calculate nth Fibonacci number using memoization
    public static BigInteger fibonacci(int n, BigInteger[] memo) {
        if (n <= 1) {
            return BigInteger.valueOf(n);
        }

        if (memo[n] != null) {
            return memo[n];
        }

        memo[n] = fibonacci(n - 1, memo).add(fibonacci(n - 2, memo));
        return memo[n];
    }

    // Function to initialize the memoization array and call the fibonacci function
    public static BigInteger nthFibonacci(int n) {
        BigInteger[] memo = new BigInteger[n + 1];
        Arrays.fill(memo, null);

        return fibonacci(n, memo);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        BigInteger result = nthFibonacci(n);
        System.out.println(result);

        scanner.close();
    }
}
