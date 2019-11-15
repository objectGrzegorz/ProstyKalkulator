import random
plik=open("pbnumbersWlasne.txt","w")
for i in range(654):
  for i in range(5):
    linia=format(random.randint(1,69),"02d")
    linia=str(linia)
    plik.write(linia+" ")
  linia = format(random.randint(1, 26), "02d")
  linia = str(linia)
  plik.write(linia + " ")
  plik.write("\n")
plik.close()