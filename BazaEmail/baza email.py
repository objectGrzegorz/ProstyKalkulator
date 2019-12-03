import pickle
import sys


def menu():
    print("1 - Odszukaj adres email")
    print("2 - dodaj nowe imię i adres email")
    print("3 - zmień istniejący adres email")
    print("4 - usuń email")
    print("5 - Zapisz efekt pracy i zakończ")
    print("6 - Pokaż wszystkie wpisy")
    print()


    plik=open("bazaemail.dat","rb")
    slownik=pickle.load(plik)
    plik.close()

    wybor=input()
    if wybor == "1":
        znajdz(slownik)
    if wybor == "2":
        dodaj(slownik)
    if wybor=="3":
        zmien(slownik)
    if wybor == "4":
        usun(slownik)
    if wybor =="5":
        zapisz(slownik)
    if wybor == "6":
        wszystkie(slownik)

def zmien(slownik):
    odp = "T"
    while odp.upper() == "T":
        dozmiany=input("Podaj imię osoby, której email chcesz zmienić")
        if dozmiany in slownik:
            nowawartosc=input("Podaj nowy adres email:")
            slownik[dozmiany]=nowawartosc
            print(("Dane zmienione"))
            odp=input("Czy chcesz zmienić dane kolejnej osoby? t/T")
            print()
        else:
            print("Nie znalazłem takiej osoby")
            odp = input("Czy chcesz zmienić dane kolejnej osoby? t/T")
            print()
    plik = open("bazaemail.dat", "wb")
    pickle.dump(slownik,plik)
    plik.close()
    menu()
    return slownik


def usun(slownik):
    odp = "T"
    while odp.upper() == "T":
        dousuniecia=input("Podaj imię do usunięcia:")
        if dousuniecia in slownik:
            del slownik[dousuniecia]
            print(dousuniecia,"został usunięty")
            odp = input("Czy chcesz usunąć kolejną osobę?")
            print()
        else:
            print("Nie znaleziono!")
            odp = input("Czy chcesz usunąć kolejną osobę?")
            print()
    plik = open("bazaemail.dat", "wb")
    pickle.dump(slownik, plik)
    plik.close()
    menu()
    return slownik

def znajdz(slownik):
    odp="T"
    while odp.upper() == "T":
        szukaj=input("Wpisz imię, którego szukasz"+"\n")

        if szukaj in slownik:
            print(szukaj,"ma maila:",slownik[szukaj])
            odp = input("Czy chcesz szukać kolejnej osoby t/T"+"\n")

        else:
            print("Nie znalazłem takiej osoby")
            odp = input("Czy chcesz szukać kolejnej osoby t/T"+"\n")

    menu()
    
def zapisz(slownik):
    plik = open("bazaemail.dat", "wb")
    pickle.dump(slownik,plik)
    plik.close()
    print("Baza email została zapisana")
    sys.exit()


def dodaj(slownik):
    odp="T"
    while odp.upper() == "T":
        imie=input("Podaj imię właściciela emaila"+"\n")
        if imie in slownik:
            print("Przykro mi, ale ta osoba już istnieje"+"\n")
        else:

            email=input("Podaj email"+"\n")
            slownik[imie]=email
            print("email pozytywnie dodany")
            print("Jeśli chcesz dodać email wpisz 't' lub 'T' "+"\n")
            odp = input()

    plik = open("bazaemail.dat", "wb")
    pickle.dump(slownik, plik)
    plik.close()
    menu()
    return slownik

def wszystkie(slownik):
    k=slownik.items()
    for a,b in k:
        print(a,b)
menu()
