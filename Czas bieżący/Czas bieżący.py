import time

sekundy=time.time() #Pobranie liczby sekund, które upłynęły od "epoki"

czas_lokalny=time.ctime(sekundy) #Wyświetlenie gotowego czasu lokalnego
print(czas_lokalny,"\n")

ob=time.localtime(sekundy) #samodzielne utworzenie godziny
print("{:02d}:{:02d}:{:02d}".format(ob.tm_hour,ob.tm_min,ob.tm_sec))
print("Od epoki minęło {:.0f} dni".format(sekundy//86400)+"\n")

#Poniższe obliczenia dają wynik z przesuniętą godziną

dni=sekundy//86400 #Tyle dni minęło od epoki
print("dni: ",dni)
pozostałe=sekundy%86400 #Tyle sekund pozostało po odjęciu dni
#print(pozostałe)

h=pozostałe//3600 #Tyle godzin minęło od epoki, nie licząc dni
print("godziny: ",format(h,"2,.0f"))
poz2=pozostałe%3600 #tyle sekund pozotało po odjęciu godzin
#print(poz2)

minuty=poz2//60 #Tyle minut minęło od epoki, nie licząc dni i godzin
print("minuty: ",format(minuty,"02,.0f"))

sek=poz2%60
print("sekundy: ",format(sek,"2,.0f")) #Sekundy

