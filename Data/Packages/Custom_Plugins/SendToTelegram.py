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


import os
# print("42",os.getcwd(),)
from .config import *
import sublime
import sublime_plugin
import os
TG=get_reg(r"tdesktop.tg\shell\open\command",'').split(' -')[0]


class SendToTelegram(sublime_plugin.TextCommand):
	def run(self, edit):
		fileToOpen = self.view.file_name()
		if self.view.is_dirty():
				print("File %s is dirty. Saving..." % (fileToOpen,))
				self.view.window().run_command("save")


		a=('{} -sendpath "{}"'.format(TG.strip()[1:-1],fileToOpen))
		print(a)
		os.system(a)
