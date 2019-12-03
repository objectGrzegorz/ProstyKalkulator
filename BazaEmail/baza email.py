import pickle
import sys

def menu():
    print("1 - Odszukaj adres email")
    print("2 - Dodaj nowe imię i adres email")
    print("3 - Zmień istniejący adres email")
    print("4 - Usuń email")
    print("5 - Pokaż wszystkie wpisy")
    print("6 - Zakończ działanie programu")
    print()

    try:
        plik=open("bazaemail.dat","rb")
        slownik = pickle.load(plik)
    except:
        plik = open("bazaemail.dat", "wb")
        slownik={}
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
    if wybor == "5":
        wszystkie(slownik)
    if wybor =="6":
        wyjdz()


def zmien(slownik):
    odp = "T"
    while odp.upper() == "T":
        dozmiany=input("Podaj imię osoby, której email chcesz zmienić: "+"\n")
        if dozmiany in slownik:
            nowawartosc=input("Podaj nowy adres email: "+"\n")
            slownik[dozmiany]=nowawartosc
            print(("Dane zmienione."+"\n"))
        else:
            print("Nie znalazłem takiej osoby"+"\n")
        odp = input("Czy chcesz zmienić dane kolejnej osoby? Wpisz \"T\"(Enter) by kontynuować lub \"Enter\" aby przejść do menu."+"\n")
    plik = open("bazaemail.dat", "wb")
    pickle.dump(slownik,plik)
    plik.close()
    menu()

def usun(slownik):
    odp = "T"
    while odp.upper() == "T":
        dousuniecia=input("Podaj imię do usunięcia: "+"\n")
        if dousuniecia in slownik:
            del slownik[dousuniecia]
            print(dousuniecia,"został usunięty"+"\n")
        else:
            print("Nie znaleziono!"+"\n")
        odp = input("Czy chcesz usunąć kolejną osobę?  Wpisz \"T\"(Enter) by kontynuować lub \"Enter\" aby przejść do menu."+"\n")
    plik = open("bazaemail.dat", "wb")
    pickle.dump(slownik, plik)
    plik.close()
    menu()

def znajdz(slownik):
    odp="T"
    while odp.upper() == "T":
        szukaj=input("Wpisz imię, którego szukasz: "+"\n")
        if szukaj in slownik:
            print(szukaj,"ma maila:",slownik[szukaj]+"\n")
        else:
            print("Nie znalazłem takiej osoby."+"\n")
        odp = input("Jeśli chcesz szukać następnej osoby wpisz \"T\"(Enter) by kontynuować lub \"Enter\" aby przejść do menu. "+"\n")
    menu()
    
def wyjdz():
    sys.exit()

def dodaj(slownik):
    odp="T"
    while odp.upper() == "T":
        imie=input("Podaj imię nowej osoby: "+"\n")
        if imie in slownik:
            print("Przykro mi, ale ta osoba już istnieje."+"\n")
        else:
            email=input("Podaj email: "+"\n")
            slownik[imie]=email
            print("Email został pozytywnie dodany."+"\n")
            print("Jeśli chcesz dodać następny email wpisz \"T\"(Enter) by kontynuować lub \"Enter\" aby przejść do menu. "+"\n")
            odp = input()
    plik = open("bazaemail.dat", "wb")
    pickle.dump(slownik, plik)
    plik.close()
    menu()

def wszystkie(slownik):
    k=slownik.items()
    if slownik=={}:
        print("Baza danych jest pusta!"+"\n\n")
    else:
        for a,b in k:
            print(a,b)
        print("\n")
    menu()
menu()
