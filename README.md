
# IRIS OSINT ![](https://img.shields.io/badge/src-public-green) ![](https://img.shields.io/github/forks//IRIS-Team/IRIS/) ![](https://img.shields.io/github/stars/IRIS-Team/IRIS) ![](https://img.shields.io/github/issues/IRIS-Team/IRIS)

## Infomation on project
IRIS is a simple way to do OSINT on a username, email, or domain. Get results on databreaches, sites the target has used, google dorks that can lead to more infomation and much more.
_______________________
## Installation
#### Windows
Dowload IRIS From [Here](https://github.com/IRIS-Team/IRIS/archive/refs/heads/main.zip)

Download [Python 3.9](https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe)

***YES IT HAS TO BE PYTHON 3.9***
```
cd DOWNLOAD_LOCATION/IRIS/

py -m pip install -r requirements.txt
py -m iris
```
#### Linux (Debian)
```
sudo apt-get update
sudo apt-get install python3.9 python3-pip

git clone https://github.com/IRIS-Team/IRIS/
cd IRIS/

python3.9 -m pip install -r requirements.txt
python3.9 -m iris
```
#### Arch Linux
```
pacman -S python3.9
pacman -S python-pip

git clone https://github.com/IRIS-Team/IRIS/
cd IRIS/

python3.9 -m pip install -r requirements.txt
python3 -m iris
```

_______________________

### Modules
Category | Module Name | Description |
| - | - | - |
Database | WeLeakInfo | Look up a email or username with the WeLeakInfo API |
| - | - | - |
Doxxing | Doxbin | Lookup published doxxes from DoxBin site |
| - | - | - |
Minecraft | Minecraft | Get Minecraft account information by username/UUID |
Minecraft | NameMC | Get NameMC profile information by Minecraft username/UUID |
Minecraft | Plancke | Get Plancke account information by Minecraft username/UUID |
| - | - | - |
Social | Github | Get GitHub account information by username |
Social | Solo To | Get social media profiles on solo by username |
Social | Keybase | Get Keybase account information by username
| - | - | - |
Other | Typer Racer | Get email-address of Typeracer user by username

Let me know if you have any problems on my [Discord Server](https://discord.gg/NBPCseG6g4)
