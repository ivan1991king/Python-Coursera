n = int(input())
a = int(n % 10)
print(a)
b = int((n // 10 ) % 10)
print(b)
c = int((n // 10 ) // 10)
print(c)
print(a+b+c)