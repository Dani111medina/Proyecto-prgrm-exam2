#Invertir un array 

def invertir_array(array):
    return array[::-1]
n = int(input("¿Cuántos elementos tendrá el arreglo?: "))

array_original = []
for i in range(n):
    valor = input(f"Ingrese el valor #{i+1}: ")
    array_original.append(valor)
    
array_invertido = invertir_array(array_original)
print("\nArray original:", array_original)
print("Array invertido:", array_invertido)
