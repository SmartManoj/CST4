@echo off
cd ..\..
rem subl .git\info\exitclude
rem exit
rem heroku accounts:set p


git init
git add .
git commit -m 'Cool'
git push --set-upstream https://github.com/SmartManoj/CST3 master
git push origin master --force
git remote add origin https://github.com/SmartManoj/CST3.git
git push --force origin master
rem git push -u  https://github.com/SmartManoj/CST3  --force
echo %date%,%time%
rem zmsg