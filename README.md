# BigIP_Cookie_Decoder

Este script decodifica cookies de BigIP en el formato `Nombre:1677787402.36895.0000` o `1677787402.36895.0000` y muestra la dirección IP y el puerto resultantes.

## Instalación

Para instalar este proyecto, sigue los siguientes pasos:

1. Clona el repositorio desde GitHub utilizando el siguiente comando:

```bash
git clone http://github.com/vpanal/BigIP_Cookie_Decoder
```

2. Navega al directorio del proyecto:

```bash
cd BigIP_Cookie_Decoder
```

3. Instala las dependencias requeridas utilizando `pip` y el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Una vez completados estos pasos, el proyecto estará listo para ser utilizado. Si estás utilizando un entorno virtual, asegúrate de activarlo antes de ejecutar el comando `pip install`. Si no tienes `git` instalado, puedes descargar el código del repositorio en formato ZIP desde el enlace: http://github.com/vpanal/BigIP_Cookie_Decoder/archive/main.zip
## Uso

Puedes usar este script de cuatro formas diferentes:

1. **Modo interactivo una sola cookie:** Ejecuta el script sin argumentos (`python bigip_decoder.py`) para ingresar las cookies manualmente. El programa le pedirá que introduzca una cookie en el formato `Nombre:1677787402.36895.0000` o `1677787402.36895.0000`. El script finalizara al decodificarla.

2. **Modo interactivo:** Ejecuta la opcion `--interactive`. El programa le pedirá que introduzca una cookie en el formato `Nombre:1677787402.36895.0000` o `1677787402.36895.0000`. Escribe "quit" o "exit" para salir del modo interactivo.

3. **Proporcionar una sola cookie:** Utiliza la opción `-c` o `--cookie` para proporcionar una sola cookie directamente en la línea de comandos.

   Ejemplo:
   ```
   python bigip_decoder.py -c Nombre:1677787402.36895.0000
   ```

4. **Leer cookies desde un archivo:** Utiliza la opción `-i` o `--input-file` para proporcionar un archivo que contenga cookies en el formato `Nombre:1677787402.36895.0000` o `1677787402.36895.0000`.

   Ejemplo:
   ```
   python bigip_decoder.py -i input.txt
   ```

## Ejemplos

### Ejemplo 1: Modo interactivo una sola Cookie

Ejecuta el script sin argumentos (`python bigip_decoder.py`) para ingresar las cookies manualmente:

```
python bigip_decoder.py
Introduce una cookie en el formato Nombre:1677787402.36895.0000 o 1677787402.36895.0000.
Introduce la cookie: lala:1677787402.36895.0000
lala-10.1.1.100:8080
```

### Ejemplo 2: Modo interactivo

Utiliza la opción `--interactive` para ingresar las cookies manualmente desde el modo interactivo:

```
python bigip_decoder.py --interactive
Modo interactivo. Introduce una cookie en el formato Nombre:1677787402.36895.0000 o 1677787402.36895.0000, o escribe 'quit' o 'exit' para salir.
Introduce la cookie: lala:1677787402.36895.0000
lala-10.1.1.100:8080
Introduce la cookie: 1677787402.36895.0000
Cookie-10.1.1.100:8080
Introduce la cookie: quit
```

### Ejemplo 3: Proporcionar una sola cookie

Utiliza la opción `-c` o `--cookie` para proporcionar una sola cookie directamente en la línea de comandos:

```
python bigip_decoder.py -c lala:1677787402.36895.0000
lala-10.1.1.100:8080

python bigip_decoder.py -c 1677787402.36895.0000
Cookie-10.1.1.100:8080
```

### Ejemplo 4: Leer cookies desde un archivo

Utiliza la opción `-i` o `--input-file` para proporcionar un archivo que contenga cookies en el formato `Nombre:1677787402.36895.0000` o `1677787402.36895.0000`:

Contenido de `input.txt`:
```
srv1:1677787402.36895.0000
srv2:1677787402.36895.0000
1677787402.36895.0000
srv3:1677787402.36895.0000
srv4:1677787402.36895.0000
srv5:1677787402.36895.0000
```

Ejecutar el script:

```
python bigip_decoder.py -i input.txt
--- IPs decodificadas ---

srv1-10.1.1.100:8080
srv2-10.1.1.100:8080
Cookie-10.1.1.100:8080
srv3-10.1.1.100:8080
srv4-10.1.1.100:8080
srv5-10.1.1.100:8080

--------------------------
```

## Requisitos

Este script requiere Python 3 y el módulo `argparse`.

## Referencias

- [Overview of BIG-IP Persistence Cookie Encoding](https://my.f5.com/manage/s/article/K6917)

## Autores

- [vpanal](https://github.com/vpanal): Pentester.

## Licencia

Este proyecto está bajo la Licencia [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/deed.es). Puedes obtener más información en el archivo [LICENSE](LICENSE).
