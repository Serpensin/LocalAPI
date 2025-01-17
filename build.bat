@echo off
set /p version="Enter Version: "

./env/Scripts/nuitka.bat "main.py" -o "Local API" --plugin-enable=tk-inter --lto=yes --python-flag=no_site --plugin-enable=pylint-warnings --remove-output --standalone --onefile --company-name="Serpent Modding" --product-name="LocalAPI" --file-version=%version% --file-description="This serves locally saved json files." --windows-icon-from-ico="./icon.ico" --include-data-dir="./static/=static"