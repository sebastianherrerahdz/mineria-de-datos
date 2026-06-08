import math

def area_circulo(radio):
    return math.pi * radio**2
if __name__ == "__main__":   radio = float(input("Ingrese el radio del círculo: "))
print(f"El área del círculo es: {area_circulo(radio)}") 
