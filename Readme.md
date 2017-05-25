# LEEME

## Instalacion

El Simulador corre sobre Python, utilizando el framework Flask para proveer un entorno web contra el cual la UI (implementada en HTML y Javascript) hará las requests.

Para mantener las dependencias encapsuladas, se puede utilizar un virtualenv, aunque no es obligatorio. Por eso hay dos formas de instalarlo.

### Con virtualenv (mas largo)

Para instalar las dependencias, se recomienda hacerlo dentro de un virtualenv para no tener conflictos de librerias.

El virtualenv se puede crear de la siguiente forma (instrucciones para Ubuntu)

Primero se instalan los paquetes necesarios:

```
sudo apt-get install wget unzip git mercurial python-setuptools python-imaging
sudo easy_install pip
pip install virtualenv
```

Una vez en la carpeta del proyecto, se crea un nuevo virtualenv:
```
virtualenv .env
```

Luego, se activa el virtual de la siguiente forma
```
source .env/bin/activate
```

El virtualenv se debera activar cada para correr el proyecto. Una vez dentro del virtualenv, se instalan las librerias necesarias:
```
pip install reqs.txt
```

### Sin virtualenv (mas rapido)

Se instalan directamente las dependencias en la maquina propia (Flask mas que nada) con
```
pip install reqs.txt
```

## Correr
Para correr el servidor, se hace de la siguiente forma:
```
python app.py
```
Eso mostrara una URL en la consola (casi siempre de la forma 127.0.0.1:5000 o 0.0.0.0:5000) a la cual se puede acceder desde el browser. Alli se vera la UI.