@echo off
rem exit
rem heroku accounts:set p
call a.cmd
rem git init

if "1" EQU "1." (
	git pull origin master
	git mergetool 
	pause & exit
)	

git add .
rem git rm -r --cached Data/Backup
rem git rm -r --cached 	Data/Cache
git commit -m 'Cool'
rem git push --set-upstream https://github.com/SmartManoj/CST3 master
rem git remote add origin https://github.com/SmartManoj/CST3.git
git push --force origin master 
rem git push  origin master
rem git push -u  https://github.com/SmartManoj/CST3  --force
echo %date%,%time%
zmsg