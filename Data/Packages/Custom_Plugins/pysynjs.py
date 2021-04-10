import sublime
import sublime_plugin


class PySynJsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# self.view.insert(edit, 0, "aaz")
		self.view.set_syntax_file("Packages/JavaScript/JavaScript.sublime-syntax")
		self.view.run_command("code_formatter")
		self.view.set_syntax_file("Packages/Python/Python.sublime-syntax")