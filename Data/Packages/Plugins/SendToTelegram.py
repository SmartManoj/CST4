def r():
	#Python3 version of hugo24's snippet
	import winreg,os


	REG_PATH = r"tg\shell\open\command"
	def set_reg(name, value):
		try:
			winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
			registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, 
										   winreg.KEY_WRITE)
			winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
			winreg.CloseKey(registry_key)
			return True
		except WindowsError as e:
			print(e)
			return False

	def get_reg(name):
		try:
			registry_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, REG_PATH, 0,
										   winreg.KEY_READ)
			value, regtype = winreg.QueryValueEx(registry_key, name)
			winreg.CloseKey(registry_key)
			return value
		except WindowsError as e:
			print(e)
			return None

	#Example MouseSensitivity
	#Read value 
	path="D:\1.Manoj\2.Soft-war\5.Rest\Telegram\T.exe"
	path2='/'.join(path.split('\\')[:-1])
	f=''' """{path}\"" -workdir ""{path2}"" -- ""%1\""" /f '''
	# print(set_reg('1',f))
	a=get_reg('').split('"')[1]
	if r'\\' in a:
		a=a.split('\\')
		b='\\'.join(a[4:])
		a="{}:\\{}".format(a[3][0],b)
	print('3',a)
	print('TG=r"{}"'.format(a),file=open(__file__+'\..\config.py','a'))
import os
print("42",os.getcwd(),)
try:
	from .config import *
	TG
	print('3',TG)
except Exception as e:
	r()

	from .config import *
import sublime
import sublime_plugin
import os

class SendToTelegram(sublime_plugin.TextCommand):
	print("TG2",TG)
	def run(self, edit):
		fileToOpen = self.view.file_name()
		if self.view.is_dirty():
				print("File %s is dirty. Saving..." % (fileToOpen,))
				self.view.window().run_command("save")


		a=('{} -sendpath "{}"'.format(TG,fileToOpen))
		print(a)
		os.system(a)
