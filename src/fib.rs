use std::io;

// Function to calculate nth Fibonacci number using memoization
fn fibonacci(n: u128, memo: &mut Vec<Option<u128>>) -> u128 {
    if n <= 1 {
        return n;
    }

    if let Some(value) = memo[n as usize] {
        return value;
    }

    memo[n as usize] = Some(fibonacci(n - 1, memo) + fibonacci(n - 2, memo));
    memo[n as usize].unwrap()
}

// Function to calculate nth Fibonacci number
fn nth_fibonacci(n: u128) -> u128 {
    let mut memo = vec![None; (n + 1) as usize];
    fibonacci(n, &mut memo)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read input");
    let n: u128 = input.trim().parse().expect("Invalid input");

    let result = nth_fibonacci(n);
    println!("{}", result);
}
