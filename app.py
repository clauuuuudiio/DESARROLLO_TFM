from langchain_openai import AzureChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

def get_memory(id):
    # Recupera o crea la memoria del chatbot
    memory = ConversationBufferMemory()
    lista_mensajes = get_mensajes(id)
    for mensajes in lista_mensajes:
        memory.save_context(mensajes.input, mensajes.output)
    return memory

def get_mensajes(id):
    # Obtener los mensajes de la BBDD
    lista_mensajes  = []
    return lista_mensajes

def llm_generate():
    llm = AzureChatOpenAI(
        deployment_name="prueba-gpt-35-turbo",
        temperature=0.1,
        max_tokens=100,
    )
    return llm
    
def chatbot_generate(id):
    chatbot = ConversationChain(
        llm=llm_generate(), 
        memory=get_memory(id),
        prompt=PromptTemplate(input_variables=["history", "input"], template=template_generate())
    )
    return chatbot

def template_generate():
    template = """
    Eres un asistente conversacional, que debe responder la pregunta o duda del usuario
    
    {history}
    
    El usuario a preguntado "{input}", respondela de manera amigable.
    """
    return template

def response_generate(id, pregunta):
    chatbot = chatbot_generate()
    response = chatbot.predict(input=pregunta)
    return response

def main():
    id = 1
    pregunta = "Dime la capital de Argentina"
    response = response_generate(id, pregunta)
    return response

if __name__ == "__main__":
    main()