pip install pyinstaller
pyinstaller --onefile cli.py
cd dist
mv cli taskily
cp taskily /usr/local/bin
cd ..
rm -r dist
rm -r build
