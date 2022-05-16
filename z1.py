import numpy

table = numpy.genfromtxt('ABBREV.csv', delimiter=';', dtype=None, names=True, encoding="utf8")

table.sort(order=['Energ_Kcal', 'Shrt_Desc'])
print("Больше всего калорий в", str(table[-1][1]) + ':', table[-1][3])

table.sort(order=['Shrt_Desc'])
table.sort(order=['Sugar_Tot_g'])
print("Меньше всего сахара в", str(table[0][1]) + ':', table[0][9])

table.sort(order=['Shrt_Desc'])
table.sort(order=['Protein_g'])
print("Больше всего протеина в", str(table[-1][1]) + ':', table[-1][4])

table.sort(order=['Vit_C_mg'])
print("Больше всего витамина С в", str(table[-1][1]) + ':', table[-1][20])

