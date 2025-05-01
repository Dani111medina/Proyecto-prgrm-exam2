def invertir_array(array):
    return array[::-1]

# 1. Solicitar la cantidad de elementos
n = int(input("¿Cuántos elementos tendrá el arreglo?: "))

# 2. Solicitar los elementos
array_original = []
for i in range(n):
    valor = input(f"Ingrese el valor #{i+1}: ")
    array_original.append(valor)

# 3. Llamar la función y mostrar resultados
array_invertido = invertir_array(array_original)

print("\nArray original:", array_original)
print("Array invertido:", array_invertido)
