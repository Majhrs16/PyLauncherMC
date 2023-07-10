from threading import Thread
import colorama

class _dThread(Thread):
    def __init__(self, funcion, *args, **kw):
        super().__init__()
        self.funcion = funcion
        self.args = args
        self.kwargs = kw

    def run(self):
        self.funcion(*self.args, **self.kwargs)

    def start(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        Thread.start(self)

def dThread(func):
    def decorator(*args, **kw):
        return _dThread(func, *args, **kw)
    return decorator

if __name__ == "__main__":
    @dThread
    def Func(abc):
        print(abc)

    x = Func(123)
    x.start(daemon = False)
    x.start(daemon = True)
    x.start(daemon = True)
    print("OK")
    exit()


class Color:
    def __enter__(self):
        colorama.init()
        return self

    def __exit__(self, *x):
        colorama.deinit()

    def clear(self):
        print(colorama.ansi.clear_screen())

    def translate(self, str):
        colores_minecraft = {
            "&0": colorama.Fore.BLACK,
            "&1": colorama.Fore.BLUE,
            "&2": colorama.Fore.GREEN,
            "&3": colorama.Fore.CYAN,
            "&4": colorama.Fore.RED,
            "&5": colorama.Fore.MAGENTA,
            "&6": colorama.Fore.YELLOW,
            "&7": colorama.Fore.WHITE,
            "&8": colorama.Fore.BLACK + colorama.Style.BRIGHT,
            "&9": colorama.Fore.BLUE + colorama.Style.BRIGHT,
            "&a": colorama.Fore.GREEN + colorama.Style.BRIGHT,
            "&b": colorama.Fore.CYAN + colorama.Style.BRIGHT,
            "&c": colorama.Fore.RED + colorama.Style.BRIGHT,
            "&d": colorama.Fore.MAGENTA + colorama.Style.BRIGHT,
            "&e": colorama.Fore.YELLOW + colorama.Style.BRIGHT,
            "&f": colorama.Fore.WHITE + colorama.Style.BRIGHT,
            "&r": colorama.Style.RESET_ALL,
            "&m": colorama.Style.DIM,
            "&l": colorama.Style.BRIGHT,
        }

        for codigo, color in colores_minecraft.items():
            str = str.replace(codigo, color)

        return str