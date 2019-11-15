plik=open("pbnumbersWlasne.txt","r")
lista=[]  #Lista wszystkich liczb z pliku

for linia in plik:
  linia = linia.rstrip("\n")  #Funkcja dodawania liczb z plku do listy
  lista2=linia.split()
  lista+=lista2

plik.close()

lista3=[] #Lista pojedynczych liczb
lista4=[] #Lista, na której zliczane są powtórzenia liczb z listy3 wg indeksów
for i in lista:
  if i not in lista3:
    lista3.append(i)
    lista4.append(1)  #Funkcja tworząca listy 3 i 4
  else:
    indeks = lista3.index(i)
    lista4[indeks] += 1

for i in range(10):
  mini=min(lista4)
  indeks=lista4.index(mini)
  liczba=lista3[indeks]
  print("Liczba",liczba,"wystąpiła",mini,"razy")
  del(lista3[indeks])
  del(lista4[indeks])

