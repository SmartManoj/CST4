import sublime
import sublime_plugin

class ExecOutputFocusCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.window.run_command('show_panel', args={'panel': 'output.exec'})
    self.window.focus_view(self.window.find_output_panel("exec"))