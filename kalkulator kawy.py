from tabulate import tabulate

dane = [["1", "Kawa palona Arabica", "5 zł"], 
        ["2", "Kawa palona Robusta", "6 zł"], 
        ["3", "Kawa bezkofeinowa", "7 zł"]]

naglowek = ["Numer kawy", "Nazwa", "Cena za 1 dekagram"]

print(tabulate(dane, headers=naglowek, tablefmt='fancy_grid'))

numer = input("Podaj numer kawy: ")
waga = int(input("Podaj wage kawy: "))

if numer == '1':
  koszt = str(waga * 5)
elif numer == '2':
  koszt =str(waga * 6)
elif numer == '3':
  koszt = str(waga * 7)
else:
  koszt = '0'

print("Koszt kawy wynosi: " + koszt + "zł")