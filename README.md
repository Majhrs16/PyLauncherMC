# PyLauncherMC

PyLauncherMC es una herramienta escrita en Python 3.11 para lanzar Minecraft Java de forma rápida y eficiente en Windows y Linux. El proyecto se distribuye como un ejecutable único compilado con PyInstaller, lo que significa que no son necesarias dependencias adicionales de Python.

## Argumentos

- `--version VERSION`: Especifica la versión de Minecraft que se lanzará.
- `--nick NICK`: Define el nombre del jugador.
- `--minRam MINRAM`: Asigna la cantidad mínima de memoria asignada a la JVM.
- `--maxRam MAXRAM`: Asigna la cantidad máxima de memoria asignada a la JVM.
- `--debug`: Activa la opción de depuración.

Si no se proporciona ningún argumento, PyLauncherMC mostrará una interfaz de línea de comandos estilo DOS que permite seleccionar las versiones disponibles de Minecraft.

## Uso con acceso directo o script

PyLauncherMC está diseñado para ser utilizado con un acceso directo o un script de shell, lo que te permite abrir tu Minecraft configurado con un solo clic. Puedes crear un acceso directo o un archivo de script (por ejemplo, `.sh` en Linux o `.bat` en Windows) con los argumentos correspondientes y ejecutarlo para lanzar Minecraft automáticamente con la configuración adecuada.

## Requisitos

- Sistema operativo Windows. en el futuro: Linux y MacOS.
- No se requieren dependencias adicionales.

## AVISO DE SEGURIDAD

¡Atención a todos los usuarios que descarguen `PyLauncherMC.exe`!

Quiero asegurarles que mi código NO es malware, incluso les invito a comprobarlo por ustedes mismos.

Los falsos positivos que detectan algunos antivirus en archivos compilados pueden ocurrir debido a características específicas de la compilación, que pueden interpretarse erróneamente como actividad maliciosa.

Posiblemente la causa de dichas alertas sea por ser un programa.exe empaquetado, osea el cual contiene muchas otras secciones de codigo dentro(Libreria estandar de Python3 + dependencias usadas en el proyeto).

Si aún tienen dudas, les animo a que realicen una prueba por sí mismos. Compilen un archivo.py vacío utilizando tanto py2exe como pyinstaller y comprueben que, incluso en ese caso, [VirusTotal](https://www.virustotal.com) también lo detecta como virus.

Gracias por su comprensión y confianza en mi software. Estoy aquí para ayudar si tienen alguna pregunta adicional.

## Compilación de PyLauncherMC
Antes que nada, PyLauncherMC necesita de los siguientes requisitos/pasos:
- `git clone https://github.com/Majhrs16/PyLauncherMC`
- Al menos [Python 3.8](https://www.python.org/downloads/release/python-3810/) para funcionar correctamente.
- Es importante destacar que los archivos `.py` dentro de la carpeta "versions" no deben ser ni siquiera precompilados(`.pyc` o `.pyo`).
- Y por ultimo! Simplemente ejecuta el archivo `Compile.bat` y él se encargará del resto del proceso de compilación.

Por el momento, mi soporte se limita a sistemas Windows. Sin embargo, en el futuro se planea agregar soporte para Linux.

¡Disfruta de PyLauncherMC y aprovecha al máximo tus experiencias de juego!

## Licencia

Este proyecto se distribuye bajo la licencia [GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

---

Si deseas contribuir al proyecto, ¡eres bienvenido! Puedes abrir un problema o enviar una solicitud de extracción.

¡Disfruta de PyLauncherMC y juega Minecraft Java de forma más rápida y eficiente!
