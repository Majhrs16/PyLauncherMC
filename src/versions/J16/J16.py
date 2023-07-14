from os.path import join
class Data(Data):
	Natives     = join(Data.MC, 'versions', Data.Version, 'natives')
	AssetsIndex = '1.16'
Data.Flags.JVM[-1] = '-Dlog4j.configurationFile=%s' % join(f'{Data.Lib}', 'client-1.12.xml')