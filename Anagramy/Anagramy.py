with open("words.txt","r") as plik:
    dict={}
    slowo=plik.readline().strip()
    while slowo !="":
        k=tuple(sorted(slowo))
        lista = [slowo]
        if k not in dict:
            dict[k]=lista
        else:
            dict[k]+=lista
        slowo = plik.readline().strip()
    for k,v in dict.items():
        print(v)