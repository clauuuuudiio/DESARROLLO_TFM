# Desarrollo del chatbot y la integración omnicanal del TFM

### Crear entorno virutal
Para crear un entorno virtual, donde descargar las dependencias del proyecto, es necesario descargar el paquete `virtualenv` mediante el siguiente comando:

```
pip install virtualenv
```
\
Después se creará el entorno virtual, llamado *env*.

```
virtualenv -p python3 env
```
\
Una vez creado el entorno hay que activarlo indicando la siguiente ruta.
```
.\env\Scripts\activate
```
\
Al activar el entorno se indica mediante (env) en la consola de comandos que se ha activado correctamente. Además se pueden listar las dependencias del entorno mediante `pip list`. 
\
Si dentro del entorno virtual se instala una nueva dependendecia únicamente se podrá utilizar dentro de este.
\
\
Finalmente, cuando se quiere deactivar el entorno virutal habrá que ejecutar el siguiente comando:

 ```
deactivate
```
\
Las dependencias instaladas son:

 ```
pip install transformers langchain langchain-community 
```