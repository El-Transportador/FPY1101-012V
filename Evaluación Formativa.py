import os
import time

R=True

valor_proll=4500
valor_oroll=5000
valor_pvroll=5200
valor_aeroll=4800

cant_total_PR=0
cant_total_OR=0
cant_total_PVR=0
cant_total_AER=0

cant_total_prod=0
subtotal_Por_Pagar=0
descto=0.1
total=0



contador=0
while (R==True):
    os.system("cls")
    print("Este es nuestro menú de Rolls")
    print("")
    print("1. Pikachu Roll $ 4.500")
    print("2. Otaku Roll $ 5.000")
    print("3. Pulpo Venoso Roll $ 5.200")
    print("4. Anguita Eléctrica Roll $ 4.800")
    print("")
    try:
        elige=int(input("Elige el número de tu opción: "))
    except ValueError:
        print("Opción no válida. Debes elegir un número del 1-4.")
        continue
    
    try:
        cant_ped=int(input("Ingresa la cantidad que deseas llevar: "))
    except ValueError:
        print("Ingreso incorrecto. Debes ingresar un número")
        continue

    if elige==1:
        cant_total_PR +=cant_ped
        cant_total_prod +=cant_ped
        subtotal_Por_Pagar = valor_proll*cant_ped
    
    elif elige==2:
        cant_total_OR +=cant_ped
        cant_total_prod +=cant_ped
        subtotal_Por_Pagar = valor_oroll*cant_ped

    break

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




