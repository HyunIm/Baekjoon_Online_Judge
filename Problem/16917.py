A, B, C, X, Y = map(int, input().split())
price = 0

if A+B > 2*C:
    half = min(X, Y)
    price += half*C*2
    X -= half
    Y -= half

price += A*X if A < 2*C else X*C*2
price += B*Y if B < 2*C else Y*C*2

print(price)
