def most_frequent(a):
    dict={}
    for i in a:
        if i!=" ":
            i=i.lower()
            dict[i]=dict.get(i,0)+1
    return dict


def rozwiazanie(dict):
    lista = []
    for k, v in dict.items():
        lista.append((v, k))
    odpowiedz = []
    for v, k in lista:
        odpowiedz.append(k)
    print(odpowiedz)

dict=most_frequent("Chrzaszcz brzmi w trzcinie")
rozwiazanie(dict)



