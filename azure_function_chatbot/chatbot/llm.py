from langchain_openai import AzureChatOpenAI
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
import os
from chatbot.memory import get_memory, save_memory
from chatbot.database import DatabaseConnection
import logging

def llm_generate():
    # Cargar las variables mediante os
    os.environ["OPENAI_API_VERSION"] = os.getenv("OPENAI_API_VERSION")
    os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv("AZURE_OPENAI_ENDPOINT")
    os.environ["AZURE_OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY")
    
    llm = AzureChatOpenAI(
        deployment_name="prueba-gpt-35-turbo",
        temperature=0,
        max_tokens=25,
    )
    
    return llm

def prompt_generate():
    template = """
Eres un asistente diseñado para ayudar a los usuarios respondiendo preguntas de forma clara y respetuosa.

{history}

Pregunta: "{input}"

Por favor, proporciona una respuesta útil y amigable.
Respuesta:
"""
    
    prompt = PromptTemplate(input_variables=["history", "input"], template=template)
    
    return prompt

def chatbot_generate(id, canal, conn):
    chatbot = ConversationChain(
        llm=llm_generate(), 
        memory=get_memory(id, canal, conn),
        prompt=prompt_generate()
    )
    
    return chatbot

def response_generate(id, canal, question):
    db = DatabaseConnection()
    conn = db.connect()
        
    logging.info('Inicio creación del chatbot')
    chatbot = chatbot_generate(id, canal, conn)
    logging.info('Creación del chatbot correcta')

    
    logging.info('Inicio de la respuesta')
    response = chatbot.predict(input=question)
    logging.info('Obtención de la respuesta correcta')


    save_memory(id, canal, question, response, conn)
    
    db.close()
    
    return response