@echo off
rem exit
rem heroku accounts:set p
call a.cmd
rem git init
git add .
rem git rm -r --cached Data/Backup
rem git rm -r --cached 	Data/Cache

git commit -m 'Cool'
git push --set-upstream https://github.com/SmartManoj/CST3 master
git push origin master --force
rem git remote add origin https://github.com/SmartManoj/CST3.git
rem git push  origin master
rem git push -u  https://github.com/SmartManoj/CST3  --force
echo %date%,%time%
zmsg