from os.path import join, basename
from urllib.request import urlretrieve
from os import remove

class Data(Data):
	Version     = '1.20.1'
	VersionPath = join(Data.MC, 'versions', Version)
	CLASSPATH   = []
	Natives     = join(VersionPath, 'natives') # Manten viva esta variable por si acaso otras lo necesitan.

	try:
		with open(join(Data.MC, 'versions', Version, "installed")):
			install = False

	except FileNotFoundError:
		install = True
		PB.text = "Instalando..."

	for url in [
            "https://libraries.minecraft.net/ca/weblite/java-objc-bridge/1.1/java-objc-bridge-1.1.jar",
            "https://libraries.minecraft.net/com/github/oshi/oshi-core/6.2.2/oshi-core-6.2.2.jar",
            "https://libraries.minecraft.net/com/google/code/gson/gson/2.10/gson-2.10.jar",
            "https://libraries.minecraft.net/com/google/guava/failureaccess/1.0.1/failureaccess-1.0.1.jar",
            "https://libraries.minecraft.net/com/google/guava/guava/31.1-jre/guava-31.1-jre.jar",
            "https://libraries.minecraft.net/com/ibm/icu/icu4j/71.1/icu4j-71.1.jar",
            "https://libraries.minecraft.net/com/mojang/authlib/4.0.43/authlib-4.0.43.jar",
            "https://libraries.minecraft.net/com/mojang/blocklist/1.0.10/blocklist-1.0.10.jar",
            "https://libraries.minecraft.net/com/mojang/brigadier/1.1.8/brigadier-1.1.8.jar",
            "https://libraries.minecraft.net/com/mojang/datafixerupper/6.0.8/datafixerupper-6.0.8.jar",
            "https://libraries.minecraft.net/com/mojang/logging/1.1.1/logging-1.1.1.jar",
            "https://libraries.minecraft.net/com/mojang/patchy/2.2.10/patchy-2.2.10.jar",
            "https://libraries.minecraft.net/com/mojang/text2speech/1.17.9/text2speech-1.17.9.jar",
            "https://libraries.minecraft.net/commons-codec/commons-codec/1.15/commons-codec-1.15.jar",
            "https://libraries.minecraft.net/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar",
            "https://libraries.minecraft.net/commons-logging/commons-logging/1.2/commons-logging-1.2.jar",
            "https://libraries.minecraft.net/io/netty/netty-buffer/4.1.82.Final/netty-buffer-4.1.82.Final.jar",
            "https://libraries.minecraft.net/io/netty/netty-codec/4.1.82.Final/netty-codec-4.1.82.Final.jar",
            "https://libraries.minecraft.net/io/netty/netty-common/4.1.82.Final/netty-common-4.1.82.Final.jar",
            "https://libraries.minecraft.net/io/netty/netty-handler/4.1.82.Final/netty-handler-4.1.82.Final.jar",
            "https://libraries.minecraft.net/io/netty/netty-resolver/4.1.82.Final/netty-resolver-4.1.82.Final.jar",
            "https://libraries.minecraft.net/io/netty/netty-transport-classes-epoll/4.1.82.Final/netty-transport-classes-epoll-4.1.82.Final.jar",
            "https://libraries.minecraft.net/io/netty/netty-transport-native-epoll/4.1.82.Final/netty-transport-native-epoll-4.1.82.Final-linux-aarch_64.jar",
            "https://libraries.minecraft.net/io/netty/netty-transport-native-epoll/4.1.82.Final/netty-transport-native-epoll-4.1.82.Final-linux-x86_64.jar",
            "https://libraries.minecraft.net/io/netty/netty-transport-native-unix-common/4.1.82.Final/netty-transport-native-unix-common-4.1.82.Final.jar",
            "https://libraries.minecraft.net/io/netty/netty-transport/4.1.82.Final/netty-transport-4.1.82.Final.jar",
            "https://libraries.minecraft.net/it/unimi/dsi/fastutil/8.5.9/fastutil-8.5.9.jar",
            "https://libraries.minecraft.net/net/java/dev/jna/jna-platform/5.12.1/jna-platform-5.12.1.jar",
            "https://libraries.minecraft.net/net/java/dev/jna/jna/5.12.1/jna-5.12.1.jar",
            "https://libraries.minecraft.net/net/sf/jopt-simple/jopt-simple/5.0.4/jopt-simple-5.0.4.jar",
            "https://libraries.minecraft.net/org/apache/commons/commons-compress/1.21/commons-compress-1.21.jar",
            "https://libraries.minecraft.net/org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.jar",
            "https://libraries.minecraft.net/org/apache/httpcomponents/httpclient/4.5.13/httpclient-4.5.13.jar",
            "https://libraries.minecraft.net/org/apache/httpcomponents/httpcore/4.4.15/httpcore-4.4.15.jar",
            "https://libraries.minecraft.net/org/apache/logging/log4j/log4j-api/2.19.0/log4j-api-2.19.0.jar",
            "https://libraries.minecraft.net/org/apache/logging/log4j/log4j-core/2.19.0/log4j-core-2.19.0.jar",
            "https://libraries.minecraft.net/org/apache/logging/log4j/log4j-slf4j2-impl/2.19.0/log4j-slf4j2-impl-2.19.0.jar",
            "https://libraries.minecraft.net/org/joml/joml/1.10.5/joml-1.10.5.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-glfw/3.3.1/lwjgl-glfw-3.3.1.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-glfw/3.3.1/lwjgl-glfw-3.3.1-natives-linux.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-glfw/3.3.1/lwjgl-glfw-3.3.1-natives-macos.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-glfw/3.3.1/lwjgl-glfw-3.3.1-natives-macos-arm64.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-glfw/3.3.1/lwjgl-glfw-3.3.1-natives-windows.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-glfw/3.3.1/lwjgl-glfw-3.3.1-natives-windows-arm64.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-glfw/3.3.1/lwjgl-glfw-3.3.1-natives-windows-x86.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-jemalloc/3.3.1/lwjgl-jemalloc-3.3.1.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-jemalloc/3.3.1/lwjgl-jemalloc-3.3.1-natives-linux.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-jemalloc/3.3.1/lwjgl-jemalloc-3.3.1-natives-macos.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-jemalloc/3.3.1/lwjgl-jemalloc-3.3.1-natives-macos-arm64.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-jemalloc/3.3.1/lwjgl-jemalloc-3.3.1-natives-windows.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-jemalloc/3.3.1/lwjgl-jemalloc-3.3.1-natives-windows-arm64.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-jemalloc/3.3.1/lwjgl-jemalloc-3.3.1-natives-windows-x86.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-openal/3.3.1/lwjgl-openal-3.3.1.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-openal/3.3.1/lwjgl-openal-3.3.1-natives-linux.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-openal/3.3.1/lwjgl-openal-3.3.1-natives-macos.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-openal/3.3.1/lwjgl-openal-3.3.1-natives-macos-arm64.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-openal/3.3.1/lwjgl-openal-3.3.1-natives-windows.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-openal/3.3.1/lwjgl-openal-3.3.1-natives-windows-arm64.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-openal/3.3.1/lwjgl-openal-3.3.1-natives-windows-x86.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-opengl/3.3.1/lwjgl-opengl-3.3.1.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-opengl/3.3.1/lwjgl-opengl-3.3.1-natives-linux.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-opengl/3.3.1/lwjgl-opengl-3.3.1-natives-macos.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-opengl/3.3.1/lwjgl-opengl-3.3.1-natives-macos-arm64.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-opengl/3.3.1/lwjgl-opengl-3.3.1-natives-windows.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-opengl/3.3.1/lwjgl-opengl-3.3.1-natives-windows-arm64.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-opengl/3.3.1/lwjgl-opengl-3.3.1-natives-windows-x86.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-stb/3.3.1/lwjgl-stb-3.3.1.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-stb/3.3.1/lwjgl-stb-3.3.1-natives-linux.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-stb/3.3.1/lwjgl-stb-3.3.1-natives-macos.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-stb/3.3.1/lwjgl-stb-3.3.1-natives-macos-arm64.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-stb/3.3.1/lwjgl-stb-3.3.1-natives-windows.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-stb/3.3.1/lwjgl-stb-3.3.1-natives-windows-arm64.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-stb/3.3.1/lwjgl-stb-3.3.1-natives-windows-x86.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-tinyfd/3.3.1/lwjgl-tinyfd-3.3.1.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-tinyfd/3.3.1/lwjgl-tinyfd-3.3.1-natives-linux.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-tinyfd/3.3.1/lwjgl-tinyfd-3.3.1-natives-macos.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-tinyfd/3.3.1/lwjgl-tinyfd-3.3.1-natives-macos-arm64.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-tinyfd/3.3.1/lwjgl-tinyfd-3.3.1-natives-windows.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-tinyfd/3.3.1/lwjgl-tinyfd-3.3.1-natives-windows-arm64.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl-tinyfd/3.3.1/lwjgl-tinyfd-3.3.1-natives-windows-x86.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl/3.3.1/lwjgl-3.3.1.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl/3.3.1/lwjgl-3.3.1-natives-linux.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl/3.3.1/lwjgl-3.3.1-natives-macos.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl/3.3.1/lwjgl-3.3.1-natives-macos-arm64.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl/3.3.1/lwjgl-3.3.1-natives-windows.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl/3.3.1/lwjgl-3.3.1-natives-windows-arm64.jar",
            "https://libraries.minecraft.net/org/lwjgl/lwjgl/3.3.1/lwjgl-3.3.1-natives-windows-x86.jar",
            "https://libraries.minecraft.net/org/slf4j/slf4j-api/2.0.1/slf4j-api-2.0.1.jar"
]:
		file = basename(url)
		path = join(Data.Lib.format(Data = Data), file)

		if install:
			PB.text = "Descargando %s ..." % file
			urlretrieve(url, path)
			PB.text = "Descargando %s ... OK" % file

		CLASSPATH.append(path)

	if install:
		PB.text = "Descargando 1.20.1 ..."
		urlretrieve("https://piston-data.mojang.com/v1/objects/0c3ec587af28e5a785c0b4a7b8a30f9a8f78f838/client.jar", join(VersionPath, Version + '.jar'))
		PB.text = "Descargando 1.20.1 ... OK"

		with open(join(VersionPath, "installed"), "w"): pass
		PB.text = "Instalando... OK"

	CLASSPATH.append(join(VersionPath, Version + '.jar'))
Data.Flags.JVM[-1] = '-Dlog4j.configurationFile=%s' % join(f'{Data.Lib}', 'client-1.12.xml')
del Data.Flags.JVM[-3] # Deshabilitar parametro natives.

PB.text = "Lanzando..." 