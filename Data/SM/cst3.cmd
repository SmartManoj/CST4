@echo off
rem exit
rem heroku accounts:set p
call a.cmd
git rm -r --cached Data\Backup
git rm -r --cached Data\Cache
git init
git add .
git commit -m 'Cool'
exit
rem git push --set-upstream https://github.com/SmartManoj/CST3 master
rem git push origin master --force
rem git remote add origin https://github.com/SmartManoj/CST3.git
git push --force origin master
rem git push -u  https://github.com/SmartManoj/CST3  --force
echo %date%,%time%
zmsg