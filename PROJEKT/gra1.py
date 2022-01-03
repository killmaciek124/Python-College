# link do tworzenia tabeli (szachownicy) https://ichi.pro/pl/jak-latwo-tworzyc-tabele-w-pythonie-51327615359229
from tabulate import tabulate
table = [['First', 'Last', 'Age'], ['John', 'Smith', 39], ['Mary', 'Jane', 25], ['Jenny', 'Doe', 28]]
#print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
#def itemplacement(table):
info = {'First Name': ['John', 'Mary', 'Jennifer'], 'Last Name': ['Smith', 'Jane', 'Doe'], 'Age': [39, 25, 28]}
print(tabulate(info, headers='keys', tablefmt='fancy_grid',  ))