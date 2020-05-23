import datetime
import io
wiersze = []


tytul = input("Dodaj tytuł ")
tekst = input("Dodaj tekst sprawozdania ")


strona = io.open("sprawozdania.htm", mode="r", encoding="utf-8")
ilosc_wierszy = strona.readlines()

for i in range(len(ilosc_wierszy)):
    wiersze.append(ilosc_wierszy[i])
    if ilosc_wierszy[i] == "<!--WPIS_POCZATEK-->\n":
        wiersze.append("<h2>" + tytul + "</h2>\n")
        wiersze.append("<h3>" + "Dodano: " + str(datetime.datetime.now())[:19] + "</h3>\n")
        wiersze.append("<p>" + tekst + "<p>\n")

strona.close()

strona = io.open("sprawozdania.htm", mode="w", encoding="utf-8")
ilosc_wierszy_po_edycji = len(wiersze)
for i in range(ilosc_wierszy_po_edycji):
    strona.write(wiersze[i])

strona.close()