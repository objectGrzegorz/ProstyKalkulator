plik=open("pbnumbersWlasne.txt","r")
lista=[] #Lista liczb powerball

for linia in plik:
  linia = linia.rstrip("\n")  #Funkcja tworzenia listy liczb powerball
  lista2=linia.split()
  del(lista2[:-1])  #Usuwanie wszystkich liczb oprócz ostatniej (powerball) z każdej linii pliku
  lista+=lista2

plik.close()

lista3=[] #Lista pojedynczych liczb
lista4=[] #Lista indeksów liczb z listy3
for i in lista:
  if i not in lista3:
    lista3.append(i)
    lista4.append(1)

  else:
    indeks = lista3.index(i)
    lista4[indeks] += 1

kopia=[]
for i in lista3:
  kopia.append(i) #Tworzenie kopii listy 3
lista3.sort() #Posortowanie listy 3 celem wyświetlenia wyników w kolejności rosnącej
lista5=[] #Lista zliczonych powtórzeń dla posortowanej listy 3

for i in lista3:
  nowyin=kopia.index(i) #Funkcja "sortująca" wystąpienia zgodnie z posortowaną listą 3
  lista5.append(lista4[nowyin])

for i in lista3:
  print("liczba {} wystąpiła {} razy".format(i,lista5[lista3.index(i)]))

