def silnia(n):
    if n == 0:
        return 1
    elif n > 0:
        return n*silnia(n-1)
    else:
        return False

x = int(input("Podaj index do obliczenia silni:"))
print("Silnia(" ,x, ") =" silnia(x))
