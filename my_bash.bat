@echo off
pip "install" "-r" "requirements.txt"
python -m eel runner.py statics --add-data "./.env;." --onefile --hidden-import behave.__main__ --hidden-import pymongo --hidden-import names --hidden-import behave.formatter.pretty
pyinstaller "runner.spec"
DEL /S "package"
mkdir  "package\opt"
mkdir  "package\usr\share\applications"
mkdir  "package\usr\share\icons\hicolor\scalable\apps"
COPY  "dist\runner" "package\opt\main"
COPY  "statics\icons\elmos.svg" "package\usr\share\icons\hicolor\scalable\apps\main.svg"
COPY  "main.desktop" "package\usr\share\applications"