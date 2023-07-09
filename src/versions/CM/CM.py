from os.path import join
class Data(Data):
	Natives = join(Data.MC, 'versions', Data.Version, 'natives')
	CLASSPATH = [
		join(f"{Data.Lib}", 'log4j-core-2.17.0.jar'),
		join(f"{Data.Lib}", 'log4j-api-2.17.0.jar'),
		join(f"{Data.MC}", 'versions', f"{Data.Version}", f"{Data.Version}.jar"),
	]