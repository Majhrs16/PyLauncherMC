
try:
	from ctypes     import WinDLL
	k = WinDLL("kernel32")
	k.SetConsoleMode(k.GetStdHandle(-11), 7)
except: WinDLL = None
from threading      import Thread #, _active_limbo_lock, _limbo, _start_new_thread, _HAVE_THREAD_NATIVE_ID, _active, _trace_hook, _profile_hook
from socket         import socket, AF_INET, SOCK_DGRAM
from urllib.request import build_opener
from uuid           import getnode
import re
import sys


class ProgressBar(object):
	def __init__(self, max, width=50):
		self._T = max
		self._X = width
		self.i  = 0

	def __exit__(*x):
		pass

	__iter__ = __enter__ = lambda self: self
	step = __next__ = lambda self, i = +1: self.set(self.i + i)

	def get(self, _ = 100):
		return _ * self.i / float(self._T)

	def set(self,i):
		self.i  = i
		percent = "{0:.2f}".format(self.get())
		bar     = round(self.get(self._X))
		print("\r[{0}] {1}%\r".format("█" * bar + "-" * (self._X - bar), percent), end = "")
PB = ProgressBar

def FormatErr(Exc): return (str(Exc.__class__.__name__), str(Exc))
def PrintErr(Exc): print(*FormatErr(Exc), sep = ": ", file = ERR)

def MAC():
	MAC=hex(getnode())[2:].upper()
		# f'{getnode():02x}'.upper()
		# '{:02x}'.format(getnode()).upper()
		# "%x".upper() % x
	return ":".join([MAC[i:i+2] for i in range(0,len(MAC),2)])

def Percent(s): ## algo no me convence...ujummmm, lo veo algo inpotente y rebundante aunq, a veces es muy util....
	"""Percent(str) -> float
    >>> Percent("30%1200")
    360.0
    >>> Percent("30-%1200")
    330.0
    >>> Percent("30+%1200")
    330.0
"""
	if match("\d+\%\d+",s):
		v=s.split("%")
		v=float(v[0])*float(v[1])/100
	elif match("\d+\+\%\d+",s):
		v=s.split("+%")
		v=float(v[0])*float(v[1])/100+float(v[0])
	elif match("\d+\-\%\d+",s):
		v=s.split("-%")
		v=float(v[0])*float(v[1])/100-float(v[0])
	else: raise ValueError(Percent.__doc__)
	return v

def _GetSize(num, max, Bits):
	if not isinstance(num,(int,float)): raise TypeError("{!r} != float/int".format(num))
	if num<0: raise ZeroDivisionError("not {!r} > 0".format(num))
	if max is not None and max not in range(8 +1): raise IndexError("{!r} not in range(0, 8 +1)".format(max))

	Multiple = 1000 if Bits else 1024
	Sufijos  = {
		1024:["B","KB","MB","GB","TB","PB","EB","ZB","YB"],
		1000:["b","Kb","Mb","Gb","Tb","Pb","Eb","Zb","Yb"]
	}[Multiple]
	for Sufijo in Sufijos:
		if max and Sufijo==Sufijos[max]:
			return (num, Sufijo)
		elif num <= Multiple: return (num, Sufijo)
		num /= Multiple

	raise OverflowError("Max value: %s" % 1024**8)
def GetSize(num: "int or float", max: 8 = None, Bits: bool = False):
	"""
GetSize(int or float, int, bolean) -> float
    >>> GetSize(1024 ** 4)
    '1 TB'
    >>> GetSize(1024 ** 4, 2) # TB -> MB
    '1048576 MB'
    >>> GetSize(1024 ** 3, Bits = True) # GByte -> Gbit
    '1.07 Gb'
"""
	num, Sufijo = _GetSize(num, max, Bits)
	return "{0:.2f} {1}".format(int(num) if int(num) == num else num, Sufijo)

def NetIP():
	try:
		s = socket(AF_INET, SOCK_DGRAM)
		s.connect(("8.8.8.8", 80))
		return s.getsockname()[0]
	finally: s.close()

def iNetIP(timeout = 60):
	web            = build_opener()
	web.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')]
	sock           = None
	try:
		sock       = web.open("ifconfig.me/ip", timeout = timeout)
		return sock.read().decode()
	except Exception as e: return e
	finally: sock and sock.close()

class Class(object):
	def __init__(self,**Kw): self.__dict__.update(Kw)
	def __setitem__(self,k,v): self.__dict__[k]=v
	def __getitem__(self,k): return self.__dict__[k]
	def __delitem__(self,k): del self.__dict__[k]
	def __repr__(self): return str(self.__dict__)

""" # NO COMPATIBLE CON LINUX
class _Thread(Thread):
	def __call__(self):
		self.start()
		return self

	def start(self):
		if not self._initialized: raise RuntimeError("thread.__init__() not called")
		if self._started.is_set(): raise RuntimeError("threads can only be started once")
		with _active_limbo_lock: _limbo[self] = self
		try: _start_new_thread(self._bootstrap, ())
		except Exception:
			with _active_limbo_lock: del _limbo[self]
			raise
		self._started.wait()

	def run(self):
		try:
			if self._target is not None: return self._target(*self._args, **self._kwargs)
		finally: del self._target, self._args, self._kwargs

	def _bootstrap(self):
		try: self.value = self._bootstrap_inner()
		except:
			if self._daemonic and _sys is None: return
			raise

	def _bootstrap_inner(self):
		try:
			self._set_ident()
			self._set_tstate_lock()
			if _HAVE_THREAD_NATIVE_ID: self._set_native_id()
			self._started.set()
			with _active_limbo_lock:
				_active[self._ident] = self
				del _limbo[self]
			if _trace_hook: _sys.settrace(_trace_hook)
			if _profile_hook: _sys.setprofile(_profile_hook)
			try: return self.run()
			except: self._invoke_excepthook(self)
		finally:
			with _active_limbo_lock:
				try: del _active[get_ident()]
				except: pass

	def wait_value(self):
		self.join()
		return self.value
"""

if WinDLL:
	class console:
	    def _windowsConsole(self, state):
	        WinDLL('user32').ShowWindow(WinDLL('kernel32').GetConsoleWindow(), state)
	    def minimize(self): self._windowsConsole(6)
	    def restore(self): self._windowsConsole(9)
	    def hide(self): self._windowsConsole(0)

else:
	console = None

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

class Color:
    colors = {
        '&0': '\033[30m',
        '&1': '\033[34m',
        '&2': '\033[32m',
        '&3': '\033[36m',
        '&4': '\033[31m',
        '&5': '\033[35m',
        '&6': '\033[33m',
        '&7': '\033[37m',
        '&8': '\033[90m',
        '&9': '\033[94m',
        '&a': '\033[92m',
        '&b': '\033[96m',
        '&c': '\033[91m',
        '&d': '\033[95m',
        '&e': '\033[93m',
        '&f': '\033[97m',
        '&r': '\033[0m'
    }

    def __enter__(self):
        return self

    def __exit__(self, *x):
        pass

    def _clear(self):
    	return '\033c'

    def clear(self):
    	sys.stdout.write(self._clear())

    def cleartext(self, text):
    	return self.translate(text, {k: '' for k, v in self.colors.items()})

    def translate(self, text, _colors = None):
        if _colors is None: _colors = self.colors

        pattern = re.compile('|'.join(re.escape(key) for key in _colors.keys()))
        return pattern.sub(lambda match: _colors[match.group()], text)