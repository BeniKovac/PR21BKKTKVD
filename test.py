import csv

headers = set()
merilna_mesta = set()
merilna_mesta_na_zacetku = set()
popolna_merilna_mesta = set()

for i in range(2000, 2020, 1):
    with open('podatki/improved/'+str(i)+'.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        # na zacetku vsakega CSVja je BoM, zato v naslednjem koraku uporabimo [3:]
        vrstica = next(reader)

        # print(', '.join(vrstica)[3:])
        if len(headers) > 0:
            headers = headers.intersection(set(vrstica))
        else:
            headers = set(vrstica)

        trenutna_merilna_mesta = set()
        for vrstica in reader:
            if i == 2000:
                merilna_mesta_na_zacetku.add(vrstica[6])
            merilna_mesta.add(vrstica[6])
            trenutna_merilna_mesta.add(vrstica[6])

        if i == 2000:
            popolna_merilna_mesta = merilna_mesta_na_zacetku
        popolna_merilna_mesta = popolna_merilna_mesta.intersection(trenutna_merilna_mesta)

print('Skupni headerji: '+', '.join(headers))
print('Merilnih mest na zacetku: '+str(len(merilna_mesta_na_zacetku)))
print('Popolnih merilnih mest: '+str(len(popolna_merilna_mesta)))
print('Vseh merilnih mest: '+str(len(merilna_mesta)))