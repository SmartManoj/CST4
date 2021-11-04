@echo off
rem exit
rem heroku accounts:set p
call a.cmd
rem git init
git push --set-upstream https://github.com/SmartManoj/CST4 main
git remote add origin https://github.com/SmartManoj/CST4.git

if "1" EQU "1." (
	git pull origin main
	git mergetool 
	pause & exit
)	
rem git checkout --orphan main
rem git rm -r --cached .
git add .
rem git rm -r --cached 	Data/Cache
git commit -m 'Cool'
git push --force origin main 
rem git push  origin master
rem git push -u  https://github.com/SmartManoj/CST3  --force
echo %date%,%time%
rem zmsg
pause