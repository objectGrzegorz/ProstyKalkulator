def slownik():
    with open("words.txt", "r") as plik:
        dict2 = {}
        slowo = plik.readline().strip()
        while slowo != "":
            k = tuple(sorted(slowo))
            lista = [slowo]
            if k not in dict2:
                dict2[k] = lista
            else:
                dict2[k] += lista
            slowo = plik.readline().strip()
        dict={}
        for k,v in dict2.items():
            if len(v)>1:
                dict[k]=v
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

def bingo(dict):
    slownik2 = {}
    for k, v in dict.items():
        slownik2[tuple(v)] = len(v)
    lista = []
    for k, v in slownik2.items():
        lista.append((v, k))
    lista.sort(reverse=True)
    for k, v in lista:
        if len(v) == 8:
            print(v)
bingo(dict)