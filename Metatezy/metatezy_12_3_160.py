plik1=open("words.txt","r")
lista1=[]
slowo=plik1.readline()
while slowo!="":
    lista1.append(slowo.strip("\n"))
    slowo = plik1.readline()
plik1.close()

plik2=open("words.txt","r")
lista2=[]
slowo=plik2.readline()
while slowo!="":
    lista2.append(slowo.strip("\n"))
    slowo = plik2.readline()
plik1.close()

for slowo1 in lista1:
    for slowo2 in lista2:
        if len(slowo1)==len(slowo2):
            count=0
            for a,b in zip(slowo1,slowo2):
                if a!=b:
                    count+=1
            if count==2:
                print(slowo1,slowo2)