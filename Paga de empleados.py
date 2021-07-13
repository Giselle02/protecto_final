nombre = input("Ingrese el nombre del empleado: ")
salario = float(input("Ingrese el salario basico por hora: "))
horas = int(input("Ingrese la cantidad de horas normales de trabajo: "))
h_extra = int(input("Ingrese la cantidad de horas extras trabajadas: "))

import matplotlib.pyplot as plt
fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.

salario_normal = horas * salario
salario_extra = (h_extra * salario) * 1.25

retencion = salario_extra * 0.1

a_pagar = salario_normal + salario_extra - retencion

print("\nLa paga del empleado", nombre, "es de", a_pagar,
      "\nLa retencion fue de:", retencion)