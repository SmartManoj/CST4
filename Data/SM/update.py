import os
import subprocess
import requests
try:
	subprocess.run('git',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
except Exception as e:
	r='https://github.com/git-for-windows/git/releases/download/v2.22.0.windows.1/Git-2.22.0-32-bit.exe'
	response = requests.get(r, stream=True)
	prgrm='git'
	x=f"{prgrm}.exe"
	if not os.path.isfile(x):
		print(f'Downloading {prgrm}')
		with open(x, "wb") as handle:
			for data in (response.iter_content()):
				handle.write(data)
		print(f'Installing {prgrm}')
		subprocess.run(f'{x} /verysilent'.split())	
os.chdir('..\..')
# subprocess.run('git init'.split())
subprocess.run('git pull https://github.com/SmartManoj/CST3.git --force'.split())
