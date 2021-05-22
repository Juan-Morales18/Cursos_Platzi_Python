
print("--Comparacion de edades de dos personas--\n")

nombre_persona_1 = input("Ingrese nombre de primera persona: ")
edad_persona_1 = int(input(f"Ingrese edad de {nombre_persona_1}: "))

nombre_persona_2 = input("\nIngrese nombre de segunda persona: ")
edad_persona_2 = int(input(f"Ingrese edad de {nombre_persona_2}: "))

print("\n")
if edad_persona_1 > edad_persona_2:
    print(f"{nombre_persona_1} es mayor que {nombre_persona_2}")
elif edad_persona_1 < edad_persona_2:
    print(f"{nombre_persona_2} es mayor que {nombre_persona_1}")
else:
    print(f"{nombre_persona_1} y {nombre_persona_2} tienen la misma edad")
