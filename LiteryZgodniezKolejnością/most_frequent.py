#Utworzenie słownika liter z częstotliwością ich występowania
def most_frequent(a):
    dict={}
    for i in a:
        if i!=" ":
            i=i.lower()
            dict[i]=dict.get(i,0)+1
    return dict

#
def rozwiazanie(dict):
    lista = []
    for k, v in dict.items():
        lista.append((v, k))
    lista.sort(reverse=True)
    for k,v in lista:
        print(v)

dict=most_frequent("a lllllll kk a yyyyyyyyy")
rozwiazanie(dict)



