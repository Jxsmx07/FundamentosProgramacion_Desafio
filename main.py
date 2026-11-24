# Prototipo Funcional - Mesa de Partes Digital (Fundamentos de Programación UPN)
import datetime

# Arreglos paralelos para almacenar los datos de los expedientes
codigos = []
ciudadanos = []
documentos = []
asuntos = []

def registrar_expediente():
    print("\n--- REGISTRO DE NUEVO EXPEDIENTE ---")
    codigo = "EXP-" + str(len(codigos) + 101)
    
    ciudadano = input("Nombres y Apellidos o Razón Social: ").strip()
    if not ciudadano:
        print("Error: El nombre no puede estar vacío.")
        return

    num_doc = input("Número de Documento (DNI 8 dígitos / RUC 11): ").strip()
    if not (num_doc.isdigit() and (len(num_doc) == 8 or len(num_doc) == 11)):
        print("Error: Número de documento inválido.")
        return

    asunto = input("Asunto o motivo del trámite: ").strip()
    if not asunto:
        print("Error: El asunto es obligatorio.")
        return

    # Almacenar en los arreglos paralelos
    codigos.append(codigo)
    ciudadanos.append(ciudadano)
    documentos.append(num_doc)
    asuntos.append(asunto)
    
    # Persistencia inmediata en archivo de texto
    with open("expedientes.txt", "a", encoding="utf-8") as archivo:
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo.write(f"{codigo}|{ciudadano}|{num_doc}|{asunto}|{fecha_hora}\n")

    print(f"¡Éxito! Expediente registrado con el código: {codigo}")

def consultar_expediente():
    print("\n--- CONSULTA DE EXPEDIENTE POR CÓDIGO ---")
    buscado = input("Ingrese el código del expediente (ej. EXP-101): ").strip()
    
    encontrado = False
    for i in range(len(codigos)):
        if codigos[i].lower() == buscado.lower():
            print(f"\n[Expediente Encontrado]")
            print(f"Código: {codigos[i]}")
            print(f"Ciudadano: {ciudadanos[i]}")
            print(f"N° Doc: {documentos[i]}")
            print(f"Asunto: {asuntos[i]}")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ningún registro con ese código.")

def ordenar_y_mostrar():
    print("\n--- LISTA DE EXPEDIENTES ORDENADOS ---")
    if len(codigos) == 0:
        print("No hay expedientes registrados.")
        return
    
    # Ordenamiento básico por código utilizando burbuja sobre arreglos paralelos
    n = len(codigos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if codigos[j] > codigos[j + 1]:
                # Intercambiar elementos en todos los arreglos paralelos
                codigos[j], codigos[j + 1] = codigos[j + 1], codigos[j]
                ciudadanos[j], ciudadanos[j + 1] = ciudadanos[j + 1], ciudadanos[j]
                documentos[j], documentos[j + 1] = documentos[j + 1], documentos[j]
                asuntos[j], asuntos[j + 1] = asuntos[j + 1], asuntos[j]

    for i in range(n):
        print(f"{codigos[i]} | {ciudadanos[i]} | Doc: {documentos[i]} | Asunto: {asuntos[i]}")

# Menú principal de ejecución
def main():
    while True:
        print("\n=== MESA DE PARTES DIGITAL - MUNICIPALIDAD ===")
        print("1. Registrar nuevo expediente")
        print("2. Consultar expediente por código")
        print("3. Ordenar y listar expedientes")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            registrar_expediente()
        elif opcion == "2":
            consultar_expediente()
        elif opcion == "3":
            ordenar_y_mostrar()
        elif opcion == "4":
            print("Saliendo del sistema prototipo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
