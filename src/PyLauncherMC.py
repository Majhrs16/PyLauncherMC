from Maj.Sh import dThread, Color, console
from threading import Thread

import urllib.request ## Solamente por dar soporte a las versiones descargadoras.
import traceback
import keyboard
import argparse
import shutil
import runpy
import glob
import time
import sys
import os

__version__ = "b1.2.6"

class _Logger:
    out = None

    def __init__(self):
        self.log = []

    def add(self, *s):
        self.log.extend(s)

    @dThread
    def show(self):
        pass

class LoggerOut(_Logger):
    out = sys.stdout

    @dThread
    def show(self):
        with Color() as term:
            while True:
                if self.log:
                    self.out.write(term.translate(self.log.pop(0)))
                    self.out.flush()

                time.sleep(1 / 30)

class LoggerFile(_Logger):
    out = open("log.log", "w") # No estoy seguro si esto sea seguro...

    @dThread
    def show(self):
        with  Color() as term, self.out:
            while True:
                if self.log:
                    self.out.write(term.cleartext(self.log.pop(0)))
                    self.out.flush()

                time.sleep(1 / 30)

out = LoggerOut()
log = LoggerFile()

class PB:
    def __init__(self, *s):
        self.exit = False
        
        self.prefix  = ""
        self.text    = " ".join(s)
        self.postfix = "\r"
        self.x       = 1

        self.prefixes = [
            "&f[&2*     &f]",
            "&f[&a*&2*    &f]",
            "&f[&2*&a*&2*   &f]",
            "&f[ &2*&a*&2*  &f]",
            "&f[  &2*&a*&2* &f]",
            "&f[   &2*&a*&2*&f]",
            "&f[    &2*&a*&f]",
            "&f[     &2*&f]",
            "&f[    &a*&a*&f]",
            "&f[   &2*&a*&2*&f]",
            "&f[  &2*&a*&2* &f]",
            "&f[ &2*&a*&2*  &f]",
            "&f[&2*&a*&2*   &f]",
            "&f[&2*&a*    &f]"
        ]


    def __enter__(self):
        self.show().start()
        return self

    def __exit__(self, *x):
        self.stop(x != (None, None, None))

    def update(self, outfile = None):
        if outfile is None: outfile = out
        outfile.add((self.prefix + " " + self.text).ljust(self.x) + self.postfix)

    @dThread
    def showPrefix(self):
        while not self.exit:
            for prefix in self.prefixes:
                self.prefix = prefix
                time.sleep(0.250)


    @dThread
    def show(self):
        self.showPrefix().start(daemon = True)

        while not self.exit:
            self.update()
            time.sleep(1 / 30)


    def stop(self, id = 0):
        self.exit = True

        if id: self.prefix = "&f[ &cFAIL &f]"
        else:  self.prefix = "&f[  &2OK  &f]"

        self.postfix = "\n"
        self.update()
        self.update(log)

class CLI:
    def __init__(self):
        self.input    = "> "
        self.Versions = {}

    def start(self):
        self.exit     = False

        self.searchVersions().start(daemon = True)
        self.show().start()

    def getVersions(self):
        Versions = {}
        for i, path in enumerate(glob.glob(os.path.join(".", "versions", "*"))): # Tecnicamente es imposible poner la ruta principal en este tiempo.
            ver = os.path.basename(path)
            if os.path.exists(os.path.join(path, ver + ".py")):
                Versions[str(i + 1)] = ver
        return Versions

    @dThread
    def searchVersions(self):
        while not self.exit:
            self.Versions = self.getVersions()
            time.sleep(1)

    @dThread
    def show(self):
        while True:
            if self.exit: break
            x, y = shutil.get_terminal_size()
            Buff = []

            if sys.platform == "linux":
                Color().clear()

            Buff.append("&2╔" + ("═" * (x - 2) + "╗"))
            Buff.append("&2║&7" + ("PyLauncherMC " + __version__).center(x - 2) + "&2║")
            Buff.append("&2╠" + ("═" * (x - 2) + "╣"))
            if self.Versions:
                Buff.append("&2║ &e" + "Por favor, presione el numero que corresponda a su version:".ljust(x - 3) + "&2║")
                for i, version in self.Versions.items():
                    if i != '0':
                        Buff.append("&2║ &b" + ("%s) %s" % (i, version)).ljust(x - 3).replace(") ", "&f) &b") + "&2║")
            else:
                Buff.append("&2║ &e" + "Buscando versiones instaladas...".ljust(x - 3).replace("...", "&f...") + "&2║")
            for _ in range(len(Buff), y - 2):
                Buff.append("&2║" + (" " * (x - 2) + "&2║"))
            Buff.append("&2║&3 " + self.input.ljust(x - 3).replace("> ", "&f> &b").replace("...", "&f...") + "&2║")
            Buff.append("&2╚" + ("═" * (x - 2) + "╝&f"))

            out.add("\n".join(Buff))

            time.sleep(1 / 10) # 10 FPS

    def getVersion(self):
        key = ""
        while not self.exit:
            if key.isdigit():
                self.input = "> " + key
                if key == '0' or self.Versions.get(key, None):
                    break

            try: key = keyboard.read_key()

            except KeyboardInterrupt:
                key = '0'
                break

            except: pass

        time.sleep(0.1)

        if key == '0':
              self.input = "Cerrando ..."
        else: self.input = "Lanzando ..."

        time.sleep(0.3)

        return self.Versions.get(key, None)

    def stop(self):
        self.exit = True

