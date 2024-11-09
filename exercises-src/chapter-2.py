def call_operation(a, b, c):
  op1 = a * b + a + b
  res1 = op1 * c + op1 + c
  op2 = b * c + b + c
  res2 = a * op2 + a + op2
  return  res1 == res2

def solve(a, b, c):
  op1 = a * b + a + b
  res1 = op1 * c + op1 + c
  return res1

def inverse_abelian(x):
  y = (x * -1) / (x + 1)
  return round(x * y + x + y, 3)

def main():
  print(call_operation(1, 5, 10))
  print(inverse_abelian(-2))
  print(solve(3, 1, 1))

if __name__ == '__main__':
  main()