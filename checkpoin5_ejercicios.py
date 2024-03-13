# Cree un bucle For de Python
rickroll = ["Never", "Gonna", "Give", "You", "Up"]

for rick in rickroll:
    print(rick)

# Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
    
def suma(num1, num2, num3):
    return num1 + num2 + num3


print(suma(2, 3, 10))

# Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

suma_lambda = lambda num1, num2, num3: num1 + num2 + num3

print(suma_lambda(2, 3, 10))

# Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. 
# Sugerencia, si es necesario, utilice un bucle for in y el operador in.

nombre = 'Enrique'

lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

# Utilizando bucle for
for person in lista_nombre:
    if person == nombre:
        print("El nombre está en la lista")
        break
else:
    print("El nombre no está en la lista")

# Utilizando operador in: solución más sencilla

if nombre in lista_nombre:
    print("El nombre está en la lista")
else:
    print("El nombre no está en la lista")