with PB("Cargando variables por defecto."):
    class Data:
        def __init__(self): pass

        def format(self):
            sep = {'win32': ';', 'linux': ':'}.get(sys.platform, ":")

            self.JVM         = self.JVM         .format(Data = self)
            self.MinRam      = self.MinRam      .format(Data = self)
            self.MaxRam      = self.MaxRam      .format(Data = self)
            self.MC          = self.MC          .format(Data = self)
            self.Lib         = self.Lib         .format(Data = self)
            self.CLASSPATH   = sep.join([s.format(Data = self) for s in self.CLASSPATH])
            self.Natives     = self.Natives     .format(Data = self)
            self.MainClass   = self.MainClass   .format(Data = self)
            if self.Nick:
                self.Nick    = '--username ' + self.Nick.format(Data = self)
            self.Token       = self.Token       .format(Data = self)
            self.Version     = self.Version     .format(Data = self)
            self.AssetsIndex = self.AssetsIndex .format(Data = self)
            self.Flags.JVM   = [s.format(Data = self) for s in self.Flags.JVM]
            self.Flags.MC    = [s.format(Data = self) for s in self.Flags.MC]

            return self

        def clone(self):
            class D(Data): pass
            D.__dict__.update(self.__dict__)
            return D

        Debug       = False
        JVM         = 'java'
        MinRam      = '1G'
        MaxRam      = '1G'
        MC          = '.'
        Lib         = os.path.join('{Data.MC}', 'libraries')
        CLASSPATH = [
            os.path.join('{Data.Lib}', 'log4j-core-2.17.0.jar'),
            os.path.join('{Data.Lib}', 'log4j-api-2.17.0.jar'),
            os.path.join('{Data.MC}', 'versions', '{Data.Version}', '{Data.Version}.jar'),
        ]
        Natives     = os.path.join('{Data.MC}', 'bin', 'natives')
        MainClass   = 'net.minecraft.client.main.Main'
        Nick        = ''
        Token       = 'null'
        Version     = 'CM'
        AssetsIndex = '1.8'

        class Flags:
            JVM = [
                '-Xms{Data.MinRam}',
                '-Xmx{Data.MaxRam}',
                '-XX:+UseG1GC',
                '-XX:+ParallelRefProcEnabled',
                '-XX:MaxGCPauseMillis=200',
                '-XX:+UnlockExperimentalVMOptions',
                '-XX:+DisableExplicitGC',
                '-XX:+AlwaysPreTouch',
                '-XX:G1NewSizePercent=30',
                '-XX:G1MaxNewSizePercent=40',
                '-XX:G1HeapRegionSize=8M',
                '-XX:G1ReservePercent=20',
                '-XX:G1HeapWastePercent=5',
                '-XX:G1MixedGCCountTarget=4',
                '-XX:InitiatingHeapOccupancyPercent=15',
                '-XX:G1MixedGCLiveThresholdPercent=90',
                '-XX:G1RSetUpdatingPauseTimePercent=5',
                '-XX:SurvivorRatio=32',
                '-XX:+PerfDisableSharedMem',
                '-XX:MaxTenuringThreshold=1',
                '-Dusing.aikars.flags=https://mcflags.emc.gs',
                '-Daikars.new.flags=true',
                '-XX:+IgnoreUnrecognizedVMOptions',
                '-XX:MaxGCPauseMillis=50',
                '-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump',
                '-Dsun.java2d.d3d=false',
                '-Dsun.java2d.opengl=true',
                '-Dorg.lwjgl.opengl.Display.allowSoftwareOpenGL=true',
#               '-Xlog:gc*:logs/gc.log:time,uptime:filecount=5,filesize=1M',
                '-XX:+AggressiveOpts',
                '-XX:-UseCompressedOops',
                '-XX:ParallelGCThreads=4',
#               '-Dorg.lwjgl.opengl.Display.setFullscreen=true',
                '-Djava.library.path={Data.Natives}',
                '-cp {Data.CLASSPATH}',
                '-Dlog4j.configurationFile=%s' % os.path.join('{Data.Lib}', 'client-1.7.xml')
            ]

            MC  = [
                '--gameDir ' + os.path.join('{Data.MC}', '{Data.Version}'),
                '--assetsDir ' + os.path.join("{Data.MC}", 'assets'),
                '{Data.Nick}',
                '--accessToken {Data.Token}',
                '--version "{Data.Version}"',
                '--assetIndex {Data.AssetsIndex}',
            ]

