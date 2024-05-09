import os
import time

R=True

cant_total_PR=0
cant_total_OR=0
cant_total_PVR=0
cant_total_AER=0
cant_total_prod=0


subtotal_Por_Pagar=0

descto=0.1
total=0

while (R==True):
    os.system("cls")
    time.sleep(1)
    print("Este es nuestro menú de Rolls")
    print("")
    print("1. Pikachu Roll $ 4.500")
    print("2. Otaku Roll $ 5.000")
    print("3. Pulpo Venoso Roll $ 5.200")
    print("4. Anguita Eléctrica Roll $ 4.800")
    print("")
    try:
        elige=int(input("Elige el número de tu opción: "))
        if elige <=0 or elige >4:
            print("Debes ingresar número del 1-4.") 
    except ValueError:
        print("Opción no válida. Debes elegir un número del 1-4.")
        continue

    if elige==1:
        cant_total_PR +=1
        cant_total_prod +=1
        subtotal_Por_Pagar += cant_total_PR*4500

    elif elige==2:
        cant_total_OR +=1
        cant_total_prod +=1
        subtotal_Por_Pagar += cant_total_OR*5000
    elif elige==3:
        cant_total_PVR +=1
        cant_total_prod +=1
        subtotal_Por_Pagar += cant_total_PVR*5200

    elif elige==4:
        cant_total_AER +=1
        cant_total_prod +=1
        subtotal_Por_Pagar += cant_total_AER*4800

    try:
        continuar=str(input("¿Deseas agregar al pedido? (si/no): "))
        print("Debes ingresar si o no.") 
    except ValueError:
        print("Opción no válida. Debes elegir si o no.")
        continue
    if continuar=="si":
        True
    else:
        continuar=="no"
        break
   
# Me faltó tiempo para codificar el descto.  

print("")
print("********************************")
print(f"TOTAL PRODUCTOS: {cant_total_prod}")
print("********************************")
print(f"Pikachu Roll: {cant_total_PR}")
print(f"Otaku Roll: {cant_total_OR}")
print(f"Pulpo Venoso Roll: {cant_total_PVR}")
print(f"Anguita Eléctrica Roll: {cant_total_AER}")
print("********************************")
print(f"Subtotal por pagar: $ {subtotal_Por_Pagar}")
print(f"Descuento por código: $ {subtotal_Por_Pagar*descto}")
print(f"TOTAL: $ {subtotal_Por_Pagar-descto}")
print("")




