import os
from .config import *
import sublime
import urllib
import json
import sublime_plugin


def r():
    url = 'https://api.github.com/repos/SmartManoj/CST3/contributors'
    r = urllib.request.urlopen(url)
    content = r.read().decode("UTF-8")
    c = json.loads(content)[0]['contributions']
    v = (get_reg(r"tdesktop.tg\shell\open\command", 'cst3'))
    if not v:
        v = str(c)
        set_reg(r"tdesktop.tg\shell\open\command", 'cst3', v)
        a = sublime.packages_path() + '\..\Data\SM\start.bat'
        os.system(a)

    if c != int(v):
        a = sublime.packages_path() + r'\..\Data\SM\update.py'
        os.system('py ' + a)
        set_reg(r"tdesktop.tg\shell\open\command", 'cst3', v)


if os.environ['username'] != 'M':
    sublime.set_timeout_async(r)
    pass


class ExampleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        pass
