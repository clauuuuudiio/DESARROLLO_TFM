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
Las dependencias instaladas son: (Azure OpenAI)

 ```
pip install langchain langchain-community openai azure-identity
```

## Creación del asistente conversacional

Para la creación del chatbot se va a utilizar langchain y se realizará en el directorio `app.py`. Dentro de este archivo se definirá la función main encargada de realizar una petición al modelo y esperar una respuesta. Hay dos modulos más dentro de la carpeta llm que se encargan de crear el Chatbot y de crear o recuperar la conversación. En el modulo `chatbot.py` se genera el LLM, el prompt template y el asistente conversacional, al cual se invocará para obtener la respuesta. Por otro lado, en el módulo `memory.py` se crea o se recupera la conversación si existe. 


Se va a utilizar Azure OpenAI para crear el Chatbot. 