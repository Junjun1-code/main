# Evaluación 1: Calcular monto a pagar por minutos hablados del cliente en una compañia telefonica - Nicolás Aguilar, informatica mencion cyberseguridad, 08-04-2025

# precio_dia=10
# precio_noche=7
# limite_dia=100
# limite_noche=80
# precio_sobre_limite=15
# precio_sobre_limite_n=13

# Pregunta al usuario sobre cantidad de minutos que utilizo el servicio
min_dia=int(input("[?] ¿Cuantos minutos hablo por telefono durante el DIA?"))
min_noche=int(input("[?] ¿Cuantos minutos hablo por telefono durante la NOCHE"))

# Tiempo limite superado/no superado
if min_dia<=100:
    print("[+] DIA: No excede el tiempo limite del servicio")
else:
    print(f"[-] DIA: Se ha excedido el tiempo limite del servicio por {min_dia-100} minutos")
if min_noche<=80:
    print("[+] NOCHE: No excede el tiempo limite del servicio")
else:
    print(f"[-] NOCHE: Se ha excedido el tiempo limite del servicio por {min_noche-80} minutos")

#Calculo de valor total por minutos
precio_total=0
if min_dia<=100:
    precio_total=precio_total+min_dia*10
else:
    precio_total=precio_total+(100*10)+(min_dia-100)*15
if min_noche<=100:
    precio_total=precio_total+min_noche*7
else:
    precio_total=precio_total+(80*7)+(min_noche-80)*13

print(f"[+] El cliente debe pagar ${precio_total}")
