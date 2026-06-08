def total_factura(cantidad, iva=21):
    total = cantidad + (cantidad * iva / 100)
    return total 
if __name__ == "__main__":    cantidad = float(input("Ingrese el monto de la factura: "))
iva = float(input("Ingrese el porcentaje de IVA (por defecto es 21%): "))
if iva == "":    iva = 21
else:    iva = float(iva)
print(f"El total de la factura es: {total_factura(cantidad, iva)}") 