def Launch(D):
    CommandLine = " ".join([D.JVM, *D.Flags.JVM, D.MainClass, *D.Flags.MC])

    s = "&aLinea de comando resultante a ejecutar&f: '&b%s&f'\n" % CommandLine
    log.add(s)
    if D.Debug:
        out.add(s)

    else: console and console().hide()

    try: os.system(CommandLine)
    except KeyboardInterrupt: pass
    except Exception as e:
        s = traceback.format_exc()
        log.add(s)
        out.add(s)

if __name__ == "__main__":
    log.show().start(daemon = True)
    out.show().start(daemon = True)

    parser = argparse.ArgumentParser()
    parser.add_argument('--version', default = None, help = 'Version de Minecraft')
    parser.add_argument('--nick', default = Data.Nick, help = 'Nombre del jugador')
    parser.add_argument('--minRam', default = Data.MinRam, help = 'Memoria minima asignada a la JVM')
    parser.add_argument('--maxRam', default = Data.MaxRam, help = 'Memoria maxima asignada a la JVM')
    parser.add_argument('--debug', action="store_true", help = "Opcion para desarrolladores")
    args = parser.parse_args()

    Data.Version = args.version
    Data.MinRam  = args.minRam
    Data.MaxRam  = args.maxRam
    Data.Debug   = args.debug
    Data.Nick    = args.nick

    try:
        i = 0
        max = 1
        while i < max:
            cli = CLI()
            if args.version is None:
                max = 999

                raise

                console and console().restore()
                cli.start()
                Data.Version = cli.getVersion()

            cli.stop()

            if Data.Version is not None:
                dir = os.path.join(Data.MC, "versions", Data.Version)
                os.makedirs(dir, exist_ok = True)
                py = os.path.join(dir, Data.Version + ".py")

                try:
                    assert os.path.exists(py), "\tArchivo de config &f'&b%s&f' no encontrado.\n"
                    with PB("Cargando Minecraft %s." % Data.Version) as pb:
                        D = runpy.run_path(py,
                            init_globals = {"Data": Data, "PB": pb}
                        ).get("Data", None)
                        assert D, "\t&4Version incompatible o mal estructurada&f.\n"

                except AssertionError as e:
                    log.add(e)
                    out.add(e)
                    time.slep(3)

                except Exception as e:
                    s = "\t&4Error al cargar la version&f. &ePara mas detalles&b, &emire el &blog&f.&blog&f.\n"
                    log.add(s)
                    out.add(s)
                    log.add(traceback.format_exc())
                    time.sleep(3)

                Launch(D().format())

            else: break

            i += 1

    except Exception as e:
        s = "\n\n&4Error desconocido&f. &ePor favor notificarlo en &bhttps://github.com/Majhrs16/PyLauncherMC/tree/main\n&f"
        log.add(s)
        out.add(s)
        log.add(traceback.format_exc())
        time.sleep(3)

    console and console().restore()
    sys.exit(0)