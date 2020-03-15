@echo off
color a

echo Certifique-se que a vers�o do Python � a 3.7.2
echo Execute os comandos abaixo caso tenha erro:
python -m pip install --upgrade pip
python -m pip install pyinstaller

echo Deletando arquivo feynman.exe
del feynman.exe

echo Criando uma c�pia tempor�ria
copy script.py feynman.pyw

echo Gerando o Execut�vel
pyinstaller --onefile -windowed --icon=app.ico feynman.pyw

echo Tornando o execut�vel acessivel
move dist\feynman.exe .

echo Deleteando o arquivo tempor�rio
del feynman.pyw

echo deletando o residuo feynman.spec
del feynman.spec

echo deletando pasta build/
rd /s  /q build

echo deletando pasta dist/
rd /s  /q dist

color e
pause