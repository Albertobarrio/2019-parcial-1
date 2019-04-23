from decimal_hexadecimal import decimal_to_hexadecimal
def main():
    palabra=input("Ingrese un numero: ")
    print("Su numero en hexadecimal es:",interfaz(palabra))

def interfaz(data):
    try:    
        decimal=int(data)
        return decimal_to_hexadecimal(decimal)
    except:
        return 'ERROR:Debe ingresar un numero entero'
