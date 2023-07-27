use std::io;
use num::bigint::BigUint;
use num::traits::One;

// Function to calculate nth Fibonacci number using memoization
fn fibonacci(n: u128, memo: &mut Vec<Option<BigUint>>) -> BigUint {
    if n <= 1 {
        return BigUint::from(n);
    }

    if let Some(value) = &memo[n as usize] {
        return value.clone();
    }

    memo[n as usize] = Some(fibonacci(n - 1, memo) + fibonacci(n - 2, memo));
    memo[n as usize].as_ref().unwrap().clone()
}

// Function to calculate nth Fibonacci number
fn nth_fibonacci(n: u128) -> BigUint {
    let mut memo = vec![None; (n + 1) as usize];
    memo[0] = Some(BigUint::one());
    memo[1] = Some(BigUint::one());
    fibonacci(n, &mut memo)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read input");
    let n: u128 = input.trim().parse().expect("Invalid input");

    let result = nth_fibonacci(n);
    println!("{}", result);
}
