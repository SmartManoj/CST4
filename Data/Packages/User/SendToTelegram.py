import sublime
import sublime_plugin
import os

class SendToTelegram(sublime_plugin.TextCommand):
	def run(self, edit):
		fileToOpen = self.view.file_name()
		if self.view.is_dirty():
				print("File %s is dirty. Saving..." % (fileToOpen,))
				self.view.window().run_command("save")

		a=(r'D:\1.Manoj\2.Soft-war\5.Rest\Telegram\T.exe -sendpath "{}"'.format(fileToOpen))
		print(a)
		os.system(a)
