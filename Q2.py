def fib(prev, atual, num):
    if atual == num:
        return True
    if atual > num:
        return False
    prox = prev + atual
    prev = atual
    if prox == 0:
        prox = 1
    return fib(prev, prox, num)

num = int(input("Insira o número a testar: "))
print(fib(0, 0, num))
