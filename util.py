import os
import re


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')

# Por Refinar: ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


lp_regex = re.compile(
    r"""
    (
        ([A-Z]){2}
        (-|·)
        (\w){2}
        (-|·)
        (\d){2}
    )|(
        ([A-Z]){2}
        (-|·|*)
        (\w){2}(\d){2}
    )
""")


def imprimir_datos(ciudadano: list):
    print(f'''

DATOS DEL CIUDADANO:

NIF:               {ciudadano[0].upper()}

Nombre:            {ciudadano[1].title()}

Edad:              {ciudadano[2]}

Pertenece a la UE: {ciudadano[5].title()}
''')


def imprimir_cert_nac(ciudadano: list):
    print(f'''
CERTIFICADO DE NACIMIENTO DEL CIUDADANO:
                
NIF:                 {ciudadano[0]}

Nombre:              {ciudadano[1]}

Fecha de Nacimiento: {ciudadano[3]}    
''')


def imprimir_cert_conyugal(ciudadano: list):
    print(f'''
ESTADO CONYUGAL:

    {ciudadano[4].title()}
''')


def imprimir_cert_ue(ciudadano: list):
    print(f'''
PERTENENCIA A LA UNION EUROPEA:

    {ciudadano[5].title()}
''')


def input_brand():
    while True:
        marca = input("Ingrese la marca del vehículo: ")
        if len(marca) in range(2, 16):
            return marca


def input_plate():
    while True:
        patente = input("Ingrese patente del vehículo: ")
        if not not lp_regex.fullmatch(patente):
            return patente


def validacion_edad():
    while True:
        edad = int(input("Ingrese la edad del ciudadano: "))
        if edad >= 0:
            return edad


def validacion_fecha_nacimiento():
    while True:
        fecha_nacimiento = input("Ingrese fecha de nacimiento: ")
        return fecha_nacimiento


def validacion_estado_conyugal():
    while True:
        estado_conyugal = input("Ingrese estado conyugal: ").lower()

        if estado_conyugal in ("casado", "soltero", "viudo", "divorciado", "mas solo que la luna"):
            if estado_conyugal == "casado":
                print("Puta que eri weon...")
            return estado_conyugal


def validacion_union_europea():
    while True:
        union_europea = input(
            "¿Pertenece a la Unión Europea? [s/n]: ").lower()
        if union_europea in ("s", "n"):
            return union_europea
