import sublime_plugin
import sublime
# sublime.message_dialog('34')


class ExampleCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        self.view.insert(edit, 0, "Hello, World!")
