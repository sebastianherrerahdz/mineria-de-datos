import math

def area_circulo(radio):
    return math.pi * radio ** 2
def volumen_cilindro(radio, altura):
    return area_circulo(radio) * altura
if __name__ == "__main__":    radio = float(input("Ingrese el radio del círculo: "))
altura = float(input("Ingrese la altura del cilindro: "))
print(f"El volumen del cilindro es: {volumen_cilindro(radio, altura)}")