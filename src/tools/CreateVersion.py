import re
import os
import sys
import json

code = """\
from os.path import join, basename
from urllib.request import urlretrieve
from os import remove

class Data(Data):
	Version     = '{ver}'
	VersionPath = join(Data.MC, 'versions', Version)
	CLASSPATH   = []
	Natives     = join(VersionPath, 'natives') # Manten viva esta variable por si acaso otras lo necesitan.

	try:
		with open(join(Data.MC, 'versions', Version, "installed")):
			install = False

	except FileNotFoundError:
		install = True
		PB.text = "Instalando..."

	for url in {libs}:
		file = basename(url)
		path = join(Data.Lib.format(Data = Data), file)

		if install:
			PB.text = "Descargando %s ..." % file
			urlretrieve(url, path)
			PB.text = "Descargando %s ... OK" % file

		CLASSPATH.append(path)

	if install:
		PB.text = "Descargando {ver} ..."
		urlretrieve("{jar}", join(VersionPath, Version + '.jar'))
		PB.text = "Descargando {ver} ... OK"

		with open(join(VersionPath, "installed"), "w"): pass
		PB.text = "Instalando... OK"

	CLASSPATH.append(join(VersionPath, Version + '.jar'))
Data.Flags.JVM[-1] = '-Dlog4j.configurationFile=%s' % join(f'{Data.Lib}', 'client-1.12.xml')
del Data.Flags.JVM[-3] # Deshabilitar parametro natives.

PB.text = "Lanzando..." """

with open(sys.argv[1]) as IN:
	_D = IN.read()
	libs = re.findall("https://libraries\.minecraft\.net/.*?\.jar", _D)
	Json = json.loads(_D)
	mainClass = Json['mainClass']
	ver = Json['id']
	jar = Json["downloads"]["client"]["url"]

code = code.replace('{ver}', ver).replace('{libs}', json.dumps(libs, indent = 12)).replace('{mainClass}', mainClass).replace('{jar}', jar)

path = os.path.join('.', "versions", ver)
os.makedirs(path, exist_ok = True)
with open(os.path.join(path, ver + ".py"), "w") as OUT:
	OUT.write(code)