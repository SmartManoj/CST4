import sublime
import sublime_plugin
import re

class RubyCommand(sublime_plugin.TextCommand):
	def ruby(self,a):
		return a+'5'
	def run(self, edit):
		r=sublime.Region(0, self.view.size())
		content=self.view.substr(r)
		self.view.replace(edit,r,self.ruby(content))
