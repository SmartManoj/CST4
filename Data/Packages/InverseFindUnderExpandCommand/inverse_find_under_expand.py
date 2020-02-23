import sublime, sublime_plugin

class InverseFindUnderExpandCommand(sublime_plugin.TextCommand):
    "Add the previous occurrence of the word under the cursor to the selection"

    def run(self, edit):
        sel = [s for s in self.view.sel()]

        new_sel = []

        for s in sel:
            self.view.sel().clear()
            self.view.sel().add(s)

            self.view.window().run_command('find_under_prev')

            for ns in self.view.sel():
                new_sel.append(ns)

        self.view.sel().clear()

        for s in sel:
            self.view.sel().add(s)

        for s in new_sel:
            self.view.sel().add(s)