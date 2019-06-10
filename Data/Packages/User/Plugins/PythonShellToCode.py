import sublime
import sublime_plugin


class PythonShellToCodeCommand(sublime_plugin.TextCommand):
	def ruby(a):
		b=[]
		for i in a.splitlines():
			j=i.lstrip('>.')
			if i!=j:
				b.append(j[1:])
			else:
				b.append('# '+i)
		return "\n".join(b)
	def run(self, edit):
		r=sublime.Region(0, self.view.size())
		content=self.view.substr(r)
		self.view.replace(edit,r,self.ruby(content))
