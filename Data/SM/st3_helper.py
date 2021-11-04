from pyperclip import *
import re
a=paste()
a=re.sub('([A-Z])',r'_\1',a)[1:].lower()
copy(a)