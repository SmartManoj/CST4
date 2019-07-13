import winreg,os

def set_reg(REG_PATH,name, value):
	try:
		winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, REG_PATH)
		registry_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, REG_PATH, 0, 
									   winreg.KEY_WRITE)

		winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
		winreg.CloseKey(registry_key)
		return True
	except WindowsError as e:
		return False

def get_reg(REG_PATH,name):
	try:
		registry_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, REG_PATH, 0,
									   winreg.KEY_READ)
		value, regtype = winreg.QueryValueEx(registry_key, name)
		winreg.CloseKey(registry_key)
		return value
	except WindowsError as e:
		return None

if __name__ == '__main__':
	# print(get_reg(r"tdesktop.tg\shell\open\command",''))
	print(set_reg(r"tdesktop.tg\shell\open\command",'cst3','854'))
	print(get_reg(r"tdesktop.tg\shell\open\command",'7cst3'))