rm -rf main.deb
pip3 install -r requirements.txt
python3 -m eel runner.py statics/ --add-data './.env:.'
pyinstaller runner.spec
#!/bin/sh
# Create folders.
[ -e package ] && rm -r package
mkdir -p package/opt
mkdir -p package/usr/share/applications
mkdir -p package/usr/share/icons/hicolor/scalable/apps

# Copy files (change icon names, add lines for non-scaled icons)
cp -r dist/runner package/opt/main
cp statics/icons/elmos.svg package/usr/share/icons/hicolor/scalable/apps/main.svg
cp main.desktop package/usr/share/applications

# Change permissions
find package/opt/main -type f -exec chmod 644 -- {} +
find package/opt/main -type d -exec chmod 755 -- {} +
find package/usr/share -type f -exec chmod 644 -- {} +
chmod +x package/opt/main/runner
fpm