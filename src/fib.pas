program Fibonacci;

const
  MAXN = 1000;

var
  memo: array[0..MAXN] of Int64;

function Fibonacci(n: Int64): Int64;
begin
  if n <= 1 then
    Exit(n);

  if memo[n] <> -1 then
    Exit(memo[n]);

  memo[n] := Fibonacci(n - 1) + Fibonacci(n - 2);
  Exit(memo[n]);
end;

function NthFibonacci(n: Int64): Int64;
begin
  if n < 0 then
    Exit(0);

  FillChar(memo, SizeOf(memo), $FF); // Initialize the memoization array with -1
  Exit(Fibonacci(n));
end;

var
  n: Int64;
begin
  ReadLn(n);

  WriteLn(NthFibonacci(n));
end.
