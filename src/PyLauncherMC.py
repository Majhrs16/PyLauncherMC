from threading import Thread
from Sh import dThread, Color
import argparse
import runpy
import os
import time
import sys
import glob
import keyboard
import shutil

__version__ = "b1.0"

class Logger:
    log = []

    def add(self, *s):
        self.log.extend(s)

    @dThread
    def show(self):
        with Color() as term:
            while True:
                if self.log: sys.stdout.write(term.translate(self.log.pop(0)))
                else: time.sleep(0.1)

log = Logger()

class PB:
    def __init__(self, *s):
        self.exit = False
        self.s = " ".join(s)

    def __enter__(self):
        self.show().start()
        return self

    def __exit__(self, *x):
        self.stop()

        if x == (None,) * 3:
            log.add("&f[  &2OK  &f] " + self.s + "\n")
        else:
            log.add("&f[ &cFAIL &f] " + self.s + "\n")

    @dThread
    def show(self):
        while not self.exit:
            for s in ["&f[&a*     &f]",
                      "&f[&a**    &f]",
                      "&f[&a***   &f]",
                      "&f[&a ***  &f]",
                      "&f[&a  *** &f]",
                      "&f[&a   ***&f]",
                      "&f[&a    **&f]",
                      "&f[&a     *&f]",
                      "&f[&a    **&f]",
                      "&f[&a   ***&f]",
                      "&f[&a  *** &f]",
                      "&f[&a ***  &f]",
                      "&f[&a***   &f]",
                      "&f[&a**    &f]"
                     ]:
                if self.exit: break
                log.add(s, " ", self.s, "\r")
                time.sleep(0.250)

    def stop(self):
        self.exit = True

class CLI:
    def __init__(self):
        self.input    = "> "
        self.exit     = False
        self.Versions = {}

    def start(self):
        self.searchVersions().start(daemon = True)
        self.show().start()

    def getVersions(self):
        Versions = {}
        for i, path in enumerate(glob.glob(os.path.join(Data.MC, "versions", "*"))):
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

#            os.system('cls' if sys.platform.startswith("win") else 'clear')
            Buff.append("&2╔" + ("═" * (x - 2) + "╗"))
            Buff.append("&2║" + ("&bPyLauncherMC " + __version__).center(x) + "&2║")
            Buff.append("&2╠" + ("═" * (x - 2) + "╣"))
            Buff.append("&2║ " + "&ePor favor, presione el numero que corresponda a su version&f:".ljust(x + 1) + "&2║")
            for i, version in self.Versions.items():
                if i != '0':
                    Buff.append("&2║ " + ("&b%s&f) &b%s" % (i, version)).ljust(x + 3) + "&2║")
            for _ in range(len(Buff), y - 2):
                Buff.append("&2║" + (" " * (x - 2) + "║"))
            Buff.append("&2║ " + self.input.ljust(x - 3) + "║")
            Buff.append("&2╚" + ("═" * (x - 2) + "╝"))

            log.add("\n".join(Buff))
            time.sleep(1 / 15) # 15 FPS

    def getVersion(self):
        key = ""
        while not self.exit:
            if key.isdigit():
                self.input = "> " + key
                if key == '0' or self.Versions.get(key, None):
                    break

            try:
                key = keyboard.read_key()

            except KeyboardInterrupt:
                key = '0'
                break

            except: pass

        if key == '0':
            self.input = "Abortando ..."
        else: self.input = "Lanzando ..."

        time.sleep(0.1)

        return self.Versions.get(key, None)

    def stop(self):
        self.exit = True

with PB("Cargando variables por defecto."):
    class Data:
        Debug       = False
        JVM         = 'java'
        MinRam      = '1G'
        MaxRam      = '1G'
        MC          = '.'
        Lib         = os.path.join('{Data.MC}', 'libraries')
        CLASSPATH   = []
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
                '-Dsun.java2d.d3d=true',
                '-Dsun.java2d.opengl=false',
                '-Dorg.lwjgl.opengl.Display.allowSoftwareOpenGL=false',
#               '-Xlog:gc*:logs/gc.log:time,uptime:filecount=5,filesize=1M',
                '-XX:+AggressiveOpts',
                '-XX:-UseCompressedOops',
                '-XX:ParallelGCThreads=4',
                '-Dorg.lwjgl.opengl.Display.setFullscreen=true',
                '"-Djava.library.path={Data.Natives}"',
                '-cp "{Data.CLASSPATH}"',
                '"-Dlog4j.configurationFile=%s"' % os.path.join('{Data.Lib}', 'client-1.7.xml')
            ]

            MC  = [
                '--gameDir ' + os.path.join('{Data.MC}', '{Data.Version}'),
                '--assetsDir ' + os.path.join("{Data.MC}", 'assets'),
                '{Data.Nick}',
                '--accessToken {Data.Token}',
                '--version "{Data.Version}"',
                '--assetIndex {Data.AssetsIndex}',
                '--userProperties {{}}'
            ]

def Launch(Data, args):
    Data.JVM         = Data.JVM         .format(Data = Data)
    Data.MinRam      = Data.MinRam      .format(Data = Data)
    Data.MaxRam      = Data.MaxRam      .format(Data = Data)
    Data.MC          = Data.MC          .format(Data = Data)
    Data.Lib         = Data.Lib         .format(Data = Data)
    Data.CLASSPATH   = ";".join([D.format(Data = Data) for D in Data.CLASSPATH])
    Data.Natives     = Data.Natives     .format(Data = Data)
    Data.MainClass   = Data.MainClass   .format(Data = Data)
    if Data.Nick: Data.Nick = "--username " + Data.Nick .format(Data = Data)
    Data.Token       = Data.Token       .format(Data = Data)
    Data.Version     = Data.Version     .format(Data = Data)
    Data.AssetsIndex = Data.AssetsIndex .format(Data = Data)

    Data.Flags.JVM   = " ".join([D.format(Data = Data) for D in Data.Flags.JVM])
    Data.Flags.MC    = " ".join([D.format(Data = Data) for D in Data.Flags.MC])

    CommandLine = " ".join([Data.JVM, Data.Flags.JVM, Data.MainClass, Data.Flags.MC])
    if Data.Debug:
        log.add(CommandLine)
    else:
        try: os.system(CommandLine)
        except KeyboardInterrupt: pass

if __name__ == "__main__":
    log.show().start(daemon = True)

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

    cli = CLI()
    if Data.Version is None:
        cli.start()
        Data.Version = cli.getVersion()

    cli.stop()

    if Data.Version is not None:
        try:
            dir = os.path.join(Data.MC, "versions", Data.Version)
            os.makedirs(dir, exist_ok = True)
            with PB("Cargando Minecraft %s." % Data.Version):
                Data = runpy.run_path(os.path.join(dir, Data.Version + ".py"), init_globals = {"Data": Data, "log": log, "args": args}).get("Data", None)
            assert Data, "Version incompatible o mal estructurada."
            Launch(Data, args)

        except AssertionError as e:
            log.add(e)

        except FileNotFoundError:
            log.add("Archivo de configuracion no encontrada")

        except: pass

    exit()