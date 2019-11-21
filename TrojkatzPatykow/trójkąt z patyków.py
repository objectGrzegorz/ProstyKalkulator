def is_triangle(a,b,c):
    if a>b+c or b>a+c or c>a+b:
        print("Nie da się uformować trójkąta z podanych liczb")
    else:
        print("Jest możliwe uformowanie trójkąta z podanych liczb")
def pobierz_liczby():
    a=int(input("Podaj liczbę a: "))
    b = int(input("Podaj liczbę b: "))
    c = int(input("Podaj liczbę c: "))
    is_triangle(a,b,c,)

pobierz_liczby()

