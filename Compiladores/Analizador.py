def obtener_estado(numero, estado_actual):
    # Esta línea define un diccionario llamado `transiciones` que mapea un estado actual a otro diccionario. 
    # El diccionario interno mapea un número de entrada a un nuevo estado. Estas son las transiciones de estado posibles.
    transiciones = {
        0: {5: 1, 10: 2, 25: 3},
        1: {5: 2, 10: 3, 25: 4},
        2: {5: 3, 10: 3, 25: 4},
        3: {5: 4, 10: 4, 25: 4},
        4: {5: 4, 10: 4, 25: 4}
    }
    # Esta línea verifica si el número proporcionado está en el diccionario de transiciones para el estado actual. 
    # Si el estado actual no está en el diccionario `transiciones`, devuelve un diccionario vacío como predeterminado.
    if numero in transiciones.get(estado_actual, {}):
        # Si el número está en las transiciones para el estado actual, retorna el nuevo estado asociado a ese número.
        return transiciones[estado_actual][numero]
    else:
        # Si el número no está en las transiciones para el estado actual, retorna `None`.
        return None

def Archi_read(archi_input):
    # Abre el archivo especificado en `archi_input` en modo de lectura ('r') y lo asigna a la variable `file`.
    with open(archi_input, 'r') as file:
        # Itera sobre cada línea del archivo, enumerándolas desde 1. La variable `i` contiene el número de línea, y `linea` el contenido de la línea.
        for i, linea in enumerate(file, start=1):
            # Inicializa `estado_actual` a 0 al comienzo de cada línea nueva.
            estado_actual = 0
           
            # Separa la línea en componentes basados en espacios y itera sobre cada componente.
            for caracter in linea.split():
                try:
                    # Intenta convertir el componente (caracter) a un entero y lo asigna a `numero`.
                    numero = int(caracter)
                    # Llama a la función `obtener_estado` con el `numero` y el `estado_actual`, asignando el resultado a `nuevo_estado`.
                    nuevo_estado = obtener_estado(numero, estado_actual)
                    if nuevo_estado is not None:
                        # Si `nuevo_estado` no es None, actualiza `estado_actual` al nuevo estado.
                        estado_actual = nuevo_estado
                    else:
                        # Si `nuevo_estado` es None, imprime "INGRESO NO PERMITIDO" y no cambia el estado actual.
                        print(f"INGRESO NO PERMITIDO", end=", ")
                except ValueError:
                    # Si el intento de convertir el componente a entero falla, imprime "INGRESO NO PERMITIDO".
                    print(f"INGRESO NO PERMITIDO", end=", ")
            
            # Al final de la línea, verifica si el `estado_actual` es 4.
            if estado_actual == 4:
                # Si el estado actual es 4, imprime "CADENA VALIDA".
                print("CADENA VALIDA")
            else:
                # Si el estado actual no es 4, imprime "CADENA NO VALIDA".
                print("CADENA NO VALIDA")
