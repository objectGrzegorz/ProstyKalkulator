def check_fermat(a,b,c,n):
    if n>2: #W tym warunku sprawdzamy czy Fermat miał rację
        if a**n+b**n==c**n:
            print("Do licha, Fermat się mylił!")
        else:
            print("Fermat miał rację!")
    else: #Jeśli "n" jest mniejsze od 2 to sprawdzamy czy równanie jest prawdziwe
        if a**n+b**n==c**n:
            print("W tym przypadku równanie jest prawdziwe")
        else:
            print("W tym przypadku równanie jest nieprawdziwe")


a=int(input("Podaj liczbę a: "))
b=int(input("Podaj liczbę b: "))
c=int(input("Podaj liczbę c: "))
n=int(input("Podaj liczbę n: "))
check_fermat(a,b,c,n)