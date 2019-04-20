import sublime
import sublime_plugin
import re

class RubyCommand(sublime_plugin.TextCommand):
	def ruby(self,a):
		r=re.findall(r'<person>.*?</person>',a,re.M|re.S)
		for i in r:
			c=1
			t=i
			while 'item>' in i:
				i=i.replace('item>','item{0}>'.format(c),2)
				c+=1
			a=a.replace(t,i)
		return a
	def run(self, edit):
		r=sublime.Region(0, self.view.size())
		content=self.view.substr(r)
		self.view.replace(edit,r,self.ruby(content))
