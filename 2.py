def fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
        if a == n:
            return True  # número pertence à sequência
    return False  # número não pertence à sequência

num = int(input("Informe um número: "))

if fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
