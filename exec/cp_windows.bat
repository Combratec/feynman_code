@echo off
color a

echo Certifique-se que a vers�o do Python � a 3.7.2
echo Execute os comandos abaixo caso tenha erro:
pip install --upgrade pip
pip install pyinstaller --upgrade
pip install setuptools --upgrade

echo Deletando arquivo safira.exe
del safira.exe

echo Criando uma c�pia tempor�ria
copy safira.py safira.pyw

echo Gerando o Execut�vel
pyinstaller --onefile --icon="imagens\icone.ico" safira.pyw

echo Tornando o execut�vel acessivel
move dist\safira.exe .

echo Deleteando o arquivo tempor�rio
del safira.pyw

echo deletando o residuo safira.spec
del safira.spec

echo deletando pasta build/
rd /s  /q build

echo deletando pasta dist/
rd /s  /q dist

color e
pause
