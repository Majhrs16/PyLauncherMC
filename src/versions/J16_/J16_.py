############################################################################################
# Atencion! Esta es solamente una version de prueba para testear las capacidades del PLMC. #
#     Se puede usar para inspirarte o adaptarlo a otras versiones de Minecraft.            #
#                                                                                          #
# Las versione oficiales hechas por Majhrs16 se distrubuiran como de costumbre.            #
############################################################################################
# Attention! This is just a test version to test the capabilities of PLMC.                 #
#     It can be used for inspiration or adapted to other versions of Minecraft.            #
#                                                                                          #
# Official versions made by Majhrs16 will be distributed as usual.                         #
############################################################################################

from os.path import join, basename
from urllib.request import urlretrieve
# from zipfile import ZipFile
from os import remove

from time import sleep

class Data(Data):
	VersionPath = join(Data.MC, 'versions', Data.Version)
	CLASSPATH   = []
	Natives     = join(VersionPath, 'natives') # Manten viva esta variable por si acaso otras lo necesitan.

	try:
		with open(join(Data.MC, 'versions', Data.Version, "installed")):
			install = False

	except FileNotFoundError:
		install = True
		PB.text = "Instalando..."

	for url in [ # Los comentados en esta lista causan conflictos.
			"https://libraries.minecraft.net/com/mojang/patchy/1.3.9/patchy-1.3.9.jar",
			"https://libraries.minecraft.net/oshi-project/oshi-core/1.1/oshi-core-1.1.jar",
			"https://libraries.minecraft.net/net/java/dev/jna/jna/4.4.0/jna-4.4.0.jar",
			"https://libraries.minecraft.net/net/java/dev/jna/platform/3.4.0/platform-3.4.0.jar",
			"https://libraries.minecraft.net/com/ibm/icu/icu4j/66.1/icu4j-66.1.jar",
			"https://libraries.minecraft.net/com/mojang/javabridge/1.0.22/javabridge-1.0.22.jar",
			"https://libraries.minecraft.net/net/sf/jopt-simple/jopt-simple/5.0.3/jopt-simple-5.0.3.jar",
			"https://libraries.minecraft.net/io/netty/netty-all/4.1.25.Final/netty-all-4.1.25.Final.jar",
			"https://libraries.minecraft.net/com/google/guava/guava/21.0/guava-21.0.jar",
			"https://libraries.minecraft.net/org/apache/commons/commons-lang3/3.5/commons-lang3-3.5.jar",
			"https://libraries.minecraft.net/commons-io/commons-io/2.5/commons-io-2.5.jar",
			"https://libraries.minecraft.net/commons-codec/commons-codec/1.10/commons-codec-1.10.jar",
			"https://libraries.minecraft.net/net/java/jinput/jinput/2.0.5/jinput-2.0.5.jar",
			"https://libraries.minecraft.net/net/java/jutils/jutils/1.0.0/jutils-1.0.0.jar",
			"https://libraries.minecraft.net/com/mojang/brigadier/1.0.17/brigadier-1.0.17.jar",
			"https://libraries.minecraft.net/com/mojang/datafixerupper/4.0.26/datafixerupper-4.0.26.jar",
			"https://libraries.minecraft.net/com/google/code/gson/gson/2.8.0/gson-2.8.0.jar",
			"https://libraries.minecraft.net/com/mojang/authlib/2.1.28/authlib-2.1.28.jar",
			"https://libraries.minecraft.net/org/apache/commons/commons-compress/1.8.1/commons-compress-1.8.1.jar",
			"https://libraries.minecraft.net/org/apache/httpcomponents/httpclient/4.3.3/httpclient-4.3.3.jar",
			"https://libraries.minecraft.net/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar",
			"https://libraries.minecraft.net/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.jar",
			"https://libraries.minecraft.net/it/unimi/dsi/fastutil/8.2.1/fastutil-8.2.1.jar",
			"https://libraries.minecraft.net/org/apache/logging/log4j/log4j-api/2.8.1/log4j-api-2.8.1.jar",
			"https://libraries.minecraft.net/org/apache/logging/log4j/log4j-core/2.8.1/log4j-core-2.8.1.jar",
#			"https://libraries.minecraft.net/org/lwjgl/lwjgl/3.2.1/lwjgl-3.2.1.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl/3.2.2/lwjgl-3.2.2.jar",
#			"https://libraries.minecraft.net/org/lwjgl/lwjgl-jemalloc/3.2.1/lwjgl-jemalloc-3.2.1.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-jemalloc/3.2.2/lwjgl-jemalloc-3.2.2.jar",
#			"https://libraries.minecraft.net/org/lwjgl/lwjgl-openal/3.2.1/lwjgl-openal-3.2.1.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-openal/3.2.2/lwjgl-openal-3.2.2.jar",
#			"https://libraries.minecraft.net/org/lwjgl/lwjgl-opengl/3.2.1/lwjgl-opengl-3.2.1.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-opengl/3.2.2/lwjgl-opengl-3.2.2.jar",
#			"https://libraries.minecraft.net/org/lwjgl/lwjgl-glfw/3.2.1/lwjgl-glfw-3.2.1.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-glfw/3.2.2/lwjgl-glfw-3.2.2.jar",
#			"https://libraries.minecraft.net/org/lwjgl/lwjgl-stb/3.2.1/lwjgl-stb-3.2.1.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-stb/3.2.2/lwjgl-stb-3.2.2.jar",
#			"https://libraries.minecraft.net/org/lwjgl/lwjgl-tinyfd/3.2.1/lwjgl-tinyfd-3.2.1.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-tinyfd/3.2.2/lwjgl-tinyfd-3.2.2.jar",
#			"https://libraries.minecraft.net/org/lwjgl/lwjgl/3.2.1/lwjgl-3.2.1.jar",
#			"https://libraries.minecraft.net/org/lwjgl/lwjgl/3.2.1/lwjgl-3.2.1-natives-macos.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl/3.2.2/lwjgl-3.2.2.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl/3.2.2/lwjgl-3.2.2-natives-linux.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl/3.2.2/lwjgl-3.2.2-natives-windows.jar",
#			"https://libraries.minecraft.net/org/lwjgl/lwjgl-jemalloc/3.2.1/lwjgl-jemalloc-3.2.1.jar",
#			"https://libraries.minecraft.net/org/lwjgl/lwjgl-jemalloc/3.2.1/lwjgl-jemalloc-3.2.1-natives-macos.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-jemalloc/3.2.2/lwjgl-jemalloc-3.2.2.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-jemalloc/3.2.2/lwjgl-jemalloc-3.2.2-natives-linux.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-jemalloc/3.2.2/lwjgl-jemalloc-3.2.2-natives-windows.jar",
#			"https://libraries.minecraft.net/org/lwjgl/lwjgl-openal/3.2.1/lwjgl-openal-3.2.1.jar",
#			"https://libraries.minecraft.net/org/lwjgl/lwjgl-openal/3.2.1/lwjgl-openal-3.2.1-natives-macos.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-openal/3.2.2/lwjgl-openal-3.2.2.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-openal/3.2.2/lwjgl-openal-3.2.2-natives-linux.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-openal/3.2.2/lwjgl-openal-3.2.2-natives-windows.jar",
#			"https://libraries.minecraft.net/org/lwjgl/lwjgl-opengl/3.2.1/lwjgl-opengl-3.2.1.jar",
#			"https://libraries.minecraft.net/org/lwjgl/lwjgl-opengl/3.2.1/lwjgl-opengl-3.2.1-natives-macos.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-opengl/3.2.2/lwjgl-opengl-3.2.2.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-opengl/3.2.2/lwjgl-opengl-3.2.2-natives-linux.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-opengl/3.2.2/lwjgl-opengl-3.2.2-natives-windows.jar",
#			"https://libraries.minecraft.net/org/lwjgl/lwjgl-glfw/3.2.1/lwjgl-glfw-3.2.1.jar",
#			"https://libraries.minecraft.net/org/lwjgl/lwjgl-glfw/3.2.1/lwjgl-glfw-3.2.1-natives-macos.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-glfw/3.2.2/lwjgl-glfw-3.2.2.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-glfw/3.2.2/lwjgl-glfw-3.2.2-natives-linux.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-glfw/3.2.2/lwjgl-glfw-3.2.2-natives-windows.jar",
#			"https://libraries.minecraft.net/org/lwjgl/lwjgl-stb/3.2.1/lwjgl-stb-3.2.1.jar",
#			"https://libraries.minecraft.net/org/lwjgl/lwjgl-stb/3.2.1/lwjgl-stb-3.2.1-natives-macos.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-tinyfd/3.2.2/lwjgl-tinyfd-3.2.2.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-tinyfd/3.2.2/lwjgl-tinyfd-3.2.2-natives-linux.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-tinyfd/3.2.2/lwjgl-tinyfd-3.2.2-natives-windows.jar",
#			"https://libraries.minecraft.net/org/lwjgl/lwjgl-tinyfd/3.2.1/lwjgl-tinyfd-3.2.1.jar",
#			"https://libraries.minecraft.net/org/lwjgl/lwjgl-tinyfd/3.2.1/lwjgl-tinyfd-3.2.1-natives-macos.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-stb/3.2.2/lwjgl-stb-3.2.2.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-stb/3.2.2/lwjgl-stb-3.2.2-natives-linux.jar",
			"https://libraries.minecraft.net/org/lwjgl/lwjgl-stb/3.2.2/lwjgl-stb-3.2.2-natives-windows.jar",
			"https://libraries.minecraft.net/com/mojang/text2speech/1.11.3/text2speech-1.11.3.jar",
			"https://libraries.minecraft.net/com/mojang/text2speech/1.11.3/text2speech-1.11.3.jar",
			"https://libraries.minecraft.net/com/mojang/text2speech/1.11.3/text2speech-1.11.3-natives-linux.jar",
			"https://libraries.minecraft.net/com/mojang/text2speech/1.11.3/text2speech-1.11.3-natives-windows.jar",
			"https://libraries.minecraft.net/ca/weblite/java-objc-bridge/1.0.0/java-objc-bridge-1.0.0.jar",
			"https://libraries.minecraft.net/ca/weblite/java-objc-bridge/1.0.0/java-objc-bridge-1.0.0-natives-osx.jar",
			"https://libraries.minecraft.net/ca/weblite/java-objc-bridge/1.0.0/java-objc-bridge-1.0.0.jar"
		]:
		file = basename(url)
		path = join(Data.Lib.format(Data = Data), file)


		if install:
			PB.text = "Descargando %s ..." % file
			urlretrieve(url, path)
			PB.text = "Descargando %s ... OK" % file


#		if "natives" in path: # No hace falta descomprimirlos, ya que ya estan como .jar en CLASSPATH.
#			PB.text = "Extrayendo %s  ... " % file
#			with ZipFile(path, 'r') as zip:
#				zip.extractall(Natives)
#			PB.text = "Extrayendo %s ... OK" % file
#
#		else:
		CLASSPATH.append(path)

	if install:
		PB.text = "Descargando J16 ..."
		urlretrieve("https://piston-data.mojang.com/v1/objects/37fd3c903861eeff3bc24b71eed48f828b5269c8/client.jar", join(VersionPath, Data.Version + '.jar'))
		PB.text = "Descargando J16 ... OK"

		with open(join(VersionPath, "installed"), "w"): pass
		PB.text = "Instalando... OK"

	CLASSPATH.append(join(VersionPath, Data.Version + '.jar'))
Data.Flags.JVM[-1] = '-Dlog4j.configurationFile=%s' % join(f'{Data.Lib}', 'client-1.12.xml')
del Data.Flags.JVM[-3] # Deshabilitar parametro natives.

PB.text = "Lanzando..."

# Hecho por Majhrs16 / Made by Majhrs16