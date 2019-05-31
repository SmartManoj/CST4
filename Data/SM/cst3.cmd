@echo off
cd ..\..
rem subl .git\info\exitclude
rem exit
rem heroku accounts:set p


git init
git add .

git commit -m 'Cool'
rem git push --set-upstream https://github.com/SmartManoj/CST3 master
rem git push origin master --force
rem git remote add origin https://github.com/SmartManoj/CST3.git
git push --force origin master
rem git push -u  https://github.com/SmartManoj/CST3  --force
echo %date%,%time%
zmsg