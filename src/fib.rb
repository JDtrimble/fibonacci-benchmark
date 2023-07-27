def fibonacci(n, memo)
    return n if n <= 1
  
    return memo[n] if memo[n]
  
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
  end
  
  def nth_fibonacci(n)
    memo = {}
    fibonacci(n, memo)
  end
  
  n = gets.chomp.to_i
  puts nth_fibonacci(n)
  