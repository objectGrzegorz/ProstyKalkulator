def slownik():
    with open("words.txt", "r") as plik:
        dict = {}
        slowo = plik.readline().strip()
        while slowo != "":
            k = tuple(sorted(slowo))
            lista = [slowo]
            if k not in dict:
                dict[k] = lista
            else:
                dict[k] += lista
            slowo = plik.readline().strip()
        return dict

def lista_anagramow(dict):
    for k,v in dict.items():
        print(v)

dict=slownik()
def od_najdluzszej(dict):
    slownik2={}
    for k,v in dict.items():
        slownik2[tuple(v)] = len(v)
    lista=[]
    for k,v in slownik2.items():
        lista.append((v,k))
    lista.sort(reverse=True)
    for k,v in lista:
        print(v)

od_najdluzszej(dict)