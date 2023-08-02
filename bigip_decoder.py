import sys
import argparse

def process_cookie_string(cookie_string):
    parts = cookie_string.split(".")
    if len(parts) != 3:
        raise ValueError('El formato no coincide')
    
    ip = hex(int(parts[0]))
    ip = str(int(ip[8:10], base=16)) + "." + str(int(ip[6:8], base=16)) + "." + str(int(ip[4:6], base=16)) + "." + str(int(ip[2:4], base=16))
    
    port = hex(int(parts[1]))
    port = str(int(port[4:6] + port[2:4], base=16))
    
    return ip, port

def decode_cookie(name, cookie_string):
    try:
        ip, port = process_cookie_string(cookie_string)
        print(f'{name.strip()}-{ip}:{port}')
    except ValueError as e:
        print(f'{name.strip()} - Error:', e)

def decode_cookies_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            print("\n--- IPs decodificadas ---\n")
            for line in lines:
                line = line.strip()
                if ':' in line:
                    name, _, cookie = line.partition(':')
                else:
                    name, cookie = "Cookie", line
                decode_cookie(name, cookie)
            print("\n--------------------------\n")
    except FileNotFoundError:
        print('El archivo especificado no existe.')

def interactive_mode():
    print("Modo interactivo. Introduce una cookie en el formato Nombre:1677787402.36895.0000 o 1677787402.36895.0000, o escribe 'quit' o 'exit' para salir.")
    while True:
        cookie_string = input("Introduce la cookie: ").strip()
        if cookie_string.lower() in ['quit', 'exit']:
            break
        if ':' in cookie_string:
            name, _, cookie_value = cookie_string.partition(':')
        else:
            name, cookie_value = "Cookie", cookie_string
        decode_cookie(name, cookie_value)

# Crear el objeto ArgumentParser con la descripción
parser = argparse.ArgumentParser(description="Este script decodifica cookies de BigIP en el formato Nombre:1677787402.36895.0000 o 1677787402.36895.0000 y muestra la dirección IP y el puerto resultantes. Puedes usar opciones para proporcionar una cookie directamente, leer cookies desde un archivo o utilizar el modo interactivo para introducir cookies manualmente.")

# Definir las opciones de línea de comandos
parser.add_argument("-i", "--input-file", help="Archivo que contiene las cookies en el formato Nombre:1677787402.36895.0000 o 1677787402.36895.0000.", metavar="inputfile")
parser.add_argument("-c", "--cookie", help="Cadena de cookie en el formato Nombre:1677787402.36895.0000 o 1677787402.36895.0000.", metavar="cookietodecode")
parser.add_argument("--interactive", action="store_true", help="Modo interactivo para introducir cookies manualmente. Ignora las otras opciones.")

# Obtener los argumentos proporcionados en la línea de comandos
args = parser.parse_args()

if args.interactive:
    interactive_mode()
elif args.input_file:
    decode_cookies_from_file(args.input_file)
elif args.cookie:
    if ':' in args.cookie:
        name, _, cookie_value = args.cookie.partition(':')
    else:
        name, cookie_value = "Cookie", args.cookie
    decode_cookie(name, cookie_value)
else:
    print("Introduce la cookie:")
    cookie_string = input().strip()
    if ':' in cookie_string:
        name, _, cookie_value = cookie_string.partition(':')
    else:
        name, cookie_value = "Cookie", cookie_string
    decode_cookie(name, cookie_value)
